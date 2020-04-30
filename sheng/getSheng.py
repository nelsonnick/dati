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
        .replace("：", "")\
        .replace(":", "")\
        .replace("．", "")\
        .replace("；", "")\
        .replace("%", "")\
        .replace("％", "")\
        .replace("`", "")\
        .replace("《", "")\
        .replace("》", "")\
        .replace("\\", "")


def trimB(ss):
    return ss.replace("A．", "")\
        .replace("B．", "")\
        .replace("C．", "")\
        .replace("D．", "")\
        .replace("E．", "")\
        .replace("F．", "")

with open("q.json", 'r', encoding='utf-8') as file:
    questions = json.load(file)

with open("sheng.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    sheng = data["data"]["Questions"]


for s in sheng:
    for all in questions:
        if trimA(s["Question"]) == trimA(all["q"]):
            answer = ""
            an = ""
            if all["t"] == "a":
                if all["a"] == "A":
                    an = all["oA"]
                if all["a"] == "B":
                    an = all["oB"]
                if all["a"] == "C":
                    an = all["oC"]
                if all["a"] == "D":
                    an = all["oD"]
                if all["a"] == "E":
                    an = all["oE"]
                if all["a"] == "F":
                    an = all["oF"]
                print(str(s["SequenceNumber"]) + "、" + "答案：" + trimB(an))
                for a in s["Option"]:
                    if trimA(an) == trimA(a["Value"]):
                        answer = a["Key"]
                print("选项：" + answer)
            if all["t"] == "c":
                if all["a"] == "A":
                    an = all["oA"]
                if all["a"] == "B":
                    an = all["oB"]
                for a in s["Option"]:
                    if an.find(a["Value"].replace(" ", "")) >= 0:
                        answer = a["Key"]
                print(str(s["SequenceNumber"]) + "：" + answer)
            if all["t"] == "b":
                if all["a"].find("A") >= 0:
                    an = an + all["oA"] + "****"
                if all["a"].find("B") >= 0:
                    an = an + all["oB"] + "****"
                if all["a"].find("C") >= 0:
                    an = an + all["oC"] + "****"
                if all["a"].find("D") >= 0:
                    an = an + all["oD"] + "****"
                if all["a"].find("E") >= 0:
                    an = an + all["oE"] + "****"
                if all["a"].find("F") >= 0:
                    an = an + all["oF"] + "****"
                print(str(s["SequenceNumber"]) + "：" +"答案：" + an.replace("A．", "").replace("B．", "").replace("C．", "").replace("D．", "").replace("E．", "").replace("F．", ""))
                for a in s["Option"]:
                    if an.find(a["Value"].replace(" ", "")) >= 0:
                      answer = answer + a["Key"]
                print("选项：" + answer)
            if all["t"] == "d":
                print(str(s["SequenceNumber"]) + "：" + all["a"])
            # if q["type"] == "case_problem":
            #     print(str(s["SequenceNumber"]) + "：" + q["question"].replace(" ", ""))
            #     print("答案：" + q["answer"])
            # if q["type"] == "short_answer_question":
            #     print(str(s["SequenceNumber"]) + "：" + q["question"].replace(" ", ""))
            #     print("答案：" + q["answer"])
            break
