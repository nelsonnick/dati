#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64
import hashlib
from PIL import Image

# 249	122	87	104	39	11
# 330	153	110	109	54	20
# 11	10	9	10	10	0
# 146	86	64	79	32	9
# 105	89	68	65	27	7
# 521	227	147	145	78	25


path = 'd:/image'

chapters1 = ["6238", "6239", "6240"]
chapters2 = ["6242", "6243", "6244"]
# types = ["001001", "001002", "001003", "001004", "001005", "001006"]
types = ["001001", "001002", "001003", "001004"]


# 获取百度token
def get_token():
    API_Key = '31AwI8UD7Y2rTK3dpDqc4w9e'
    Secret_Key = 'N2Gv4dEtZd6X0X0DaaH8XGpVv91dr4uB'
    client_id = API_Key
    client_secret = Secret_Key
    base_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='
    host = base_url + client_id + '&client_secret=' + client_secret
    response = requests.get(host)
    if response:
        return response.json()['access_token']


# 百度OCR识别验证码
def get_code(file, token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    f = open(file, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img, "language_type": "ENG"}
    access_token = token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        try:
            return response.json()['words_result'][0]['words']
        except (IndexError, KeyError):
            return '0000'


# 获取验证码
def get_picture(session):
    api_picture = 'https://bw.chinahrt.com.cn/api/kaptcha'
    request = session.get(api_picture)
    picture = open(path + '.jpg', 'wb')
    picture.write(request.content)
    picture.close()
    img = Image.open(path + ".jpg")
    width = img.size[0]
    height = img.size[1]
    for i in range(0, width):
        for j in range(0, height):
            data = (img.getpixel((i, j)))
            if data[0] <= 50 and data[1] <= 50 and data[2] <= 50:
                img.putpixel((i, j), (255, 255, 255, 255))
            if data[0] >= 50 and data[1] >= 50 and data[2] >= 180:
                img.putpixel((i, j), (255, 255, 255, 255))
    img = img.convert("RGB")  # 把图片强制转成RGB
    img.save(path + "1.jpg")  # 保存修改像素点后的图片


# 登录
def login(session, mobile, password, verifyCode):
    m = hashlib.md5()
    m.update(password.encode(encoding='utf-8'))
    result = m.hexdigest()
    api_login = 'https://bw.chinahrt.com.cn/api/candidate/login'
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    data_login = {
        'mobile': mobile,
        'password': result,
        'verifyCode': verifyCode}
    request = session.post(api_login, headers=headers, data=data_login)
    return json.loads(request.content.decode('UTF-8'))['message']


# 自动登录：利用百度OCR识别
def goLogin_auto(mobile, password, name):
    session = requests.session()
    get_picture(session)
    token = get_token()
    picture = get_code(path + "1.jpg", token)
    while login(session, mobile, password, picture) != '成功':
        get_picture(session)
        picture = get_code(path + "1.jpg", token)
        print('-', end='*')
    print(name + '登录成功')
    return session

# 66826
def get_new(str):
    return str.replace("2526gt;", "").replace("2526lt;", "")\
        .replace("&amp;", "").replace("/span", "").replace("span", "")\
        .replace("&nbsp;", "").replace("/p", "").replace("p", "").replace(" ", "")\
        .replace("\n", "").replace("\r", "").replace("\t", "").replace("&lt;", "").replace("&gt;", "")\
        .replace("(", "（").replace(")", "）").replace("br/", "")


def get_json(session, chapterId, questionType):
    url = "https://bw.chinahrt.com.cn/api/questionPractice/listQuestions?chapterId="+chapterId+"&questionType="+questionType+"&number=600"
    request = session.get(url)
    jstr = json.loads(request.content.decode('UTF-8'))['data']
    for q in jstr:
        id = q['id']
        content = get_new(q['content'])
        answer = get_new(q['answer'])
        analysis = get_new(q['analysis'])
        optionA = ""
        optionB = ""
        optionC = ""
        optionD = ""
        optionE = ""
        if questionType == '001001' or questionType == '001002':
            optionA = get_new(q['choices'][0]['content'])
            optionB = get_new(q['choices'][1]['content'])
            optionC = get_new(q['choices'][2]['content'])
            if len(q['choices']) == 4:
              optionD = get_new(q['choices'][3]['content'])
            if len(q['choices']) == 5:
              optionD = get_new(q['choices'][3]['content'])
              optionE = get_new(q['choices'][4]['content'])
        elif questionType == '001003':
            optionA = get_new(q['choices'][0]['content'])
            optionB = get_new(q['choices'][1]['content'])
        res = "{\"id\":\"" + id + "\",\"answer\":\"" + answer + "\",\"A\":\"" + optionA + "\",\"B\":\"" + optionB + "\",\"C\":\"" + optionC + "\",\"D\":\"" + optionD + "\",\"E\":\"" + optionE + "\"}"

        # res = "{\"_id\":\"" + id + "\",\"content\":\"" + content + "\",\"answer\":\"" + answer + "\",\"analysis\":\"" + analysis + "\",\"optionA\":\"" + optionA + "\",\"optionB\":\"" + optionB + "\",\"optionC\":\"" + optionC + "\",\"optionD\":\"" + optionD + "\",\"optionE\":\"" + optionE + "\",\"chapterId\":\"" + chapterId + "\",\"questionType\":\"" + questionType + "\"}"
        print(res)
        # print(id + "\t" + chapterId + "\t" + questionType)


# session = goLogin_auto("15753136829", "123456", "阿拉")  # 自动全部登录
session = goLogin_auto("13685388286", "20101010", "泰安")  # 自动全部登录

for c in chapters2:
    for t in types:
        get_json(session, c, t)
