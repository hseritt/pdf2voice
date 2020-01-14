#!/usr/bin/env python

# Python 3.8.1

import sys

import pdftotext
from gtts import gTTS

LANG = 'en'
SLOW = False

try:
    pdf_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    pdf_file = 'sample.pdf'
    output_file = 'sample.mp3'


class PdfToVoice:
    def get_text(self):
        with open(pdf_file, 'rb') as f:
            pdf = pdftotext.PDF(f)
        text_str = ''
        for text in pdf:
            text_str += text
        return text_str

    def write_to_audio(self, text_str):
        gTTS(
            text=text_str, lang=LANG, slow=SLOW
        ).save(output_file)

    def run(self):
        self.write_to_audio(self.get_text())


if __name__ == '__main__':
    app = PdfToVoice()
    app.run()
