"""
Created on Wed Mar 30 23:23:09 2022

@author: Rian
"""

with open("google.txt", 'r', encoding='UTF-8') as f:
    refs = [line.strip() for line in f]
    
encode_json = {
            '\\u003C': '<',
            '\\u003E': '>',
            '\\u002F': '/',
            '&#x3D;\\':'=',
            '&quot;':"'",
            '\\':'',
            '\/':'/',
            '&#39;': " '"
        }
lines = []
for text in refs :
    for key in encode_json.keys():
        text = text.replace(key, encode_json[key])
    lines.append(text) 

with open("google.txt", "w+", encoding='utf-8') as output:
    for line in lines:
        # print(text.translatedText)
        output.write(str(line) + "\n")
