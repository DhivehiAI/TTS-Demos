import argparse
from tts import TTSModel
import os
from functools import partial

import soundfile as sf


def main(text, model, output, speed):
    print("Loading Models...")
    model_path = partial(os.path.join, model)
    tts = TTSModel(model_path("tts.saved_model"), model_path("vocoder.saved_model"))

    print("Generating Audio...")
    output_wav = tts(text, speed=speed)

    print(f"Writing Output file.. ")
    sf.write(output, output_wav.astype("int16"), 22050, "PCM_16")

    print("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="The text to speak out")
    parser.add_argument("--model", "-m", type=str, help="Path to downloaded models")
    parser.add_argument("--output", "-o", type=str, help="Output audio path")
    parser.add_argument("--speed", "-s", default=0.95, type=float, help="Readout speed")
    main(**vars(parser.parse_args()))