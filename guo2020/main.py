#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import base64
import hashlib
from PIL import Image


path = 'd:/image'


# 转换图片
def change_pic():
    i = 1
    j = 1
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


# 获取验证码
def get_picture(session):
    api_picture = 'https://bw.chinahrt.com.cn/api/kaptcha'
    request = session.get(api_picture)
    picture = open(path + '.jpg', 'wb')
    picture.write(request.content)
    picture.close()
    change_pic()


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


# 提交日日学
def day_day_up(session):
    api_get = 'https://bw.chinahrt.com.cn/api/questionPractice/saveAnswer'
    data = {'chapterId': '6244',
            'questionType': '001001',
            'answerData': '[{"id":"65307","userAnswer":"A","signed":1},{"id":"65308","userAnswer":"A","signed":1},{"id":"65309","userAnswer":"D","signed":1},{"id":"65310","userAnswer":"C","signed":1},{"id":"65311","userAnswer":"A","signed":1}]'}
    request = session.post(api_get, data=data)
    if json.loads(request.content.decode('UTF-8'))['code'] != 'SUCCESS':
        print('日日学提交失败！')
    return json.loads(request.content.decode('UTF-8'))['code']  # SUCCESS


# 获取周周练id
def get_week_id(session):
    api_get = 'https://bw.chinahrt.com.cn/api/examination/listExamination'
    data = {
        'pageSize': '1',
        'curPage': '1',
        'examType': '009002'
    }
    request = session.get(api_get, params=data)
    return json.loads(request.content.decode('UTF-8'))['data']['rows'][0]['id']


# 重置周周练
def reset_week(session, id):
    api_get = 'https://bw.chinahrt.com.cn/api/examination/checkExamination'
    data = {
        'id': id
    }
    request = session.get(api_get, params=data)
    if json.loads(request.content.decode('UTF-8'))['code'] != 'SUCCESS':
        print('周周练重置失败！')
    return json.loads(request.content.decode('UTF-8'))['code']  # SUCCESS


# 获取周周练题目
def get_week_exam(session, id):
    api_get = 'https://bw.chinahrt.com.cn/api/examination/enterExamination'
    data = {
        'id': id
    }
    request = session.get(api_get, params=data)
    return json.loads(request.content.decode('UTF-8'))['data']


# 提交周周练
def save_week_exam(session, recordId, answerData):
    api_get = 'https://bw.chinahrt.com.cn/api/examination/submit'
    data = {
        'recordId': recordId,
        'answerData': answerData
    }
    request = session.post(api_get, data=data)
    # print(json.loads(request.content.decode('UTF-8'))['message'])
    if json.loads(request.content.decode('UTF-8'))['code'] != 'SUCCESS':
        print('周周练提交失败！')
    return json.loads(request.content.decode('UTF-8'))['code']  # UNKNOWN_EXCEPTION


# 获取token
def get_token():
    AppID = '19667293'
    API_Key = '31AwI8UD7Y2rTK3dpDqc4w9e'
    Secret_Key = 'N2Gv4dEtZd6X0X0DaaH8XGpVv91dr4uB'
    client_id = API_Key
    client_secret = Secret_Key
    base_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='
    host = base_url + client_id + '&client_secret=' + client_secret
    response = requests.get(host)
    if response:
        return response.json()['access_token']


# 识别验证码
def get_code(file, token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
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
        except IndexError:
            return '0000'


# 自动登录
def goLogin_auto(mobile, password, name):
    session = requests.session()
    get_picture(session)
    # picture = input('请查看D盘根目录下的image.jpg文件，并输入验证码: ')
    token = get_token()
    picture = get_code(path + "1.jpg", token)
    while login(session, mobile, password, picture) != '成功':
        get_picture(session)
        picture = get_code(path + "1.jpg", token)
        # print('更换验证码')
        print('-', end='*')
    print(name + '登录成功')
    return session


# 手动登录
def goLogin_hand(mobile, password):
    session = requests.session()
    get_picture(session)
    picture = input('请查看D盘根目录下的image.jpg文件，并输入验证码: ')
    login(session, mobile, password, picture)
    return session


# 完成日日学
def finish_day(session, times=7):
    for num in range(1, times):
        day_day_up(session)
        print('-', end='*')
    print('已完成日日练' + str((times-1)*5) + '题')


# 完成周周练
def finish_week(session):
    id = get_week_id(session)
    reset_week(session, id)
    jstr = get_week_exam(session, id)
    ids = []
    answers = []
    recordId = jstr['recordId']
    danxuans = jstr['questionTypeSummaries'][0]['questions']
    duoxuans = jstr['questionTypeSummaries'][1]['questions']
    panduans = jstr['questionTypeSummaries'][2]['questions']
    tiankons = jstr['questionTypeSummaries'][3]['questions']
    with open("json/questions1.json", 'r', encoding="utf-8", errors="ignore") as load_f1:
        questions = json.load(load_f1)
        for q in danxuans:
            for question in questions:
                if q['id'] == question['id']:
                    ids.append(question['id'])
                    answers.append(question['answer'])
                    break
    with open("json/questions2.json", 'r', encoding="utf-8", errors="ignore") as load_f2:
        questions = json.load(load_f2)
        for q in duoxuans:
            for question in questions:
                if q['id'] == question['id']:
                    ids.append(question['id'])
                    answers.append(question['answer'])
                    break
    with open("json/questions3.json", 'r', encoding="utf-8", errors="ignore") as load_f3:
        questions = json.load(load_f3)
        for q in panduans:
            for question in questions:
                if q['id'] == question['id']:
                    ids.append(question['id'])
                    answers.append(question['answer'])
                    break
    with open("json/questions4.json", 'r', encoding="utf-8", errors="ignore") as load_f4:
        questions = json.load(load_f4)
        for q in tiankons:
            for question in questions:
                if q['id'] == question['id']:
                    ids.append(question['id'])
                    answers.append(question['answer'])
                    break
    an = '['
    for i in range(len(ids)):
        a = {'id': ids[i], 'signed': 0, 'userAnswer': answers[i]}
        answerData = json.dumps(a, ensure_ascii=False)
        an = an + answerData + ','
    an = an[0: -1] + ']'
    save_week_exam(session, recordId, an)
    print('已完成周周练')


# 单用户操作
def one(mobile, password, name):
    # session = goLogin_hand(mobile)
    session = goLogin_auto(mobile, password, name)
    finish_day(session, 41)
    finish_week(session)


# 多用户操作
def get_user(password):
    file = open("user.txt", "r", encoding="utf-8", errors="ignore")
    line = file.readline()  # 调用文件的 readline()方法
    while line:
        info = line.split("#")
        one(info[0], password, info[1])
        line = file.readline()
    file.close()


# get_user('hy123456')

# pyinstaller -D D:/dati/guo2020/main.py


