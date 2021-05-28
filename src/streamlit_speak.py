import streamlit as st
import argparse
from tts import TTSModel
import os
import soundfile as sf


parser = argparse.ArgumentParser()
parser.add_argument("--model", "-m", type=str, help="Path to downloaded models")
args = parser.parse_args()


@st.cache
def get_model():
    model_path = args.model
    tts = TTSModel(
        os.path.join(model_path, "tts.saved_model"),
        os.path.join(model_path, "vocoder.saved_model")
    )

    return tts


speed = st.sidebar.slider("Speed", 0.5, 2.0, 1.0, step=0.05)
text = st.text_area("Input text", height=420)

if st.button("Syntehsize"):
    st.subheader("Generated output")
    if text:
        wav = get_model()(text, speed=speed).astype("int16")
        sf.write("temp.wav", data=wav, samplerate=22050)
        st.audio("temp.wav", format="audio/wav")
        os.remove("temp.wav")
    else:
        st.text("You must provide input text to syntehsize")


