#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

f1 = ['001001单选', '001002多选', '001003判断', '001004填空']
# f1 = ['001001单选', '001002多选', '001003判断', '001004填空', '001005简答', '001006案例']
f2 = ['6238就业创业.json', '6239劳动关系.json', '6240十九大.json', '6242人事人才.json', '6243综合服务.json', '6244社会保险.json']

file = open("questions.json", "w+", encoding="utf-8")
for a in f1:
    for b in f2:
        with open(a + "/" + b, 'r', encoding="utf-8", errors="ignore") as load_f:
            data = json.load(load_f)['data']
            for d in data:
                q = {'id': d['id'], 'answer': d['answer']}
                data_json = json.dumps(q, ensure_ascii=False)
                file.write(data_json)
                file.write(',\n')
file.close()

file1 = open("questions1.json", "w+", encoding="utf-8")
for b in f2:
    with open("001001单选/" + b, 'r', encoding="utf-8", errors="ignore") as load_f:
        data = json.load(load_f)['data']
        for d in data:
            q = {'id': d['id'], 'answer': d['answer']}
            data_json = json.dumps(q, ensure_ascii=False)
            file1.write(data_json)
            file1.write(',\n')
file1.close()

file2 = open("questions2.json", "w+", encoding="utf-8")
for b in f2:
    with open("001002多选/" + b, 'r', encoding="utf-8", errors="ignore") as load_f:
        data = json.load(load_f)['data']
        for d in data:
            q = {'id': d['id'], 'answer': d['answer']}
            data_json = json.dumps(q, ensure_ascii=False)
            file2.write(data_json)
            file2.write(',\n')
file2.close()

file3 = open("questions3.json", "w+", encoding="utf-8")
for b in f2:
    with open("001003判断/" + b, 'r', encoding="utf-8", errors="ignore") as load_f:
        data = json.load(load_f)['data']
        for d in data:
            q = {'id': d['id'], 'answer': d['answer']}
            data_json = json.dumps(q, ensure_ascii=False)
            file3.write(data_json)
            file3.write(',\n')
file3.close()

file4 = open("questions4.json", "w+", encoding="utf-8")
for b in f2:
    with open("001004填空/" + b, 'r', encoding="utf-8", errors="ignore") as load_f:
        data = json.load(load_f)['data']
        for d in data:
            q = {'id': d['id'], 'answer': d['answer']}
            data_json = json.dumps(q, ensure_ascii=False)
            file4.write(data_json)
            file4.write(',\n')
file4.close()




# 需要再手动改一下questions.json，使之成为json数组。