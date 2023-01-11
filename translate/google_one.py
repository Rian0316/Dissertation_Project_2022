# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:18:26 2022

@author: Rian
"""

from pygtrans import Translate, Null

with open("CHI_US.txt", 'r', encoding='utf-8') as f:
    refs = [line.strip() for line in f]
        
client = Translate()
text = client.translate(refs,target='en')


with open("google.txt", "w+", encoding='utf-8') as output:
    for text in text:
        print(text.translatedText[0])
        output.write(str(text.translatedText[0]) + "\n")
