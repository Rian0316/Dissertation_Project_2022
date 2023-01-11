import matplotlib.pyplot as plt
from matplotlib import rcParams
from bert_score import score
import matplotlib.pyplot as plt
import logging
import transformers
from bert_score import plot_example

from bert_score import BERTScorer



transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)


rcParams["xtick.major.size"] = 0
rcParams["xtick.minor.size"] = 0
rcParams["ytick.major.size"] = 0
rcParams["ytick.minor.size"] = 0

rcParams["axes.labelsize"] = "large"
rcParams["axes.axisbelow"] = True
rcParams["axes.grid"] = True


with open("hyp.txt") as f:
        cands = [line.strip() for line in f]

with open("ref.txt") as f:
        refs = [line.strip() for line in f]

cands[0]

P, R, F1 = score(cands, refs, lang='en', rescale_with_baseline=True)

F1
mean = F1.mean()
print(f"System level F1 score: {F1}")

#plt.hist(F1, bins=20)
#plt.xlabel("score")
#plt.ylabel("counts")
#plt.show()
plot_example(cands[0], refs[0], lang="en", rescale_with_baseline=True)

