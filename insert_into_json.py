import sys
import json
import re
import pprint as pp


def insert_txt(json_filename, txt_filename, out_filename):
    with open(json_filename, 'r') as read_file:
        json_data = json.load(read_file)
        with open(txt_filename, 'r') as read_file_2:
            txt_data = read_file_2.readlines()
            for i in range(len(txt_data)):
                print(txt_data[i])
                # Remove - in front
                json_data["speech_segments"][i]["text"] = re.sub(r'^\s*-\s*', '', txt_data[i]).strip()
                json_data["speech_segments"][i].pop("text2")
    with open(out_filename, 'w+', encoding='utf8') as write_file:
        # json.dump(json_data, write_file, indent=2)
        json.dump(json_data, write_file, indent=2, ensure_ascii=False)


def add_ids(json_filename):
    """

    :param json_filename: name of file to insert ids in
    :return: none
    """
    with open(json_filename, 'r') as read_file:
        json_data = json.load(read_file)
        if "id" in json_data["speech_segments"][0].keys():
            print("IDs already inserted.")
            return
        for i in range(len(json_data["speech_segments"])):
            json_data["speech_segments"][i]["id"] = i + 1
    with open(json_filename, 'w+', encoding='utf8') as write_file:
        # json.dump(json_data, write_file, indent=2)
        json.dump(json_data, write_file, indent=2, ensure_ascii=False)


def split_scenes(json_filename, scenes):
    with open(json_filename, 'r') as read_file:
        json_data = json.load(read_file)
        with open(scene_file, 'r') as read_scene_file:
            scene_data = json.load(read_scene_file)[json_filename.split('/')[-1][:-8]]
        json_data["scenes"] = []
        for start, end in scene_data:
            json_data["scenes"].append([json_data["speech_segments"][i] for i in range(start - 1, end)])
        json_data.pop("speech_segments")
    with open(json_filename, 'w+', encoding='utf8') as write_file:
        json.dump(json_data, write_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    json_filename = sys.argv[1]
    # scene_file = sys.argv[2]
    txt_filename = sys.argv[2]
    # out_filename = sys.argv[3]

    insert_txt(json_filename, txt_filename, json_filename)
    # add_ids(json_filename)
    # split_scenes(json_filename, scene_file)
