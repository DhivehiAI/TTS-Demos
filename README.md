## Dhivehi TTS Demo

This repository contains demo code to work with the Dhivehi.ai pretrained tts.
For documented usage, check out the notebooks.

Limitations:
* Requires additional phonemization for numbers, dates etc
* Model is not optimized against retracting

## Setup
 * Install dependencies `pip install -r requirements.txt`
 * Download pre-trained models (see below) in an appropriate path.  
   ex: `gdown --id <file_id>`


## Usage

### Command Line Interface
```commandline
usage: dv_speak.py [-h] [--model MODEL] [--output OUTPUT] [--speed SPEED] text

positional arguments:
  text                  The text to speak out

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL, -m MODEL
                        Path to downloaded models
  --output OUTPUT, -o OUTPUT
                        Output audio path
  --speed SPEED, -s SPEED
                        Readout speed
```

**Sample Usage**:  
`python3 dv_speak.py --model path_to_models --output out.wav --speed 0.9 "ހެލޯ ދިވެހި"`


### Streamlit Service
We provide a basic streamlit script to run inference as well.
The script `streamlit_speak.py` can be run like:

`streamlit run streamlit_speak.py -- -m path_to_model`

## Pretrained Models

Currently we provide the following pre-trained models

|Name|Type|file_id|model
|----|----|-------|-----|
|DV Male v1|TTS|1KXAl8823lemgovmwYzU43U5JyXx-BG6p|TransformerTTS|
|DV Female v1|TTS|1T0RyRKizHMY8r9ZS5Z_fy45TBSXAlNH5|TransformerTTS|