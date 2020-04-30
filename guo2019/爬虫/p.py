#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import time

examNum = {
    1: "19c18590fc3344b6bad76f573eae0127",
    2: "3042c8970d5f4236aeb2d3e80cd7ab69",
    3: "34af9fd260984f3dae5dddac447fc42a",
    4: "432ea6e391ed4debb32c0978c1a85b7d",
    5: "8626254d9445404a811dac11a93012b8",
    6: "96755d83d13b433380ff3e198a3bc5cb",
    7: "bf785db32caf4fc4bead8e505721c190",
    8: "f924a45e8a3f4ef1ab6f429c314cafa6",
    9: "febcbaebaaca4487bdbf72750d32aeed",
    10: "167f7ea63c6241e4928bcdd8ee6f3c28",
    11: "17bc35dfb07b4fcb99f4b09ca32882e0",
    12: "1b1dc0f6434c4b4eb0b4bd65011453b2",
    13: "1eb6d73db6df4c1b85a3b5c3414b0364",
    14: "2637430a0faf43e9baceb2e3e5b94ba1",
    15: "26c30a9abc1745deb79cec07e28b637e",
    16: "2afa7482aa0549228cf42eb3c0015b90",
    17: "326346650ce64aedb858e54b9bbce673",
    18: "3bc3ffae45da4fd795f124cb71d0bcb6",
    19: "45154c45a24d47548fa8196de6601e13",
    20: "506064ab55ac41babe69023b0a9b7613",
    21: "50afd62e967b4be38983bf58ba92bc05",
    22: "56946be96775444ebbf7e31689cfd20f",
    23: "67dcf3d2d0054cd1906613fbd11c5cee",
    24: "6dd6c52e6dd348e5b3d0618903f5e911",
    25: "72f086fa111e41968fbd2aac92515d77",
    26: "739f24b2e1ff49bcae984ec23e450efd",
    27: "81b1780ec85e454ea573b08d6d2c38c2",
    28: "8ad229bf2d934457a43408c9526b2fb3",
    29: "91ab01c963614bd48325a18adf832cb7",
    30: "a166f511eb764de29067e76e84a28aaf",
    31: "a44a38781af34c20bfda574a647e47e2",
    32: "af4b6342d6ac4b00a0f250a4a7ba7b3b",
    33: "cab8dcb418d44095a64e8ef96bc0e497",
    34: "ce6c8681658140fbb4792d991fa2f6cb",
    35: "d29cdd4c7e054182844e3c83e974e858",
    36: "d4d05c6203084b78bcc8ff465aa0755f",
    37: "d4f3c4b049514b25957cd618a5ca6a6e",
    38: "d7ff866168724cf4ac4fd9dfc8570a3f",
    39: "d844de2b2eea444bab431611a165698c",
    40: "db402e6fe4e8470895b782e6794295e1",
    41: "f0cfbcacf98e4aadbe4ab0ffd33eed63",
    42: "1e7ae8c5f3164fd5bace8fbd87c21c43",
    43: "229905b8752f4cd6bf8912359aef9076",
    44: "349a3cab7fe1410083a1a31214f3a669",
    45: "39167485e2654808ba8cfe5144c57faa",
    46: "59944f3a4dfa45e5b3c76a92b81fb2c8",
    47: "5dd8d57db7084c2daf97ac361296fe61",
    48: "674a38edb2d34be7a576fd96046f6606",
    49: "6cbbe725aece442aa65c470d550aa707",
    50: "763aa7b2b1864e7a9e60edf9c4f2d53a",
    51: "7cc373de152342818a6e142a2e88c290",
    52: "a11be9faeb2340c093c4f9b8e53a33be",
    53: "b55de2e84e7e459aa3940274a7dd06df",
    54: "eece7b5045de4f79ada8c4f9cf6798d2"
}


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
        .replace("》", "")\
        .replace("\\n", "")\
        .replace("\\", "")


# 获取验证码
def get_picture(session):
    api_picture = 'https://bw.chinahrt.com.cn/api/kaptcha'
    request = session.get(api_picture)
    picture = open('d:/image.jpg', 'wb')
    picture.write(request.content)
    picture.close()


# 登录：将所有密码改为hy123456
def login(session, mobile, verifyCode):
    api_login = 'https://bw.chinahrt.com.cn/api/candidate/login'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_login = {
        'mobile': mobile,
        'password': 'e115bc404c7749385936f24c523b2016',
        'verifyCode': verifyCode,
        'RandomCode': '327c9ecc-2e6a-4655-8329-f458b4659c4d'}
    requests = session.post(api_login, headers=headers, data=data_login)
    print(requests.text)


