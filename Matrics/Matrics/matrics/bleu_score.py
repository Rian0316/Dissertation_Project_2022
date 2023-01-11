"""
Created on Thu Mar 17 18:21:12 2022

@author: RIAN
"""

import sacrebleu
from sacremoses import MosesDetokenizer
md = MosesDetokenizer(lang='en')

refs = []

with open("eng_sub.txt") as test:
    for line in test: 
        line = line.lower().split()
        line = md.detokenize(line) 
        refs.append(line.strip('.'))

# Open the translation file by the NMT model and detokenize the predictions
preds = []

with open("google_sub.txt") as pred:  
    for line in pred: 
        line = line.strip().lower().split()
        line = md.detokenize(line) 
        preds.append(line)  

# Calculate BLEU for sentence by sentence and save the result to a file
with open("google_bleu.txt", "w+") as output:
    for line in zip(refs,preds):
        test = line[0]
        pred = line[1]
        print(test)
        print(pred)
        bleu = sacrebleu.sentence_bleu(pred, [test], smooth_method='exp')
        print(bleu, "\n")
        output.write(str(test) + "\n")
        output.write(str(pred) + "\n")
        output.write(str(bleu.score) + "\n")
