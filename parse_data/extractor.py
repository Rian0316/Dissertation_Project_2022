"""
A parser to extract subtitles from export.
Fields of interest: MovieImdbID, IDSubtitleFile, SubLanguageID
Desired path: MovieImdbID/SubLanguageID/IDSubtitleFile
"""
import numpy as np
import pandas as pd
import os
import sys
import gzip


df = pd.read_csv('opensubs/export.txt', sep='\t', skiprows=2)
df = df[['MovieImdbID', 'IDSubtitleFile', 'SubLanguageID']]

for index, row in df.iterrows():
    ID = str(row['IDSubtitleFile'])
    path = "{}/{}/{}/{}/{}".format(ID[-1], ID[-2], ID[-3], ID[-4], ID)
    f = gzip.open(path + '.gz', 'rb')
    file_content = f.read()
    # New path: imdbID/lang/IDsubfile
    filename = f"{ID}.srt"
    dir_path = os.path.join('opensubs', str(row['MovieImdbID']), str(row['SubLanguageID']))
    try:
        os.makedirs(dir_path)
    except FileExistsError:
    	pass
    path = os.path.join(dir_path, filename)
    with open(path, 'wb+') as f:
        f.write(file_content)
    # print(file_content)
    print(path)
    f.close()
