# Read corpus.align
# For each sxey/language, create a list (epID, overlap)
# Sort these lists, pick the best candidate
# From the list of best candidates, put all the files in one directory along with alignment files. get rid of ID etc


# Goal:
# - to clear up the data/ directory by removing subs with low overlap

import re
from socket import inet_aton

final_paths = []
prev_show = '11600242'
prev_lang = 'chi'
prev_overlap = 0
leader = ''
with open('corpus.align', 'r') as c:
    lines = c.readlines()
    for line in lines:
        if line.startswith('.'):
            dir, path, overlap = line.split(':')
            overlap = overlap.strip("overlap =")
            try:
                overlap = float(overlap)
            except:
                overlap = 0
            show, lang = re.split('/|_', path)[2:4]
            if (prev_show, prev_lang) == (show, lang):
                if overlap > prev_overlap:
                    # This file is better
                    prev_overlap = overlap
                    leader = path
            else:
                print("The leader is {} with overlap {}.".format(leader, prev_overlap))
                final_paths.append(leader)
                # Getting rid of associated files as well
                final_paths.append("{}srt".format(leader[:-4]))
                final_paths.append("{}xml.align".format(leader[:-4]))
                prev_show, prev_lang, prev_overlap = show, lang, overlap
                leader = path

# Append the last entry too
print("The leader is {} with overlap {}.".format(leader, prev_overlap))
final_paths.append(leader)
final_paths.append("{}srt".format(leader[:-4]))
final_paths.append("{}xml.align".format(leader[:-4]))
with open('sub.paths', 'w+') as write_file:
    for line in final_paths:
        write_file.write("{}\n".format(line))


            