# 获取试卷
def get_exam(session, exam):
    api_get = 'https://bw.chinahrt.com.cn/api/examination/enterExamination'
    headers = {
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "6db161a1-4887-4309-b376-9570a76842eb,479d4110-e722-41af-a2d4-eb5eb95aa03c",
        'Host': "bw.chinahrt.com.cn",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    data = {
        'id': exam,
        'RandomCode': 'a1e0abfc-3a96-4559-8b3d-ce4af888988e'
    }
    request = session.get(api_get, headers=headers, params=data)
    return json.loads(request.content.decode('UTF-8'))['data']


# 保存试卷
def save_exam(session, recordId, answerData):
    api_save = 'https://bw.chinahrt.com.cn/api/examination/submit?RandomCode=275855fc-f1b5-4445-9db2-d4be0b47e82d'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_check = {
        'recordId': recordId,
        'answerData': answerData}
    session.post(api_save, headers=headers, data=data_check)


def goLogin(username):
    session = requests.session()
    get_picture(session)
    picture = input('请查看E盘根目录下的image.jpg文件，并输入验证码: ')
    login(session, username, picture)
    return session


def goExam(session, num):
    j = get_exam(session, examNum[num])
    recordId = j['recordId']
    danxuan = j['questionTypeSummaries'][0]['questions']
    duoxuan = j['questionTypeSummaries'][1]['questions']
    panduan = j['questionTypeSummaries'][2]['questions']
    tiankong = j['questionTypeSummaries'][3]['questions']
    with open("all.json", 'r', encoding='utf-8') as file:
        questions = json.load(file)
    answerData = ''
    for a in danxuan:
        if a["content"][-1] == "\n":
            b = a["content"][0: -1]
        else:
            b = a["content"]
        p = b.split("\n")
        for q in questions:
            if q["t"] == "a":
                if trimA(p[len(p) - 1]) == trimA(q["q"]):
                    answerData = answerData + '{"id":"' + str(a['id']) + '","signed":0,"userAnswer":"' + str(q['a']) + '"},'
    for a in duoxuan:
        if a["content"][-1] == "\n":
            b = a["content"][0: -1]
        else:
            b = a["content"]
        p = b.split("\n")
        for q in questions:
            if q["t"] == "b":
                if trimA(p[len(p) - 1]) == trimA(q["q"]):
                    answerData = answerData + '{"id":"' + str(a['id']) + '","signed":0,"userAnswer":"' + str(
                        q['a']) + '"},'
    for a in panduan:
        if a["content"][-1] == "\n":
            b = a["content"][0: -1]
        else:
            b = a["content"]
        p = b.split("\n")
        for q in questions:
            if q["t"] == "c":
                if trimA(p[len(p) - 1]) == trimA(q["q"]):
                    answerData = answerData + '{"id":"' + str(a['id']) + '","signed":0,"userAnswer":"' + str(
                        q['a']) + '"},'
    for a in tiankong:
        if a["content"][-1] == "\n":
            b = a["content"][0: -1]
        else:
            b = a["content"]
        p = b.split("\n")
        for q in questions:
            if q["t"] == "d":
                if trimA(p[len(p) - 1]) == trimA(q["q"]):
                    answerData = answerData + '{"id":"' + str(a['id']) + '","signed":0,"userAnswer":"' + str(
                        q['a']) + '"},'
    answerData = answerData[:-1]
    answerData = '[' + answerData + ']'
    print(answerData)

    time.sleep(10)
    print('10秒过去了！')
    time.sleep(10)
    print('20秒过去了！')
    time.sleep(10)
    print('30秒过去了！')
    time.sleep(10)
    print('40秒过去了！')
    time.sleep(10)
    print('50秒过去了！')
    time.sleep(10)
    print('60秒过去了！')
    save_exam(session, recordId, answerData)
    print('试卷：' + str(num) + '---结束啦！去看成绩吧')

# 密码必须是hy123456
# s = goLogin('18653145531') # 王天硕
# s = goLogin('13256401880') # 韩琴诗
# s = goLogin('18615405117') # 董华龙
# s = goLogin('13573164731') # 刘子欧
# s = goLogin('15069169006') # 杨明
# s = goLogin('19953165928') # 王晓蕾
# s = goLogin('13854120443') # 李璐璐
s = goLogin('19953168779') # 张红

