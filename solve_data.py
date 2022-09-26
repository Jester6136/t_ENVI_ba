import json


viet_text = []
lao_text = []
with open('data/train.json', 'r', encoding='utf-8') as f:
    for line in f:
        line = json.loads(line)
        print(line['vi'])
        break
    