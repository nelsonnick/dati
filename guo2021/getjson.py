#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64
import hashlib
import os
import time
import random
from PIL import Image
import threading

path = 'd:/image'


def get_new(str):
    return str.replace("2526gt;", "").replace("2526lt;", "") \
        .replace("&amp;", "").replace("/span", "").replace("span", "") \
        .replace("&nbsp;", "").replace("/p", "").replace("p", "").replace(" ", "") \
        .replace("\n", "").replace("\r", "").replace("\t", "").replace("&lt;", "").replace("&gt;", "") \
        .replace("(", "（").replace(")", "）").replace("br/", "")


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
def get_picture(session, name):
    api_picture = 'https://bw.chinahrt.com.cn/api/kaptcha'
    request = session.get(api_picture)
    picture = open(path + '-' + name + '.jpg', 'wb')
    picture.write(request.content)
    picture.close()
    img = Image.open(path + '-' + name + ".jpg")
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
    img.save(path + '-' + name + "1.jpg")  # 保存修改像素点后的图片


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
    get_picture(session, name)
    token = get_token()
    picture = get_code(path + '-' + name + "1.jpg", token)
    while login(session, mobile, password, picture) != '成功':
        get_picture(session, name)
        picture = get_code(path + '-' + name + "1.jpg", token)
        print('-', end='*')
    print(name + '登录成功')
    return session


# 获取题目
def getQuestionJosn(session, chapterId, questionType, number):
    questionListStr = session.get('https://bw.chinahrt.com.cn/api/questionPractice/listQuestions',
                                      params={'chapterId': chapterId, 'questionType': questionType, 'number': number})
    questionList = json.loads(questionListStr.content.decode('UTF-8'))['data']
    file_name = './json/'+questionType + typeName[questionType]+'/'+chapterId+chapterName[chapterId]+'.json'

    for q in questionList:
        with open(file_name, 'a') as file_obj:
            file_obj.write(get_new(str(q)).replace("\n", "")+',\n')


chapterName = {'6238': '就业创业', '6239': '劳动关系', '6240': '党建理论', '6242': '人事人才', '6243': '综合服务', '6244': '社会保险'}
chapterId = {'6238', '6239', '6240', '6242', '6243', '6244'}
typeName = {'001001': '单选', '001002': '多选', '001003': '判断', '001004': '填空', '001005': '简答', '001006': '案例'}
typeId = {'001001', '001002', '001003', '001004', '001005', '001006'}


def go():
    session = goLogin_auto("15753136829", "123456", "阿拉")
    for c in chapterId:
        for t in typeId:
            getQuestionJosn(session, c, t, '600')

# go()

session = goLogin_auto("15753136829", "123456", "阿拉")
questionListStr = session.get('https://bw.chinahrt.com.cn/api/questionPractice/listQuestions',
                                      params={'chapterId': '6240', 'questionType': '001001', 'number': 5})
questionList = json.loads(questionListStr.content.decode('UTF-8'))['data']
for q in questionList:
    print(get_new(str(q)).replace("\n", "") )