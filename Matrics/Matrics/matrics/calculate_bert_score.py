"""
Created on Thu Mar 17 18:21:12 2022

@author: RIAN
"""

# demo:https://github.com/Tiiiger/bert_score/blob/master/example/Demo.ipynb
# pip install bert_score

from bert_score import score

with open("EN_DATA.txt") as f:
    refs = [line.strip() for line in f]


with open("youdao.txt") as f:  
    cands = [line.strip() for line in f]

print(cands[0])


P, R, F1 = score(cands, refs, lang='en', verbose=True)
print(str(F1) + "\n")
print(str(F1.mean()) + "\n")