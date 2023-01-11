"""
Adapted from os_cxt_extractor/extract_subs.py
Read xml files and .align file and extract subtitles to a .txt file
"""
import xml.etree.ElementTree as ET
import os
import math
import sys
import re


def time_converter(time_str):
    time_str = time_str.replace(',', ':').replace('.', ':').replace(' ', '')
    time_str = re.split(r'[^0-9]', time_str)
    # Bugproofing
    if len(time_str) < 4:
        time_str.append('000')
    try:
        hours, mins, secs, msecs = list(time_str)
    except:
        print("Can't unpack values correctly")
        hours, mins, secs, msecs = ['00','00', '00', '00']
    msecs = int(msecs) + int(hours) * 3600000 + int(mins) * 60000 + int(secs) * 1000

    return msecs


def parse_subtitles(tree_root):
    """
    Extract subtitles from xml files as text
    :param tree_root: root of the xml tree
    :return: subtitles : a dictionary where key is subtitle ID and value is text and timestamps
    """
    time_start = -1
    sub_count = 0
    group_buffer = []
    # Making a nan array to store subs
    subtitles = dict()
    for sub in tree_root:
        if sub.tag == 's':
            # Check for time start
            if sub[0].tag == 'time':
                time_start = time_converter(sub[0].attrib['value'])
                sub_count = 1
            else:
                sub_count += 1
            if sub[-1].tag == 'time':
                time_end = time_converter(sub[-1].attrib['value'])
            else:
                time_end = -1
            # Collecting subtitles
            single_buffer = ""
            for element in sub:
                if element.tag == 'w':
                    single_buffer = single_buffer + ' ' + element.text
            group_buffer.append((single_buffer, sub.attrib['id']))
            # Subtitles collected. Flush with time stamps if done
            if time_end != -1:
                duration = time_end - time_start
                fragment = math.floor(duration / sub_count)
                # Assigning time fragments to subs
                stamp = time_start
                for single_sub, sub_id in group_buffer:
                    subtitles[sub_id] = (single_sub, stamp, stamp + fragment - 80)
                    stamp = stamp + fragment + 80
                group_buffer = []
    # Bugproofing: if last sub is not closed
    if group_buffer:
        time_end = time_start + 1000
        duration = time_end - time_start
        fragment = math.floor(duration / sub_count)
        for single_sub, sub_id in group_buffer:
            subtitles[sub_id] = (single_sub, stamp, stamp + fragment - 80)
            stamp = stamp + fragment + 80
        group_buffer = []
    return subtitles

def parse_documents(alignment_filename):
    """
    Given a file with alignments of subtitles between source and target language, produce subtitles in .txt
    :param alignment_filename: file which contains alignment of subtitles and paths to them
    :return:
    """

    """
    Part 1: Parse alignments
    """
    align_tree = ET.parse(alignment_filename)
    root = align_tree.getroot()
    linkGrp = root[0]

    # Determining paths for input
    # ./opensubs/86661/eng/1954587469.xml
    src_path = linkGrp.attrib['fromDoc']
    src_file = open(src_path, 'r')
    # ./opensubs/86661/chi/1954545954.xml
    tgt_path = linkGrp.attrib['toDoc']
    tgt_file = open(tgt_path, 'r')

    # Determining paths for output
    #basename = os.path.basename(tgt_path).split('.')[0]
    output_root = 'corpus_clean'
    # chi
    tgt_language = tgt_path.split('/')[3] 
    # 86661
    imdb_id = tgt_path.split('/')[2] 
    # corpus.clean/86661/chi/src
    src_out_path = os.path.join(output_root, imdb_id, tgt_language)
    # corpus.clean/86661/chi/src
    tgt_out_path = os.path.join(output_root, imdb_id, tgt_language)

    # Parsing alignments
    pairs_to_parse = []
    for align in linkGrp:
        # eng id, chi id
        src_ids, tgt_ids = align.attrib['xtargets'].split(';')
        src_ids, tgt_ids = src_ids.split(), tgt_ids.split()
        pairs_to_parse.append((src_ids, tgt_ids))

    """
    Parse subtitles from subtitle files
    """
    # Parse source text
    try:
        src_tree = ET.parse(src_file)
    except:
        print("Error when parsing source file")
        pass
    src_root = src_tree.getroot()
    src_subtitles = parse_subtitles(src_root)

    # Parse target text
    try:
        tgt_tree = ET.parse(tgt_file)
    except:
        print("Error when parsing target file")
        pass
    tgt_root = tgt_tree.getroot()
    tgt_subtitles = parse_subtitles(tgt_root)
    for pair in pairs_to_parse:
        src_ids, tgt_ids = pair
        write_to_file(os.path.join(os.getcwd(), src_out_path), src_subtitles, src_ids)
        write_to_file(os.path.join(os.getcwd(), tgt_out_path), tgt_subtitles, tgt_ids)

def write_to_file(filename, subs, indices):
    """

    :param filename: name of file to write to
    :param subs: dictionary containing subtitles
    :param indices: a list of idcs (str) to access subtitles from subs
    :return:
    """
    # filename = os.makedirs(filename.strip()+'/')
    with open(filename+'/'+'opensubs.txt', 'a+') as f:
        buffer = ''
        for index in indices:
                buffer = buffer + subs[index][0].encode('utf-8')
        f.write(buffer + '\n')
    return
    

if __name__ == '__main__':
    # ./opensubs/86661/chi/1954545954.xml.align
    filename = sys.argv[1]
    parse_documents(filename)