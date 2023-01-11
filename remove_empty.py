"""
1. Open the source file, save lines to list
2. Open the target file, save lines to list
3. List comprehension over target file to remove lines if not in source file
4. Save to new files
"""

import os
import re


def remove_empty(lang):
    src = open('../Bleualign/test_output/{}-s'.format(lang), 'r')
    src_lines = src.readlines()
    src.close()
    trg = open('../Bleualign/test_output/{}-t'.format(lang), 'r')
    trg_lines = trg.readlines()
    trg.close()
    trg_lines = [trg_lines[x] for x in range(len(trg_lines)) if src_lines[x] != '\n']
    src_lines = [src_lines[x] for x in range(len(src_lines)) if src_lines[x] != '\n']
    with open('../Bleualign/test_output/{}-t-filtered'.format(lang), 'w+') as out_file:
        out_file.writelines(trg_lines)
    with open('../Bleualign/test_output/{}-s-filtered'.format(lang), 'w+') as out_file:
        out_file.writelines(src_lines)


# def preprocess_target(file):


# preprocess_target('../Bleualign/test_output/Original_files_test/S01E11_nan_2963.pol')
# trg = open('../Bleualign/test_output/Original_files_test/S01E11_nan_2953.fre', 'r')
# txt = trg.read()
# txt = re.sub(r'([?|\.|\!|\/])[^\S\r\n]+([-|\w]+)', '\g<1>\n\g<2>', txt)
# with open('../Bleualign/test_output/Original_files_test/S01E11_nan_2953.fre.prep', 'w+') as f:
#     f.write(txt)

remove_empty('french_bign')
