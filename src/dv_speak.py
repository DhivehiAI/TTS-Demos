import argparse
from tts import TTSModel
import os
import soundfile as sf

parser = argparse.ArgumentParser()
parser.add_argument("text", help="The text to speak out")
parser.add_argument("--model", "-m", type=str, help="Path to downloaded models")
parser.add_argument("--output", "-o", type=str, help="Output audio path")
parser.add_argument("--speed", "-s", default=0.95, type=float, help="Readout speed")

args = parser.parse_args()

print("Loading Models...")
model_path = args.model
tts = TTSModel(
    os.path.join(model_path, "tts.saved_model"),
    os.path.join(model_path, "vocoder.saved_model")
)

print("Generating Audio...")
output_wav = tts(args.text, speed=args.speed)

print(f"Writing Output file.. ")
sf.write(args.output, output_wav.astype('int16'), 22050, 'PCM_16')

print("Done!")

