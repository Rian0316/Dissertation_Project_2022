with open("uk_data.txt", 'r', encoding='UTF-8') as f:
    refs = [line.strip() for line in f]
  
lines = []
for text in refs :
    lines.append(text.strip('.')) 
    
with open("google.txt", "w+", encoding='utf-8') as output:
    for line in lines:
        # print(text.translatedText)
        output.write(str(line) + "\n")
