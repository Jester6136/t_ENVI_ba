import os
import pandas as pd
from sklearn.model_selection import train_test_split

count = 0
path = "data"
train_en_txt = []
# for folder_text in os.listdir(path):
folder_text = 'en_text'
for stack in os.listdir(os.path.join(path,folder_text)):
    with open(os.path.join(path,folder_text,stack),mode='r',encoding='utf8') as f:
        for line in f:
            train_en_txt.append(line.strip())
            count +=1
            if count == 100: break
train_vi_txt = []
count = 0
# for folder_text in os.listdir(path):
folder_text = 'vi_text'
for stack in os.listdir(os.path.join(path,folder_text)):
    with open(os.path.join(path,folder_text,stack),mode='r',encoding='utf8') as f:
        for line in f:
            train_vi_txt.append(line.strip())
            count +=1
            if count == 100: break

en_text = []
vi_text = []

count = 0
for index in range(len(train_vi_txt)):
    if len(train_vi_txt[index]) <256 and len(train_en_txt[index]) <256:
        en_text.append(train_en_txt[index])
        vi_text.append(train_vi_txt[index])
        count +=1
    
print(count)
            
data = {"vi":[line for line in vi_text],"en":[line for line in en_text]}

df = pd.DataFrame(data,columns=['vi','en'])
train,val = train_test_split(df, test_size=0.1, random_state=1)

with open('data_1/train.json', 'w', encoding='utf-8') as file:
    train.to_json(file, force_ascii=False,orient='records',lines=True)
with open('data_1/val.json', 'w', encoding='utf-8') as file:
    val.to_json(file, force_ascii=False,orient='records',lines=True)
    
# testtttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
# testtttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
# testtttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
# testtttttttttttttttttttttttttttttttttttttttttttttttttttttttttt
count =0
test_en_txt = []
# for folder_text in os.listdir(path):
folder_text = 'test_en'
for stack in os.listdir(os.path.join(path,folder_text)):
    with open(os.path.join(path,folder_text,stack),mode='r',encoding='utf8') as f:
        for line in f:
            test_en_txt.append(line.strip())
            count +=1
            if count == 100: break
            
test_vi_txt = []
count = 0
# for folder_text in os.listdir(path):
folder_text = 'test_vi'
for stack in os.listdir(os.path.join(path,folder_text)):
    with open(os.path.join(path,folder_text,stack),mode='r',encoding='utf8') as f:
        for line in f:
            test_vi_txt.append(line.strip())
            count +=1
            if count == 100: break

test_en = []
test_vi = []

count = 0
for index in range(len(test_vi_txt)):
    if len(test_vi_txt[index]) <256 and len(test_en_txt[index]) <256:
        test_en.append(test_en_txt[index])
        test_vi.append(test_vi_txt[index])
        count +=1
    
print(count)

test = {"vi":[line for line in test_vi],"en":[line for line in test_en]}

df = pd.DataFrame(test,columns=['vi','en'])

with open('data_1/test.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False,orient='records',lines=True)
print('getdata raw successfully')