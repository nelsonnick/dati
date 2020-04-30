import json


with open("id.json", 'r', encoding='utf-8') as file:
    ids = json.load(file)['data']
    for a in ids:
        id = a['id']
        content = a['content']\
            .replace("&nbsp;", "")\
            .replace("(", "")\
            .replace(")", "")\
            .replace("（", "")\
            .replace("）", "")\
            .replace("\n", "")\
            .replace(" ", "")\
            .replace("[", "")\
            .replace("]", "")\
            .replace("〔", "")\
            .replace("〕", "")\
            .replace("。", "")\
            .replace("，", "")\
            .replace("《", "")\
            .replace("》", "")\
            .replace("、", "")\
            .replace("%", "")\
            .replace("：", "")\
            .replace("“", "")\
            .replace("”", "")\
            .replace("〈", "")\
            .replace("〉", "")\
            .replace("？", "")\
            .replace("<", "")\
            .replace(">", "")\
            .replace("*", "")\
            .replace("=", "")\
            .replace("-", "")\
            .replace("+", "")\
            .replace(".", "")\
            .replace("-", "")\
            .replace("_", "")\
            .replace("&amp;", "").replace("2526lt;", "").replace("/p", "").replace("2526gt;", "").replace("/span", "").replace("span", "")\
            .replace(";", "").replace(",", "").replace("；", "")

        o = id +'\t' + content
        print(o)