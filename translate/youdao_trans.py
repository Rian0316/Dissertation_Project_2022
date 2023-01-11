import json
import requests
import requests
import time
import hashlib
import uuid


def translate(word):
    # 有道词典 api
    url = 'https://openapi.youdao.com/api'
    
    time_curtime = int(time.time())   # 秒级时间戳获取
    app_id = "19a64f75def1acd0"   # 应用id
    uu_id = uuid.uuid4()   # 随机生成的uuid数，为了每次都生成一个不重复的数。
    app_key = "Lppw4T69MzGY1H5JfDvYWi0Eh7hG7Xnj"   # 应用密钥

    # 翻译文本生成sign前进行的处理
    input_text = ""

    # 当文本长度小于等于20时，取文本
    if(len(word) <= 20):
        input_text = word
    
    # 当文本长度大于20时，进行特殊处理
    elif(len(word) > 20):
        input_text = word[:10] + str(len(word)) + word[-10:]

    sign = hashlib.sha256((app_id + input_text + str(uu_id) + str(time_curtime) + app_key).encode('utf-8')).hexdigest()   # sign生成

    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'q':word,   # 翻译文本
        'from':"zh-CHS",   # 源语言
        'to':"en",   # 翻译语言
        'appKey':app_id,   # 应用id
        'salt':uu_id,   # 随机生产的uuid码
        'sign':sign,   # 签名
        'signType':"v3",   # 签名类型，固定值
        'curtime':time_curtime,   # 秒级时间戳
    }
    r = requests.get(url, params = key).json() 
    return r["translation"][0]

new_lines = [] 

if __name__ == '__main__':
    with open('CHI_US.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
        for line in lines: 
            if line != '':
                tgt = translate(line)
                new_lines.append(tgt)
                print(line) # 输入的数据：'开玩笑啦'
                print(tgt) # 翻译的结果：A joke!
            else:
                tgt = line
                new_lines.append(tgt)
                print(line) # 输入的数据：'开玩笑啦'
                print(tgt) # 翻译的结果：A joke!
    
    with open('youdao.txt', 'w') as f: 
        f.write("\n".join(new_lines))  
