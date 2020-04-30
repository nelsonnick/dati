import json


def trimA(ss):
    return ss.replace(" ", "")\
        .replace("、", "")\
        .replace("（", "")\
        .replace("）", "")\
        .replace("(", "")\
        .replace(")", "")\
        .replace("。", "")\
        .replace("A", "")\
        .replace("B", "")\
        .replace("C", "")\
        .replace("D", "")\
        .replace("E", "")\
        .replace("F", "")\
        .replace("，", "")\
        .replace(",", "")\
        .replace("：", "")\
        .replace(":", "")\
        .replace("．", "")\
        .replace("；", "")\
        .replace("%", "")\
        .replace("％", "")\
        .replace("`", "")\
        .replace("《", "")\
        .replace("》", "") \
        .replace("\\n", "") \
        .replace("/", "") \
        .replace("\\", "").replace("&amp;", "").replace("2526lt;", "").replace("2526gt;", "").replace("span", "").replace("&nbsp;", "").replace("br", "").replace("p", "")


def trimB(ss):
    return ss.replace("A．", "")\
        .replace("B．", "")\
        .replace("C．", "")\
        .replace("D．", "")\
        .replace("E．", "")\
        .replace("F．", "")

with open("questions.json", 'r', encoding='utf-8') as file:
    questions = json.load(file)

with open("guo.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    danxuan = data["data"]["questionTypeSummaries"][0]["questions"]
    duoxuan = data["data"]["questionTypeSummaries"][1]["questions"]
    panduan = data["data"]["questionTypeSummaries"][2]["questions"]
    tiankong = data["data"]["questionTypeSummaries"][3]["questions"]

print("单选题")
list1 = 1
for a in danxuan:
    if a["content"][-1] == "\n":
        b = a["content"][0: -1]
    else:
        b = a["content"]
    p = b.split("\n")
    for all in questions:
        if all["type"] == "single_topic_selection":
            if trimA(p[len(p)-1]) == trimA(all["question"]):
                print(str(list1) + ":" + all["answer"])
    list1 = list1 + 1

print("多选题")
for a in duoxuan:
    if a["content"][-1] == "\n":
        b = a["content"][0: -1]
    else:
        b = a["content"]
    p = b.split("\n")
    for all in questions:
        if all["type"] == "multiple_choice":
            if trimA(p[len(p)-1]) == trimA(all["question"]):
                print(str(list1) + ":" + all["answer"])
    list1 = list1 + 1

print("判断题")
for a in panduan:
    if a["content"][-1] == "\n":
        b = a["content"][0: -1]
    else:
        b = a["content"]
    p = b.split("\n")
    for all in questions:
        if all["type"] == "true_or_false":
            if trimA(p[len(p) - 1]) == trimA(all["question"]):
                print(str(list1) + ":" + all["answer"])
    list1 = list1 + 1

print("填空题")
for a in tiankong:
    for all in questions:
        if all["type"] == "gap_filling":
            if trimA(a["content"]) == trimA(all["question"]):
                print(str(list1) + ":" + all["answer"])
    list1 = list1 + 1
