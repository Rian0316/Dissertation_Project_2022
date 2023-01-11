import requests 
 
auth_key = "0c410bd1-4e2a-9bb2-1d6f-9859efab7ce5:fx" 
target_language = "EN-US"  ## EN-US
 
#path = "opensubs/506445" # 文件夹名称末尾得有 / 
source_filename = "chi.txt" # 上一步生成的文件，成为这一步的 “源文件” 
target_filename = "deepl_US.txt" 
 
def translate(text): 
    result = requests.get(  
       "https://api-free.deepl.com/v2/translate", 
       params={  
         "auth_key": auth_key, 
         "target_lang": target_language, 
         "text": text, 
       }, 
    )  
    return result.json()["translations"][0]["text"] 

with open(source_filename, 'r', encoding='utf-8') as f:
   lines = [line.strip() for line in f]

new_lines = [] 
 
for line in lines: 
    line_translated = translate(line) 
    new_lines.append(line_translated)     
    print(line_translated) 

with open(target_filename, 'w') as f: 
    f.write("\n".join(new_lines))  
