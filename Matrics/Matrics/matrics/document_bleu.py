import sacrebleu
from sacremoses import MosesDetokenizer
md = MosesDetokenizer(lang='en')


# Open the test dataset human translation file and detokenize the references
refs = ['I must apologise']


    
print("Reference 1st sentence:", refs[0])

refs = [refs]  # Yes, it is a list of list(s) as required by sacreBLEU


# Open the translation file by the NMT model and detokenize the predictions
preds = ['I must apologise']


print("MTed 1st sentence:", preds[0])    
# Calculate and print the BLEU score
bleu = sacrebleu.corpus_bleu(preds, refs, lowercase = True)
print(bleu) 