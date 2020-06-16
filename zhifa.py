import requests
from bs4 import BeautifulSoup
import re

sjids = ['165ae675c5ca4823989ff3e5522e7c41',
         '4e59940f765f4fc8bebb8729e7373c91',
         '93fcc6982de647fe8b1b8ebdf6e32587',
         '0c0177fe7a0e41179f66bb90e882133d',
         'ba6995fceb034157bdfcf0aa9ab4a87a',
         '0482ac621d834722a6d5cad78181ba2b',
         '2a1d787eeafd4195a7b0d00523f4cebe',
         'a4e7f9eb364c40e5b3becc08fd269043',
         '65e33c37bdba40139905e256a28c0062',
         'f00a2ec3b4924cd4a425c73f2498f326',
         '6388d5be416a42918cfe835516810d6e',
         '6040cb29551c456cbf97995611f692c1',
         '6c2d699ee8c9487f8db1eb189628fb00',
         'fdd7e1619a3c4549bbf09a0a7f853d68',
         'bb122f550f0e4f3c9203f3f24b7d62ef',
         '7baf9f5be2f24ab49009ff1b989f7fa0',
         '30797f00d1014262977687bbd5c39053',
         'ee233452b3f0456db273f059af853e51',
         'f246cefe3b3f45f3913a8f5c5b1064b9',
         'ce3982f82597480e9774916c81ad20f1',
         '305ac6cd8f4b472ea3c39adcb05738ba',
         '34edfba9d7aa4ac983618147092e6f8c',
         'dbe672b563b643549a9093d14759c7fb',
         'b9132793e7bb420699fff74fe473cff4',
         '52c4240a72aa4f928dc3caae864aafbc',
         '3c72a3b8512746e195c8b2ef8b84871a',
         'ce430732a1ff4b7faac98edd05713128',
         '9605ece5bbe74ba8bd649f93d55ac93e',
         'c66ef7969c704c57a8e3901a409f1b90',
         'ed90884f67ed42b2a0d09fd853aac6b3',
         '9bebf82e9a154d629de0d4b7a4e480f1',
         '52641f536d634adcb92784a2cf3abbef',
         '4697569f676a45c8ba57c07422c47b17',
         'e1bf519cd5db4e0aa86bcf4052026609',
         'd0cb309a1aad423da3f3d40a9a0e3949',
         '5e0c05f1852741bf862c8bceb3274fae',
         'd6f2f91f2f994e608c52d1dc4f6e2d0c',
         'c34cab421b6844929742a6ee0359db0e',
         '66eb57e7e4f94e0795c4db79e3269744',
         '719205bab8c64203b9d3ddd212d1465b',
         '454a80bbf7b9433fa1dbbe07a1738867',
         'a0cda22f24ab4de088d9db98ed98d1a5',
         '128ca615b0c1466da0eab1e3ccc86f22',
         '0016caacc32442f981edbda4c070fe18',
         'ff391ac3f5894cf6900b829d23d464ef',
         '2917730f4b1c46f7bb84c4d52bc76ab3',
         '4e64d70430214a3c8a44eb4a5ab82920',
         '055443d593bf431395e6e549a923276f',
         '4b76bda310604977a393b47daf6d933a',
         'ce4b6e00da974615ae7ded6f41113974',
         '6d35271b18e947d6bacae39723843391'
         ]


def go(sjid, qtype, num):
    url = "http://123.232.119.108:8083/xzzf/mnexam/stjz.html?sjid=" + sjid + "&qtype=" + qtype + "&num=" + num + "&sytda="
    headers = {
        'Cookie': 'JSESSIONID=B757B62072A740AC1A6584A5B8BC14E0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': '123.232.119.108:8083',
        'Referer': 'http://123.232.119.108:8083/xzzf/mnexam/zujuanNewMain.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
    }

    response = requests.request("GET", url, headers=headers)
    bs = BeautifulSoup(response.text, "html.parser")
    timu = bs.select(".sub-dotitle")[0].get_text() \
        .replace("[单选题]", "").replace("[多选题]", "").replace("[判断题]", "") \
        .replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")
    p = r"\d{1,2}."
    tim = re.sub(p, "", timu)
    id = bs.select("#qbh")[0]['value']
    optionA = bs.select(".m-question-option")[0].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                       "").replace("\r",
                                                                                                                   "")
    optionB = bs.select(".m-question-option")[1].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                       "").replace("\r",
                                                                                                                   "")
    optionC = ""
    optionD = ""
    type = ""
    if qtype == '1':
        type = "单选题"
        optionC = bs.select(".m-question-option")[2].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                           "").replace(
            "\r", "")
        optionD = bs.select(".m-question-option")[3].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                           "").replace(
            "\r", "")
    if qtype == '2':
        type = "多选题"
        optionC = bs.select(".m-question-option")[2].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                           "").replace(
            "\r", "")
        optionD = bs.select(".m-question-option")[3].get_text().replace(" ", "").replace("\t", "").replace("\n",
                                                                                                           "").replace(
            "\r", "")
    if qtype == '3':
        type = "判断题"
    res = id + "\t" + tim + "\t" + optionA + "\t" + optionB + "\t" + optionC + "\t" + optionD + "\t\t" + type
    print(res)
    f = open('d:/test.txt', 'a')
    f.write('\n' + res)
    f.close()


def get(sjid):
    for num in range(0, 40):
        go(sjid, '1', str(num))

    for num in range(0, 20):
        go(sjid, '2', str(num))

    for num in range(0, 40):
        go(sjid, '3', str(num))


for id in sjids:
    get(id)
