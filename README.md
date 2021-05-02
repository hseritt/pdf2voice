# Pdf2Voice

## Installation and Setup

I set this up using:

- Ubuntu 18.04
- Python 3.8.1

Installed these packages:

### Ubuntu:

```
# sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python-dev libevent-dev
```

### Python:

*For best results, use pyenv to set up your environment.*

```
# pip install pdftotext gTTS
```


### Running the pdf2voice.py script

Running the pdf2voice.py script:

```
# ./pydf2voice.py [sample.pdf sample.mp3]
```

sample.pdf is the input PDF file that gets processed to text.
sample.mp3 is the output mp3 file that has the resulting audio.

If you don't include the arguments (per the example, sample.pdf and sample.mp3), the default input expects a pdf file called sample.pdf and will output an mp3 file called sample.mp3.

### Options

In the script there are 2 options that can be changed:

LANG is set to 'en'. For example, if you want the audio to be in French, you can use 'fr'.

SLOW is set to False. If you set this to true, the audio will play back slower.

### Related Links

Inspired from this article:

https://dev.to/mustafaanaskh99/convert-any-pdf-file-into-an-audio-book-with-python-1gk4
