#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64
import hashlib
from PIL import Image

path = 'd:/image'


def get_new(str):
    return str.replace("2526gt;", "").replace("2526lt;", "")\
        .replace("&amp;", "").replace("/span", "").replace("span", "")\
        .replace("&nbsp;", "").replace("/p", "").replace("p", "").replace(" ", "")\
        .replace("\n", "").replace("\r", "").replace("\t", "").replace("&lt;", "").replace("&gt;", "")\
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


# 添加收藏
def addCollection(session, questionId):
    url = "https://bw.chinahrt.com.cn/api/collectionLibrary/addCollection"
    data = {'questionId': questionId}
    request = session.post(url, data=data)
    if json.loads(request.content.decode('UTF-8'))['code'] != 'SUCCESS':
        print('添加收藏失败！')


# 取消收藏
def removeCollection(session, questionId):
    url = "https://bw.chinahrt.com.cn/api/collectionLibrary/removeCollection"
    data = {'questionId': questionId}
    request = session.post(url, data=data)
    if json.loads(request.content.decode('UTF-8'))['code'] != 'SUCCESS':
        print('取消收藏失败！')


# 收藏列表 8953/8954    001003/001007
def collectionLibrary(session, questionType):
    request = session.get('https://bw.chinahrt.com.cn/api/collectionLibrary/listQuestions',
                     params={'chapterId': '8953', 'questionType': questionType, 'number': '50', 'startIndex': '0'})
    if json.loads(request.content.decode('UTF-8'))['message'] == '查询失败':
        request = session.get(
            'https://bw.chinahrt.com.cn/api/collectionLibrary/listQuestions',
            params={'chapterId': '8954', 'questionType': questionType, 'number': '50',
                    'startIndex': '0'})
    id_len = len(json.loads(request.content.decode('UTF-8'))['data'])
    if id_len != 0:
        q = json.loads(request.content.decode('UTF-8'))['data'][0]
        id = q['id']
        answer = get_new(q['answer'])
        content = get_new(q['content'])
        if questionType == '001007':
            optionA = get_new(q['choices'][0]['content'])
            optionB = get_new(q['choices'][1]['content'])
            optionC = get_new(q['choices'][2]['content'])
            optionD = get_new(q['choices'][3]['content'])
            print(id + ':' + content)
            print('A、' + optionA)
            print('B、' + optionB)
            print('C、' + optionC)
            print('D、' + optionD)
            print('答案：' + answer)
        else:
            optionA = get_new(q['choices'][0]['content'])
            optionB = get_new(q['choices'][1]['content'])
            print(id + ':' + content)
            print('A、' + optionA)
            print('B、' + optionB)
            print('答案：' + answer)
    else:
        pass
        # if questionType == '001007':
        #     print('非不定项选择题！')
        # else:
        #     print('非判断题！')


def getNewQuestions(session, questionId):
    addCollection(session, questionId)
    collectionLibrary(session, '001003')
    collectionLibrary(session, '001007')
    removeCollection(session, questionId)


session = goLogin_auto('15753136829', '123456', '阿拉')
# removeCollection(session, '68728')
# removeCollection(session, '68729')
getNewQuestions(session, '68625')
# getNewQuestions(session, '68729')
# getNewQuestions(session, '68730')
# getNewQuestions(session, '68731')
# getNewQuestions(session, '68732')
# getNewQuestions(session, '68733')
# getNewQuestions(session, '68734')
# getNewQuestions(session, '68735')
# getNewQuestions(session, '68736')
# getNewQuestions(session, '68737')
# getNewQuestions(session, '68738')
# getNewQuestions(session, '68739')
# getNewQuestions(session, '68740')
