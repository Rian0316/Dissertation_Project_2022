# for each language, dictionary has IMDB ids as keys, and the values are (best_eng_file,overlap)
import os
entries = {}

with open('corpus.align_test', 'r') as f:
    while True:
        line1 = f.readline()
        if line1.startswith('Aligning'):
            line2 = f.readline()
            line3 = f.readline()
            if line2.startswith('overlap') and line3.startswith('ratio'):
                line1 = line1.split()
                eng_file, trg_file = line1[1], line1[3]
                overlap = line2.split()[2]
                trg_lang = trg_file.split('/')[8]
                imdb_id = eng_file.split('/')[7]
                if trg_lang not in entries.keys():
                    entries[trg_lang] = {}
                if imdb_id in entries[trg_lang].keys():
                    _, _, previous_overlap = entries[trg_lang][imdb_id]
                    if previous_overlap < overlap:
                        entries[trg_lang][imdb_id] = (eng_file, trg_file, overlap)
                else:
                    entries[trg_lang][imdb_id] = (eng_file, trg_file, overlap)
        if not line1:
            break

with open('align.output', 'w+') as f:
    for lang in entries:
        for id in entries[lang]:
            eng_name = os.path.basename(entries[lang][id][0])
            trg_name = os.path.basename(entries[lang][id][1])
            filename = f'{eng_name}-{trg_name}.align'
            root = '/data/seb/datasets/ccd_data/data/alignments'
            align_path = os.path.join(root, filename)
            f.write(f'{align_path}\n')
