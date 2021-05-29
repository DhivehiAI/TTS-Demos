import tensorflow as tf
import numpy as np
import re

token_mapping = {
    ' ': 1, '!': 2, "'": 3, '-': 4, '.': 5,
    ':': 6, ';': 7, '،': 8, '؟': 9, 'ހ': 10,
    'ށ': 11, 'ނ': 12, 'ރ': 13, 'ބ': 14, 'ޅ': 15,
    'ކ': 16, 'އ': 17, 'ވ': 18, 'މ': 19, 'ފ': 20,
    'ދ': 21, 'ތ': 22, 'ލ': 23, 'ގ': 24, 'ޏ': 25,
    'ސ': 26, 'ޑ': 27, 'ޒ': 28, 'ޓ': 29, 'ޔ': 30,
    'ޕ': 31, 'ޖ': 32, 'ޗ': 33, 'ޘ': 34, 'ޙ': 35,
    'ޚ': 36, 'ޛ': 37, 'ޜ': 38, 'ޝ': 39, 'ޞ': 40,
    'ޟ': 41, 'ޠ': 42, 'ޡ': 43, 'ޢ': 44, 'ޣ': 45,
    'ޤ': 46, 'ޥ': 47, 'ަ': 48, 'ާ': 49, 'ި': 50,
    'ީ': 51, 'ު': 52, 'ޫ': 53, 'ެ': 54, 'ޭ': 55,
    'ޮ': 56, 'ޯ': 57, 'ް': 58, 'ޱ': 59, '/': 0
}


class TextPipeline:

    def __init__(self) -> None:
        super().__init__()
        self.splitter = re.compile("[.\n]")

    @staticmethod
    def tokenize(inp: str):
        """
        Tokenize input string for model input
        :param inp: String for inference
        :return: 1d array of int32 tokens
        """
        return [(token_mapping[x] if x in token_mapping.keys() else token_mapping[' ']) for x in inp]

    def split(self, text):
        return self.splitter.split(text)

    def __call__(self, text: str, sent_breath=2, para_breath=3):
        return self.tokenize(text)


class TTSModel:

    def __init__(self, model_path: str, vocoder_path: str):
        self.model = tf.saved_model.load(model_path)
        self.vocoder = tf.saved_model.load(vocoder_path)
        self.text_pipeline = TextPipeline()
        self.MAX_WAV_VALUE = 32768

    def __call__(self, text: str, speed: int = 1.0):

        out = np.array([])
        for tx in self.text_pipeline.split(text):
            inp = self.text_pipeline(tx)

            if not tx:
                continue
            elif tx.isspace():
                # todo: pad silence here maybe?
                continue
            else:
                tts_out = self.model.predict_mel(inp, speed)
                tts_out = tts_out[np.newaxis, :, :]

                vocoder_out = self.vocoder(input=tts_out)[0]
                vocoder_out = vocoder_out.numpy().squeeze()
                vocoder_out *= self.MAX_WAV_VALUE

                out = np.concatenate((out, vocoder_out))

        return out
