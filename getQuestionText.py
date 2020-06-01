#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

# {"httpStatus":"OK","status":1,"message":"考试次数不足","data":null,"code":"point"}
def get_new(str):
  return str.replace("2526gt;", "").replace("2526lt;", "") \
    .replace("&amp;", "").replace("/span", "").replace("span", "") \
    .replace("&nbsp;", "").replace("/p", "").replace("p", "").replace(" ", "") \
    .replace("\n", "").replace("\r", "").replace("\t", "").replace("&lt;", "").replace("&gt;", "") \
    .replace("(", "（").replace(")", "）").replace("br/", "")


json_0530 = {
  "httpStatus": "OK",
  "status": 0,
  "message": "成功",
  "data": {
    "recordId": "db1974779b4746c99a78388d73901ea5",
    "conclusions": "感谢您的参与！",
    "description": "5月份月月比考试",
    "name": "5月份月月比考试",
    "totalScore": 100.0,
    "passScore": 60.0,
    "duration": 10,
    "remainingTime": 599235,
    "questionTypeSummaries": [
      {
        "type": "001007",
        "score": 2.0,
        "totalScores": 76.0,
        "totalNumbers": 38,
        "description": "null",
        "questions": [
          {
            "id": "68500",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;非全日制用工的描述，正确的是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "9ad7cd7ba5ef4fd89be298d71d64da24",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者在同一用人单位每周工作时间累计不超过&amp;2526lt;/span&amp;2526gt;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;0&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;小时&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "a00221fc31e2422389d588252e07b229",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;不得&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;约定试用期&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "507297b3a28f44208ba20dc79a6e1f5f",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者可与一个或一个以上用人单位订立劳动合同&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5e39af33275c4d80a803354cca0f4a0e",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者在同一用人单位一般平均每天工作不超过&amp;2526lt;/span&amp;2526gt;4&amp;2526lt;span&amp;2526gt;小时&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68504",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在办理机关事业单位职业年金转移接续时，需转移的基金项目包括（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f4ce54823444473fafb53aa3ff32b8f5",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;补记的职业年金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "94474e4f26f44ee8988695cfe65d2b6f",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人缴费本息&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "11921b57108949919964b0af0277b0bc",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;原转入的企业年金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "52d8dbddb142429b94107c0bcf050298",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;缴费形成的职业年金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68496",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;就集体合同合法性，人社&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;行政部门&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的审查事项包括（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "56f8553f005b4a40aa7d37c33ec73793",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;协商双方主体资格是否符合法律、法规和规章规定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "b0401aa7ecc64701a49edc00f5de237b",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;内容是否与国家规定相抵触&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "e0d41f9000bd4b96865f293b3309adc4",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;协商程序是否违反法律、法规、规章规定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "1cc82b8e95b34dba911d536b1b47fc1a",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;集体合同约定的工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;增幅&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;是否合理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68480",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;属于高校毕业生基层服务项目的是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "927451c7ebbd4941b0c5c7075386158a",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公益&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;就业行动计划&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "f4f427857e5c46bfacef7e5b8aa9d67c",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;大学生村官&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "904d6454e0a6494bb6360336ac1102dd",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;志愿服务西部计划&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "2b36fd34d56847ab9cac35b985872cbd",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;“&amp;2526lt;span&amp;2526gt;三支一扶&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;”&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;计划&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68502",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;甲&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;介绍两&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;名&amp;2526lt;/span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;周岁未成年人到&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;乙&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司工作。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;甲公司应被罚款&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;元。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "7c0d622fb57342de96a2129d7308edeb",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;10000&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "c1a0847ea4894cadb951c8f3ae240e15",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;15000&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d037f292946c4cbd9d3e1d6732f37324",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;000&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "7f813846f6414247916072bb673a0379",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8000&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68498",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于女职工生育享受假期，正确的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;是&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "7943a068d62f4140b7683a9b45109a9f",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;难产的，应增加产假&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;15&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天；生育&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;a href='http://baike.so.com/doc/6393709-6607366.html'&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;多胞胎&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/a&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的，每多生育&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个婴儿，可增加产假&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;0&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d14b768c970749c3be0f197ca5cff32d",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;女职工生育享受&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;98&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天产假，其中产前&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;只能&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;休假&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;0&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "c4361f9317bd46bc8b4815c1d586ccff",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;怀孕满&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个月流产的，享受&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;48&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天产假&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0f00c745a39348efb71887e73a9e8911",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;女职工怀孕未满&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个月流产的，享受&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;15&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;天产假&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68487",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职称评审委员会评审专家应当具备的条件是（&amp;2526lt;/span&amp;2526gt; &amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "ba80a809afb14d97aa8d17279863c754",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;具备良好的职业道德&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "90b84eb1baea462d84a1a5547b7321ee",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;从事本领域专业技术工作&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "778f11b220304caca415ee63ea81d0a3",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年龄不超过&amp;2526lt;/span&amp;2526gt;60周岁&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "624152cd695643fa8df4499e2581bf82",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;具有本职称系列或者专业相应层级的职称&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68482",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f0809c745d66451ebc3fdbf8014a1cc5",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;正常运营&amp;2526lt;/span&amp;2526gt;9个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "874900f58cfa4d96b156912a817cc1f8",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;正常运营&amp;2526lt;/span&amp;2526gt;7个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "e66bb8db69564cf183125b86fd250408",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;正常运营&amp;2526lt;/span&amp;2526gt;5个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0547ca51eb304b5abc2cf0747cb00e27",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;正常运营&amp;2526lt;/span&amp;2526gt;3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68497",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业裁减人员时，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;依法&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;应当优先留用（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "ed2305f4cd77402098dc0107273c914f",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;掌握企业核心技术、对&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业发展&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;至关重要&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "2759aa941299419aa40fc6ea333831c8",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;家庭无其他就业人员，有需要扶养的老人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "e2f332ef8c7a4d01befe5295f8e08467",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;与本单位订立&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;期限劳动合同的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "06b327721fe64a2aa4792367b4b68b79",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;与本单位订立无固定期限劳动合同的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68499",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位首次被列入拖欠工资&amp;2526lt;/span&amp;2526gt;“黑名单”的期限为（ &nbsp;&nbsp;）年；被列入“黑名单”的用人单位未改正违法行为的，期满不予移出并自动续期（ &nbsp;&nbsp;）年。答案正确的是（ &nbsp;&nbsp;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "9cf10e75ad7d4616b40d280269b6d564",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2 &nbsp;&nbsp;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "80db7d9ef2a948369ed5057c14b1a325",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1 &nbsp;&nbsp;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5962c279795446d3bc741147171e6ac3",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1 &nbsp;&nbsp;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "45a8ad2301d84f8d85f65e8cd77eeb01",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2 &nbsp;&nbsp;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68493",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "4e4e48e8bbb14f31bc99285bd920fff3",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;不属于本仲裁委员会管辖&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "8b8276ea52b24d878392e0eb3d491b4d",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;不属于仲裁委员会受理争议范围&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "6665ffbe1be54c9199bdae4313453479",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;确认劳动关系&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "3c2eb779c87344b188b99f5e50c66250",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;调解协议达成之日起&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;10&amp;2526lt;span&amp;2526gt;日内未提出&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68476",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;可以进行失业登记的人员包括( &nbsp; &nbsp;)&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "b3375f14bf6a4163ac3a367bd40ed6fd",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;年满14周岁，从各类学校毕业、肄业的&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "98c6f4dcc9eb401699f538ff9463a7d1",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;退出现役军人&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5e195dffc4e3454ebc7981d093ca7d77",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;刑满释放人员&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "370bc976b3e84d3796b9c79edd12cd24",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;个体工商户业主或私营企业业主停业、破产停止经营的&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68494",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;用&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人单位有下列（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;）情形的，劳动者可以解除劳动合同。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "6afe1f7e38a340729a1de1ffdf2a2274",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;未及时足额支付&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "ce42cf1a48714052835171f839862775",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;使用欺诈手段，使劳动者在违背真实意思的情况下订立劳动合同的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "859d89976425436d92b6845471ecfb4d",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;未依法为劳动者缴纳&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;养老保险费&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "3f4e9c23e2da4220bfe993324a96bb71",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;未按照劳动合同约定提供劳动保护&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68507",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "bf2e02d2b0f94218859cb19af9a9d008",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照职工本人工资一定比例的供养亲属抚恤金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d9da19159fba40d799156621f9d4dbb0",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;一次性工亡补助金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "84a6609f4dbe4d389ecbd57b339066a1",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8个月丧葬补助金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "b115f816c6b64272a1e8a06097f515b4",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;伤残津贴&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68481",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;为推动农村劳动力有序外出就业，对（ &nbsp; &nbsp;）开展有组织劳务输出的，给予就业创业服务补贴。&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "10944dc8ab4146e3a3110b8d62d73e51",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;经营性人力资源服务公司&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "75b250a6b7094c51856792c0c95af08c",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;劳务派遣公司&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "8a549cc4b48a471f9e37dbdf4e725648",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;公共就业服务机构&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "00c47ed289e847ed9bff7959150168a1",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;劳务经纪人&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68473",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业招聘广告内容中，属于&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对劳动者就业&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;歧视的情形包括&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "21ab1c7be085468a9828ba165375088a",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;需要经常出差，男士优先&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "1fd2263c4f284970aac22932eb88196d",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;本岗位需要值夜班，怀孕&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;8&amp;2526lt;span&amp;2526gt;个月以上的女性不予考虑&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "7c4d2f95af1744feaebb6bd456ce8946",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "06f57cf6299542b0bb93a764a2a38b32",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;具有互联网工作经验优先&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68495",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在申请仲裁的时效期间内，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;仲裁时效中断&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的情形包括（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "ea6f9633a1a6472da9da547f3b93b5a4",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位书面承诺，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;个月内向劳动者支付拖欠的劳动报酬&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "e3fd843f6a534c8c85abe09904cf88db",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;张某向调解组织申请，希望调解组织组织调解用人单位与其个人的劳动纠纷&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "b0f94aa08961425dabe5ecf033ef6541",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;针对用人单位拖欠的工资报酬，张某&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;向人民法院申请支付令&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "8fc6f29fbe96489f856b5b2a56a27b22",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;张某主动与用人单位协商，要求其支付其加班工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68488",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;针对疫情防控期间一线医务人员，可采取的保障措施有（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "64fffa19ed77438fbea06d875f45fd9e",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据工作情况，疫情防控一线医务人员可以享受临时性工作补助&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "6c50355c57784097bd64eb3d00c16689",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;一次性绩效工资总量应向&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;医院及其医护人员、疫情防控人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;倾斜&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "ebea0d49a24d44b797afad3276628f4b",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "17f42f3f8a5943249b42dddf9af7363e",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68501",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于试用期，正确的是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f329c964e4fa4e67803850561564f629",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;王某与&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;签订&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年的劳动合同，约定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;span&amp;2526gt;个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的试用期&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "35bb14c4f1924e669c20d3a5f42476d9",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;王某进入某事业单位工作，签订为期&amp;2526lt;/span&amp;2526gt;2&amp;2526lt;span&amp;2526gt;年的聘用合用，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;必须&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;约定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;12&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个月试用期&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d1171e1cf4914f478bcccb9b8196192d",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;约定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;王某&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工资为&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;/&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;试用期工资为&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;7&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;00&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;/&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d04bcd14c7d34dc6b91e7a3664613a48",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;王某与&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;续订为期&amp;2526lt;/span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;年的劳动合同，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;未约定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;试用期&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68490",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "4bc5431463ca4119a0b446096c323a9d",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;高寒、高海拔安置区&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "fe98fb17e3914bdaa3d6b60727a9dd77",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;“&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;三区三州&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;”&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;等深度贫困&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;地区&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;安置&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;区&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "26b667c5f6dc4ba186d6088dc722b10d",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人口&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;规模&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;以上大型安置&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;区&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "20182d3144ee4c5d858671c62979050e",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;城镇&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;和工业园区安置&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;区&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68506",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工因工致残被鉴定为六级伤残的，其劳动关系可按（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）方式处理。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "5f4380d56fe34e359536d376cc479371",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工伤职工本人提出，可以与用人单位解除劳动关系&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0b47d659c67f45e7abe5213c6825a872",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照统筹地区职工平均工资的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;span&amp;2526gt;支付伤残津贴&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "f5991180a3e24c7a91b0a204e77e6aaf",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性伤残就业补助金，由工伤保险基金支付一次性工伤医疗补助金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5e2848d6ad724627a4dd2b302c8032cb",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工伤职工本人提出，可以与用人单位终止劳动关系&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68484",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）工作日内办结失业登记，以适当方式主动反馈办理结果。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "6fb0ca41b4cc40a699a5b77014d55268",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;5个&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "307d3fdf7cd640228d19b8f0891e18a9",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;3个&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "9f397a9e9e474b3c965ef5f7c58d62c0",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;10个&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0c4af676aaf4445d8000fb7398a3b058",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;7个&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68510",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于工伤保险，说法错误的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "2a709a1895b5400282167e8e01254d1a",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位参加工伤保险并补缴应当缴纳的工伤保险费、滞纳金后，由用人单位支付新发生的费用&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "68f7663c96da4e08854dd3899b7839ed",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位和职工个人均应按时缴纳工伤保险费&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "d6aa5869689b400bb2d250d0120d6999",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工在抢险救灾等维护国家利益、公共利益活动中受到伤害的，可以视同工伤&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "502365b7ac984f178a7bcf65773eed60",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;设区的市级劳动能力鉴定委员会应当自收到鉴定申请之日起&amp;2526lt;/span&amp;2526gt;30&amp;2526lt;span&amp;2526gt;日内作出鉴定结论&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68477",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;外国人在中国就业&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;是&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;指没有取得&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "5cba6c3ee80b4e92954c578d04cbb4c4",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国籍&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "b664f706863e4dab96f4355b34cfb348",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;居住证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "c895a07e93f549a1a3962027006b6085",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;暂住证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "2841cc9afd764cba99185a41bdad730f",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;定居权&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68508",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，严重失信、失范行为包括&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "27340421208d4b3f91d8b81f7d93a181",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "dbad3c856c564a8781e2650899de6c2f",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位未按相关规定参加社会保险&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0b6825b7afff4393894989583a39dcfb",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;应缴纳社会保险费却拒不缴纳的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "10ede8629eb04877afda9b4c806018d6",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位未如实申报社会保险缴费基数&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68474",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "d15f6c570e534aec843e4f5eaf446c7e",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;员工自愿承诺，在本公司工作期间避免生育&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "a2de09ffa6b24e7eb79ed1f8ba286b31",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "feaf840849084f0180a3c2ba8e91557d",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "a1e507576bcc43029309f65a2f15d635",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;员工自愿承诺，在本公司工作期间不结婚&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68491",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;博士后设站单位可以将在站博士后予以退站的情形包括（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "b98d023dfded4eddaf5ff0a4959f5865",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;无正当理由不办理出站&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;手续&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "79fb948ac1704566914e51a7b8333ad8",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;提供虚假材料获得进站资格的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "fba33f8e4ad8428cab2ed629c7e00189",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;进站&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;三&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年后仍未取得国家承认的博士学位证书的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "2fc7de96270341478e0bd1390f8428b4",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;因患病等原因难以完成工作的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68475",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;属于行政审批项目的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "d94a6be01db9470fb00c4b2623e9c448",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职业中介活动&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "84b0810474324ae8a8648088993b35a7",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;承接人力资源服务外包&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "9dd3fa219d7e4ccc935beb20bf83fbd0",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业实行不定时工作制和综合计算工时工作制&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "383480496cee4af882b1af4d035c630e",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳务派遣经营&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68478",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;《就业补助资金管理办法》规定，下列&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;属于享受职业培训补贴的人员范围&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "7c3507e440034db8a97eebe6bb963548",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;农村转移就业劳动者&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "c4ff246e20b64abaa1af967d34e9fa5e",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;城镇登记失业人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "ce94d43880be4a1497eeb1aa11374747",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;毕业年度高校毕业生&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0059db0489144e6283bdd1c02fc0b912",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;贫困家庭子女&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68503",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;《领取社会保险待遇资格确认经办规程（暂行）》规定，属于丧失领取养老保险待遇资格的人员包括（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "e139c91582b24784a122472146b4450d",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国家人口库中标识为&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;死亡&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "84ec8af563b244a19da6dc8b826a020b",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人力资源社会保障服务平台确认及上报的死亡人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "196fbd878fd44f43bbda84155a8be26e",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;家属反映其父母仍然健在的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "7b400ee4637e4a12b02668591230868c",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;全民参保登记数据库标识为&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;健在但&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;服刑的人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68485",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业未经许可擅自从事职业中介活动，获利&amp;2526lt;/span&amp;2526gt;4&amp;2526lt;span&amp;2526gt;万余元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;罚款&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;金额可以是（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "e7fe839699b34890a9e1033c1ee65a4e",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;万元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "233b64fad1a74b9abca380d65d1ca276",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;万元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "dd18fbaa7c5a4894ab30c0026898b7a5",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;18&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;万元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "20fc7ff7ea7a41d7bac18d7d28348436",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;万元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68479",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对公益性岗位安置的就业困难人员给予岗位补贴，补贴标准参照（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）执行。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "a2acd7ed693d4fc59d2ccc3911343d43",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;当地社会平均工资标准&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "eab24c5c1fac4511a5fc2fc6d7c65f96",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;当地同等岗位工资标准&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "caab21ae998b4145b79f9694142943ff",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;当地最低工资标准&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "336978c609d941559da759cd21f5a355",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;当地失业保险金领取标准&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68505",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;从事个体工商经营的港澳台居民在内地（大陆）参加社会保险，正确的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "b6ca982fb77548aa827dffe89c348057",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可以&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;参加&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;基本医疗保险&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "05395aa8e8a444339dfe4a2294f38c47",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在注册地参加社会保险&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "4ff3e71d82494bd6a6fcff2ce372758b",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在居住地参加社会保险&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "0c5fa5bd891746af9ac11eedbab1cb46",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可以参加职工基本养老保险&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68492",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）的社会化评审机制。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f300cc646c884c748cb27c27a568c4c7",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;业内公正评价&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "b2fc36c456bb44048d0bb0bd5df135c4",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人自主申报&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "e1c21b6b73c642039fbb83b437ad2c90",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;单位择优使用&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "391af79bab4d4223aa37c00bfe12262a",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府组织认定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68489",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;乡村公益性岗位所签订的劳动合同或劳务协议期限可以是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "c35f15d0a47e42b2913c20e4235b2060",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;180天&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "df50ac3f2ed74a1997370614b7199f5e",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;一年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "c4ebff44f0dd4640986e0c5c20e10e68",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1年半&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "30f166622aee4b64bf86a60328230e99",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68486",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&nbsp;&nbsp;&nbsp;&nbsp;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f56db9fda3b044ad8b426dafd2609526",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;000&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5862403fd50c4993ac813321c9d36414",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;000&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "5d6038f6df91461d9a5b3e0bfb6a1346",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;7&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;000&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "3f6a4f796beb4a82ba9a1f4c899d8030",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;000&amp;2526lt;span&amp;2526gt;元&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68509",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业年金基金财产投资范围包括（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "8ee3dc26b9104e60addd17a01e5df06a",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国债、&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;中央银行票据&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "7f0d18e2e9dd4d30be08ea6f2e0dae6a",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;证券投资基金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "35c94483593b4823aa7518f7012de6cd",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;银行存款&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "653dc845e82349c48bfb72a6ea1844fd",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;债券回购、万能保险产品&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68483",
            "type": "001007",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照现行规定，面向个人发放的创业担保贷款期限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可以是&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "c4af6effd19f45ffbc086f39520a03fb",
                "sort": 1,
                "code": "A",
                "content": "&amp;2526lt;p&amp;2526gt;2&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "dcd024a863864e1295c75ecbe22c734f",
                "sort": 2,
                "code": "B",
                "content": "&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "986a1a2fc72b42c28c39411c58450f14",
                "sort": 3,
                "code": "C",
                "content": "&amp;2526lt;p&amp;2526gt;3&amp;2526lt;/p&amp;2526gt;"
              },
              {
                "id": "8777899a6b36420cb3b66e17f2ae3666",
                "sort": 4,
                "code": "D",
                "content": "&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"
              }
            ],
            "keywords": "null"
          }
        ]
      },
      {
        "type": "001003",
        "score": 2.0,
        "totalScores": 24.0,
        "totalNumbers": 12,
        "description": "null",
        "questions": [
          {
            "id": "68455",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;对违反劳动保障法律的行为，如发生在3年内，劳动保障行政部门应当依法受理。&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "55d9948fb8ea43648c735cb64b93d4e6",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "1251ad20c7434b698b0b18a020f27e56",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68450",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照人社部财政部文件规定，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府投资开发的公益性岗位，只限安排符合岗位要求的就业困难人员。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f2d7d36a80be4812bad72e42cc9f0226",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "512763daf07f465aae28ba05ece800ce",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68459",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;女职工禁忌从事的劳动范围，可分类为经期禁忌从事的劳动范围、孕期禁忌从事的劳动范围和哺乳期禁忌从事的劳动范围三类。&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "ce77195294cb4f8dafd617df347c8cf9",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "6ff55ec1c68c4b18841c8c7d8ed9f5df",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68460",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《社会保险基金财务制度》规定，社会保险基金预算按险种、不同制度和参保对象分别编制。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "8d7a7c5f9fe54961b9f28da7c6512529",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "8080cff438d04fa5b6eda09b8496682a",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68454",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "d8b9596a6c72451ebb8a6a9c30e63bef",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "1282a2ff80bd4bcab3f0a84ee7904a69",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68451",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;地方各级人民政府和有关部门、公共就业服务机构举办的招聘会，不得向劳动者收取费用。&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "b6226bdc7e1549389048971dec36caf6",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "07b2e2a43421456d864772c977430a96",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68452",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "396f03a688464c50a9e4b9dd37d5d166",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "31a1d0d416f24d36acd7a1b95c19632b",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68461",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工再次发生工伤后，如果之前未享受过伤残津贴待遇，则此次发生工伤后可以享受。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "c548f12c02934593ac9e3563578941a1",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "13d570453323443cb0a04020afc6ced6",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68456",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;中央直属企业实行不定时工作制和综合计算工时工作制等其他工作和休息办法的，经国务院行业主管部门审核，报国务院劳动行政部门批准。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "f9ddf3c0475e43e8b738b16e56201f0c",
                "sort": 1,
                "code": "A",
                "content": "正确"
              },
              {
                "id": "c5e7f862a40a4658ab55ed194352bbd6",
                "sort": 2,
                "code": "B",
                "content": "错误"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68458",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;生效的专项集体合同，应当自生效之日起由协商代表及时以适当的方式向本方全体人员公布。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "2453dc4119214f96871f9ec9d535522d",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "14c1efad89a5472799109e4d401c07b5",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68457",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者依法享受探亲假、婚丧假、节育手术假等国家规定的假期间&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，视为正常劳动，但带薪年休假的假期除外。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "d4423abdeb38457296680fe5ea4cbc9b",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "307057a9e4314385bd2c9b8359065dcf",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          },
          {
            "id": "68453",
            "type": "001003",
            "level": "003001",
            "content": "&amp;2526lt;p&amp;2526gt;行政处罚的执法决定信息要在执法决定作出之日起10个工作日内公开。&amp;2526lt;/p&amp;2526gt;",
            "answer": "null",
            "analysis": "null",
            "score": 2.0,
            "userAnswer": "null",
            "blanksNumber": "null",
            "signed": 0,
            "checkResult": "null",
            "userScore": "null",
            "tag": "008001",
            "chapterName": "null",
            "inCollection": 0,
            "choices": [
              {
                "id": "efbb439a52c34640a7e8e057b114159b",
                "sort": 1,
                "code": "A",
                "content": "错误"
              },
              {
                "id": "e98cd9fcf5b548e5a4e5a7f87f5d5ae2",
                "sort": 2,
                "code": "B",
                "content": "正确"
              }
            ],
            "keywords": "null"
          }
        ]
      }
    ]
  },
  "code": "SUCCESS"
}
json_0531 = {
	"httpStatus": "OK",
	"status": 0,
	"message": "成功",
	"data": {
		"recordId": "5ad9030fb58a45e4a1be289e540a4239",
		"conclusions": "感谢您的参与！",
		"description": "&amp;2526lt;p&amp;2526gt;5月份月月比考试&amp;2526lt;/p&amp;2526gt;",
		"name": "5月份月月比考试",
		"totalScore": 100.0,
		"passScore": 60.0,
		"duration": 10,
		"remainingTime": 599322,
		"questionTypeSummaries": [{
			"type": "001007",
			"score": 2.0,
			"totalScores": 78.0,
			"totalNumbers": 39,
			"description": "null",
			"questions": [{
				"id": "68524",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府对符合领取城乡居民养老保险待遇条件的参保人全额支付基础养老金，其中，中央财政对中西部地区按中央确定的基础养老金标准给予&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "455b46841e5c4ae2a677b9edf69c5ef7",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "10e0a465cf3c4d44a5a08dffc69cef47",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "8a2553e1166b41b89177886c49217071",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;50&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "348a8125c3d74fdb96154fe1511f2e12",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;30%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68549",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;申请职业培训补贴时，（ &nbsp; &nbsp;）等证明材料不再提供。&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "f640994097bc444e90a4d5dd6f2a63ef",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;职业资格证书&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "59714a58dad0441e922a192dfe6b7eee",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;职业技能等级证书&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "e02d4d9816ee4a3399c80749b706511f",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;专项职业能力证书复印件&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "ca3930b7e17a4108bff98374cbd23777",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;培训合格证书复印件&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68537",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在社会体育指导员中，属于准入类职业资格的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "de4f6781fc594f0fb3095f0579a1b026",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;游泳&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "edba44476b20490aa012d0de1c3a721e",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;潜水&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "042ff6c235f643e4947eec93a51abc9a",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;滑雪&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "3d16670aca6a45f0ae60f0effcbf74cc",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;攀岩&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68513",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于领取失业保险金，说法错误的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "75d415f729e2491fbe6982f2dae1abca",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;领取失业保险金期间患病就医，可以享受职工基本医疗保险待遇&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a495fa444d5942e2b93d9a8fb5718eb4",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在领取失业保险金期间病逝，其遗属可以领取丧葬补助金和抚恤&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "cf66a2bee75247158e12694410b5e01d",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;领取失业保险金期间重新就业，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;停止领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;失业保险金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a7adcb0803ca479bba46babfc79f719b",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老王&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;领取失业保险金期间应征服兵役，可一次性领取未领取的失业保险金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68548",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对返乡入乡创业企业吸纳（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）就业的，按规定给予社会保险补贴。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "a87476d78c3d44a59e133a2ce114bb03",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;事业单位专业技术人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "64e92c2026a34b5a912fbc8cad2cc41d",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;就业困难人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "9d5562af73d04ef08767fe71e16e1558",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;复员转业退役军人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "72248ef7d2064dc8af595fcbe4aababb",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;农村建档立卡贫困人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68514",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业职工依法依规参加失业保险&amp;2526lt;/span&amp;2526gt;36&amp;2526lt;span&amp;2526gt;个月及以上，自&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2017&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日后取得（ &nbsp;&nbsp;&nbsp;）职业资格证书或职业技能等级证书的企业职工可以申领失业保险技能提升补贴。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "111be9ab0cb44dca97dc768cb3f5b03f",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;技师（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;二&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;级）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "210f23d87b2049b0a423e082eaaba377",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;初级（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;四&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;级）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "71df2fb8e21c47f59cd3d8afb0b19b00",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;高级技师&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;一&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;级）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6478f49c628747aeb44b31ed675c051e",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;中级（&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;三&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;级）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68543",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人力资源社会保障行政部门应当（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "d9a04e8967374180a6660e7a47d20faa",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;维护市场秩序&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，保障公平竞争&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "ff65747c3056419fad079a8dfb64c0b2",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;保障充分就业，推动企业与劳动者签订劳动合同&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "0f97f27ff2074e2e80a02df0ef02ce21",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;加强人力资源市场监管&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "24acf3eb61db40f2a83a889766c8c099",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;调控人力资源市场供求关系&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68515",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;参&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;加基本养老保险的个&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人因病或非因工死亡的，其遗属可以领取的待遇项目有&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "e2471930524e40fd8ed75904e2d4f6a9",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;因病特殊补助&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "75705f5c3da94abea4d0238602e0cdb4",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;丧葬补助金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "33f4eb1d46714a61a0df88a8f02af563",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;抚恤金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "902095300b5043c7b74b7967d4a23adf",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;非因工死亡医疗补助&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68540",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;《外商投资人才中介机构管理暂行规定》&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请设立外商投资人才中介机构的材料包括（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "415bee8f17774f2185924f34fb001282",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;书面申请及可行性报告&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "fe80dad9633948f09f82a093606897ef",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工商营业执照（副本）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "dcaa4e6dc8284657a74ff4f28df808cc",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;合资各方开展人才中介服务&amp;2526lt;/span&amp;2526gt;3年以上的资质证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "c044d317844b4710a8da5ca7724ffc2b",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;管理制度草案与章程&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68545",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;通过人力资源市场求职、招聘和开展人力资源服务，应当遵循（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）的原则。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "20143eaed338457b94f692a3a4141246",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;诚实信用&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "ad128151de8341a9ac1350cf7e2f8a8b",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;合法&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;、公平&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "890ddf7359a148678d387f66f7603637",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;快捷、高效&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "56c10ad24ab347c9b540fd02c47362f2",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;书面交易&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68536",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;机关事业单位职业年金基金应当委托具有资格的&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;作为（ &nbsp;&nbsp;）人，负责职业年金基金的投资运营。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "87cda8808d0f4641a147649ae8b296f6",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;投资运营机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;投资管理人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "8d088bfccb154b998c5a76909849277f",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;商业银行&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;受托人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "57db1209088a4481bbb718240d384fcc",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;投资运营机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;托管人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5f98f6cb0ead40a28dbc789c2033af30",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;商业银行&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;投资管理人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68523",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在提高城乡居民养老保险最低缴费档次时，对（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）等困难群体保留现行最低缴费档次。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "067bf66c7b594f7baeb8c1e420e97068",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;低保对象&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "2b9e746e615746eca5b7919f685c71b8",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;特困人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "e436b49e91be407aa20e21afd6849083",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;高校应届学生&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "224d837ed64c40d5b4730e7189ad9c47",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;建档立卡未标注脱贫的贫困人口&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68542",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人力资源社会保障行政部门对经营性人力资源服务机构实施监督检查，可以采取的措施有（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "ccf7724da8664f359cab02525ed62b21",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;要求被检查单位提供与检查事项相关的文件资料，并作出解释和说明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "0fe2a0d320594f57b7e14b9c602fe97e",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;采取记录、录音、录像、照相或者复制等方式收集有关情况和资料&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "e5fc147aa4124c00a8248f4a6b9afb80",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;进入被检查单位进行检查&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "2fa3233fb4da4e06908d0134feb10e7c",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;询问有关人员，查阅服务台账等服务信息档案&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68520",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工伤保险基金由&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;组成。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "90a5aec1108c43d8bac4bac073e4c1da",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位缴纳的工伤保险费&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "930b06d385cb48eda9ec6d123630a278",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;依法纳入工伤保险基金的其他资金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "74907c5415af48a281fe96d3a6d19e97",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工伤保险基金的投资收益&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "8c9e98209a8043ea96d14fbb4aaf0624",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工伤保险基金的利息&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68511",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于工伤保险待遇标准，错误的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "04ad035dfc094db8add96f3b02480980",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;三级伤残的一次性伤残补助金为&amp;2526lt;/span&amp;2526gt;23&amp;2526lt;span&amp;2526gt;个月的本人工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "36cb51bfa57e4b3eb49ff72d8dcf77de",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;十级伤残的一次性伤残补助金为&amp;2526lt;/span&amp;2526gt;6&amp;2526lt;span&amp;2526gt;个月的本人工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "105349959f104cdb8c9da4ea172f9ef3",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;三级伤残的伤残津贴为本人工资的&amp;2526lt;/span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "15768506fc4f4e08a5f327ffb9bbe0fb",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;一次性工亡补助金的标准为上一年度全国城镇职工平均工资的&amp;2526lt;/span&amp;2526gt;20&amp;2526lt;span&amp;2526gt;倍&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68519",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;社会保险待遇发放岗位任用的正式人员，可以连续任职&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;年。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "8c313f4840b743fcb3fd6b0bd1788427",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "e92ee2e1d9184163a5fbd792653a7eb4",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "61739ee70bfa4d40bb246f7c63220932",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;3&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a6daf062f74a47f1b9dc8ae60d01968f",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68547",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;关于公益性岗位政策的属性，正确的( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "b0f492f67c2147e28f83c03b835eb608",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;具有福利性、救急性&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6ba9ce0f353e41f086ebf839a3139c5c",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;具有托底线、临时性&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "21b881c40bbf43f2b77671f07441b9c7",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;具有临时性、福利性&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "3eb4e8a82a44468a9b2de741c67f9c60",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;具有托底线、救济性&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68518",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可以制订行业标准的部门是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "2b3c628b5fd54a89b5f5248bcaf368b7",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国务院标准化行政主管部门&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "0398c52a24ec4c5dbdd65e0d83e0e84f",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;省级人民政府&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a71924c2b3714c73864727b9ccffead7",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;人力资源社会保障部&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "2efef6fa16fc4cf28472a145e86cd1e9",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;财政部&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68535",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于参保人员跨统筹范围流动或从机关事业单位流动到企业，说法错误的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "5492b49884134ba7881d3a61095b1857",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人缴费按本人养老保险个人账户储存额&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;12%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;转移&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "85c03e2f7518487781227cea6e2579ba",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;单位缴费以本人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;工作年限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;为基数，按&amp;2526lt;/span&amp;2526gt;12%&amp;2526lt;span&amp;2526gt;的总和转移&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "efc39cf3192b44d4af919d2f5a0edbac",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人缴费和单位缴费部分应暂且不予转移&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "62784d1f6ce04f03872312a10dbbe554",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人缴费和单位缴费部分应当全部转移&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68522",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;各级劳动保障部门作为被征地农民社会保障工作的主管部门，负责被征地农民社会保障政策的&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "5eb3240f0f7f4a59b91f56e74e563038",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;审批&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "dcf1611107ef44e5a65af815db1f7d56",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;审查&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "9716620f0e7247c2a61d102bfbcf0e77",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;实施&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "664c6e6f25cb4ec5b1123b1f6fbd4c91",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;制定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68546",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国家建立（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）的人力资源市场体系，发挥市场在人力资源配置中的决定性作用。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "9651bb2a933c40c0b2d4a1e488fa601b",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;平等一致&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "067b9207ac384309862b975ab670c345",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;竞争有序&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "b64bad4a1aed473898348ac17565c1a1",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;自由竞争&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "307df5463c2242ba9ae980854cedf62f",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;统一开放&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68527",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工老王通过伪造病历骗得鉴定结论，并领取&amp;2526lt;/span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;万元工伤保险待遇。按照《工伤职工劳动能力鉴定管理办法》规定，可对老王处以&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;的罚款。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "9caee5f1ac5c4c04bbf0207eb9e4757e",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6&amp;2526lt;span&amp;2526gt;万&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "08165329147945548fc8659a1703897e",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;span&amp;2526gt;万&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "9e521f17899a447a83beb3ac895590b1",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;万&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "4e674658dd8247a8b9f578730841e53b",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5&amp;2526lt;span&amp;2526gt;万&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68532",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业和职工建立企业年金，由企业代表委托人与受托人签订（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）合同。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "c8d0d76c9d444c4fb57e2a60d720253c",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;委托投资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6a10e4f02e094e959a41ce58df580782",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;委托管理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "1c25e3a00cb1486cbf93a5a926f3fc24",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;资金托管&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "4a1f3210eb21458ab96a2a7368a7e639",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;受托管理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68538",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;属于准入类职业资格的是（ &nbsp; &nbsp;）。&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "48b165641af242ed93604cda66f7666f",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;消防员&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "72090a7127bf4972881edd3a21af1d27",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;轨道列车司机&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6b0a9bce2ffc48b7912c4e3058edd207",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;所有类型焊工&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "62a64b9d26da48b9935def54a91f0e42",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;安检员&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68528",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;失业人员在领取失业保险金期间死亡的，向其遗属支付的待遇包括( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "2aa1706f21784b8885cc41e31bb059bb",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;一次性丧葬补助金&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5ef801cd79bc4d928d4b3cc56bbd2d19",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;定期未成年子女抚养费&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "e3c23011153e4457a4f9c183c0bec252",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;一次性医疗补助费&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "4d66802b4a8a4b7e84a03e159e1fa422",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;定期抚恤金&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68541",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人跨地区就业且按照有关规定办理入职手续后，其档案在有人事档案管理权限的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）之间可直接办理转递手续。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "0c06afad44ee45ae98113f227ba74045",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;机关&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "f8976f434bce474984f8cd5bbd598a0f",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国有&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;企业&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "c93a2cb4c954447cb69802e5a056d48b",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;事业单位&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "2089492fd65d433c85b1c689cbfcf166",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;流动人员人事档案管理服务机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68517",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工因工致残被鉴定为一级至四级伤残的，从工伤保险基金按月支付伤残津贴，标准分别为本人工资的&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "4ad36097099f474b8f9a55df9cf3ed99",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;95%&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;85%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "096353dd8b51434688203f4a079c1369",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;85%&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;75%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;70%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a3c4175ba22044348a7a235e2ec951ba",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;85%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;75%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "92fda3478d794b239735125803979e2c",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;95%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;；&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;85%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68525",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;不属于停止享受工伤保险待遇的情形是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "f0364f84882c4366ad4074cafa64be1f",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;治疗完成后旧伤复发的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "7c0a07dfee454567ae4b178648e3d980",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;拒绝治疗的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5defa010376047538c17d8f647754786",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;丧失享受待遇条件的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6d2e73ecfb8742a6a5a310c4f574c3a8",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;拒不接受劳动能力鉴定的&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68531",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;各省在确定全口径城镇单位就业人员平均工资时，应当考虑（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "04b3ec938c5b4d5480c9e4ea81214026",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;行业工资指导线&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "8d7e39bbbd274e2db0feeed2954a0918",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年均在岗职工工资增长率&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a077df3f05824664904ecc6e9f1f279c",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;城镇私营单位就业人员平均工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "715d7df77d2d4d7ebcbb3998d8195ff2",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;城镇非私营单位就业人员平均工资&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68529",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老王&amp;2526lt;/span&amp;2526gt;2015&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月在&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;A&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司工作，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2017&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;10&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月失业。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2018&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月重新在&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;B&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;公司工作，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;2&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月又再次失业。在&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;A&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;、&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;B&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;两家企业工作期间一直正常参保缴费。上次失业时的失业保险金还没有领取。老王最多可以领取（ &nbsp;）的失业保险金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "d100d3ab1f32427cbeda96b006aeac1e",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "c3d348adbe774aa1b6bebfd040cb6323",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;24&amp;2526lt;span&amp;2526gt;个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5fa08f19e3774b3fb0d9818cd6ac42c0",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;18&amp;2526lt;span&amp;2526gt;个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6ffa1af0798a4c21827b3692210fb760",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;6&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68512",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;《关于失业保险支持企业稳定就业岗位的通知》规定，对面临暂时性生产经营困难且恢复有望、坚持不裁员少裁员的参保企业，稳岗返还标准可按（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）确定。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "3eac5248ac5b4fadbb6abbbe9125197f",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月的企业及其职工应缴纳社会保险费50%的标准确定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "f4102887059a4171b7389aef53a2e179",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月的当地月人均失业保险金和参保职工人数确定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "11f6bef73f9f4939a54cc6011307b393",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月的当地月人均失业保险金和参保职工人数确定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "9e2973e02e174a3cbb56bacaf52bb20a",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;3个月的企业及其职工应缴纳社会保险费50%的标准确定&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68526",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;张某于&amp;2526lt;/span&amp;2526gt;2019&amp;2526lt;span&amp;2526gt;年&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;1&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日抢险救灾时下落不明，其工资应照发至（ &nbsp;&nbsp;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "f632024c2d8948299d4cc78b7c40d984",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "2b30e3207f4b40aa9705852175b391d5",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "d7c88dbd92c3423b81596bf6f44ef0b8",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "52e049578ca9487fba2a5b47a0fbf1df",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5&amp;2526lt;span&amp;2526gt;月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;日&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68516",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;某统筹地区上年度职工月平均工资为&amp;2526lt;/span&amp;2526gt;2000&amp;2526lt;span&amp;2526gt;元。工伤职工张某属于生活部分不能自理，其生活护理费应当是（ &nbsp;&nbsp;&nbsp;）元。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "5894d3f911024044aa40ea8db9f4d672",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;400&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5bd4ea65a7194154b603716ea2dfe185",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;600&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "97542fb114f044eab4f3847dc779588e",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;1000&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "718692167aae453e83eaaf52b21a44fb",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;800&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68533",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;职工失业期间，关于其企业年金个人账户，错误的是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "625aa4e9ef7648e09d14ce3320172306",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;转入新就业单位的企业年金或者职业年金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "a5be56cd5559413e8d22bc7d1e089177",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人账户资金可一次性领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "17d00442fcbe4f61a1e241628642c57f",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可由原管理机构继续管理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "28bfa9af19f340a1afdf23ad8b330bc9",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;可由&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;法人&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;受托&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;发起的集合计划&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;设置的保留账户暂时&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;管理&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68521",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《职业年金基金管理暂行办法》，职业年金代理人是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "c334bb810dd048668d91b885dd603c99",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;省级社会保险经办机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "cb3ebc3996144a0ebe96ab18fbf2e7f1",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;法人受托机构&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "49f7ab238d4c46599332796f8282a9ab",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;商业银行&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "975b9c2d81e14d89b383524c3e8ce069",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;中央&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;国家机关养老保险管理中心&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68534",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;参保人员养老保险关系在企业职工基本养老保险和城乡居民基本养老保险转移时，说法错误的是&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "91a69f29627342fe9cbd2b3f80f08442",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;从企业职工基本养老保险转入城乡居民养老保险，转移全部个人账户储存额和&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;12%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;统筹基金&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "24524877cbb342178914dcc251fdee89",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;首先需要按照企业职工养老保险有关规定确定待遇领取地&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "6a299999eafa4ab4948174f5f64156ae",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;从城乡居民养老保险转入企业职工基本养老保险，城乡居民养老保险缴费年限可以折算为企业职工基本养老保险缴费年限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "5790a27017f94e5688e7033669ac71ad",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;同一年度内同时参加了企业职工基本保险和城乡居民养老保险的，可以协商保留其中一个缴费关系和相应缴费年限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68530",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;我国失业保险基金的来源包括&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "fa37ce06f31e4cfc916a129b7640c0ac",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;失业保险基金的利息&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "114faec03d914c4b935cd06f96272361",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;社会非商业性捐赠款项&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "8db35b6132134bfc8cc239371661eb4d",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;基金投资运营收入&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "4713535ad2494161b7335a587b0ab9fb",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;失业保险费&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;、财政补贴&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68544",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;失业人员可在&amp;2526lt;/span&amp;2526gt;( &nbsp;&nbsp;&nbsp;)&amp;2526lt;span&amp;2526gt;公共就业服务机构办理失业登记。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "a2ce9db2e83f476e8495e0716e76d1dd",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;户籍地&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "1755d36383c3414fb8f655913ad73a45",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;出生地&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "68a97449dcb44919a51a8ae04c19045d",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;单位注册地&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "444a5d32a51b4840a0278b59038949a7",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;常住地&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}, {
				"id": "68539",
				"type": "001007",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;属于设立人才中介服务机构应具备条件的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "808a81e004c34aad8f7537f050330346",
					"sort": 1,
					"code": "A",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;有&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;4&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;名以上大专以上学历、取得人才中介服务资格证书的专职工作人员&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "0b5862444de349588e2a0bd3eab4c0ac",
					"sort": 2,
					"code": "B",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;有独立承担民事责任的能力&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "d878d3c3b60640e794697d5f33f5b1e0",
					"sort": 3,
					"code": "C",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;有与开展人才中介业务相适应的场所、设施&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}, {
					"id": "100c4e145b4148f598a5e568e779e964",
					"sort": 4,
					"code": "D",
					"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;有健全可行的工作章程和制度&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"
				}],
				"keywords": "null"
			}]
		}, {
			"type": "001003",
			"score": 2.0,
			"totalScores": 22.0,
			"totalNumbers": 11,
			"description": "null",
			"questions": [{
				"id": "68472",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年4月15日至年底，符合条件的个人最高可申请创业担保贷款额度为20万元。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "7057ce627e804a8a85db45693673fa32",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "586a92fae1e14b37877007f0f9bfd9fb",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68465",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;城乡居民养老保险个人账户养老金的月计发标准，为&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人缴费和政府补贴额&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;除以&amp;2526lt;/span&amp;2526gt;139。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "ef0fbaed8aed4b4ca26e0e6d3659e32f",
					"sort": 1,
					"code": "A",
					"content": "错误"
				}, {
					"id": "b589f6b3e5c644f8b2ecb29210593a94",
					"sort": 2,
					"code": "B",
					"content": "正确"
				}],
				"keywords": "null"
			}, {
				"id": "68470",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;参保人员辞职离开机关的，根据改革前本人在机关工作的年限长短补记职业年金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "faeb0315eb574a65a23d66d3cca5a019",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "f97920139e2a4231a59c495796f592fb",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68471",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个人求职，应当如实提供本人基本信息、家庭情况以及与应聘岗位相关的知识、技能、工作经历等情况。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "f4985e96a80543aaac3fff6cdb184037",
					"sort": 1,
					"code": "A",
					"content": "错误"
				}, {
					"id": "ebf317d014324536a18e42c1f3cd69e8",
					"sort": 2,
					"code": "B",
					"content": "正确"
				}],
				"keywords": "null"
			}, {
				"id": "68463",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年度调整退休人员基本养老金时，全国总体调整比例按照2019年退休人员月人均基本养老金的5%确定。各省以全国总体调整比例为高限确定本省调整比例和水平。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "e698f04dfc464d1c84e0ad62ab193a8d",
					"sort": 1,
					"code": "A",
					"content": "错误"
				}, {
					"id": "b67c1e0d9918443b87bc7930c2ec7f1c",
					"sort": 2,
					"code": "B",
					"content": "正确"
				}],
				"keywords": "null"
			}, {
				"id": "68467",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位违反规定拒不协助社会保险行政部门对工伤事故进行调查核实的，社会保险行政部门责令改正，并处一定数额的罚款。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "cbf4d256fce645d693d6607e71523644",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "9aa88cb512b648e197a0b6ca8aaa65c7",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68466",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照《工伤保险条例》规定，丧葬补助金为&amp;2526lt;/span&amp;2526gt;6个月统筹地区上年度职工月平均工资。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "6d1a4135c12e4ef38e1aea5478bf60a8",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "058171a441cd4816941bf2462983e967",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68462",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照社会保险基金会计制度，支出户存款科目核算社会保险基金按规定存入支出户的款项。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "f647daf703ae4965a3580cfb9318a8cb",
					"sort": 1,
					"code": "A",
					"content": "错误"
				}, {
					"id": "a25dc7838399466ebc9315c7b6453599",
					"sort": 2,
					"code": "B",
					"content": "正确"
				}],
				"keywords": "null"
			}, {
				"id": "68464",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;为实现贫困人员城乡居民基本养老保险应保尽保，纳入城乡居民基本养老保险制度且已经按规定发放城乡居民养老保险待遇的贫困老人，其待遇支付终身。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "b040897c1bbe41ee85cdd60eacfef63e",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "0eaad4179f9544f08fe23a3d5f91e1b1",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68469",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;用人单位未按规定申报应当缴纳的社保费数额的，按照该单位上月缴费额的&amp;2526lt;/span&amp;2526gt;110%确定应当缴纳数额。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "bd8587d2ea7d488bb7d7a8a810d7ddc6",
					"sort": 1,
					"code": "A",
					"content": "正确"
				}, {
					"id": "0bfdd3e170a34ffd88a500292ce6a303",
					"sort": 2,
					"code": "B",
					"content": "错误"
				}],
				"keywords": "null"
			}, {
				"id": "68468",
				"type": "001003",
				"level": "003001",
				"content": "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;某省份在岗职工月平均工资标准为&amp;2526lt;/span&amp;2526gt;1000元，其可以将失业保险金月标准提高900元。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;",
				"answer": "null",
				"analysis": "null",
				"score": 2.0,
				"userAnswer": "null",
				"blanksNumber": "null",
				"signed": 0,
				"checkResult": "null",
				"userScore": "null",
				"tag": "008001",
				"chapterName": "null",
				"inCollection": 0,
				"choices": [{
					"id": "8b2f49b37a5542b5bf0bfeef83de36d7",
					"sort": 1,
					"code": "A",
					"content": "错误"
				}, {
					"id": "5ea892b1d2af4b23b860684af657c671",
					"sort": 2,
					"code": "B",
					"content": "正确"
				}],
				"keywords": "null"
			}]
		}]
	},
	"code": "SUCCESS"
}

j = {"httpStatus":"OK","status":0,"message":"成功","data":{"name":"周周练考试","duration":45,"recordId":"6813c31ef80149119a7b2c43c076505d","conclusions":"谢谢","description":"null","totalScore":30.0,"passScore":18.0,"examinationScore":29.0,"totalExaminationUserNumbers":0,"currentUserScoreRanking":1,"questionTypeSummaries":[{"type":"001001","score":1.0,"totalScores":12.0,"totalNumbers":12,"description":"单选题","questions":[{"id":"66322","type":"001001","level":"003001","content":"\n《人力资源和社会保障事业发展“十三五”规划纲要》提出，到“十三五”期末，高、中、初级专业技术人才比例达到(    )。\n","answer":"A","analysis":"解析《人力资源和社会保障事业发展“十三五”规划纲要》提出，到“十三五”期末，高、中、初级专业技术人才比例达到10：40：50。    解析：《人力资源和社会保障事业发展“十三五”规划纲要》第三章第三节提出：职工和城乡居民基本医疗保险政策范围内住院费用支付比例稳定在75%左右。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f4f7b4343a9947afb38a9f9c4cbb003f","sort":1,"code":"A","content":"10:40:50"},{"id":"6af6bc914a574ef8b0401870b1b8c01b","sort":2,"code":"B","content":"20:30:40"},{"id":"15e50fef61084d83b0429bc93ffcec40","sort":3,"code":"C","content":"30:20:50"},{"id":"50b39d1678d94c21984f8a5ec74b3cab","sort":4,"code":"D","content":"30:30:40"}],"keywords":"null"},{"id":"65773","type":"001001","level":"003001","content":" 依据《中华人民共和国社会保险法》，养老保险个人账户因个人死亡的，个人账户余额(    )。","answer":"D","analysis":"解析：《中华人民共和国社会保险法》第二章第十四条规定，养老保险个人账户不得提前支取，记账利率不得低于银行定期存款利率，免征利息税。个人死亡的，个人账户余额可以继承。","score":1.0,"userAnswer":"D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"569f9286ccca4521b0e540ceae56a74b","sort":1,"code":"A","content":"纳入养老保险基金"},{"id":"b5b7c2317b2c48baaa4284f447b949e7","sort":2,"code":"B","content":"可以部分继承"},{"id":"868bbd3e602c4069aa1cc3d4717d31a2","sort":3,"code":"C","content":"不可以继承"},{"id":"b1469b2d058648dc9427dad660b065ea","sort":4,"code":"D","content":"可以继承"}],"keywords":"null"},{"id":"65610","type":"001001","level":"003001","content":"\n《关于切实做好社会保险扶贫工作的意见》规定，对(    )等困难群体，参加城乡居民基本养老保险的，地方人民政府为其代缴部分或全部最低标准养老保险费。\n","answer":"C","analysis":"《人力资源社会保障部财政部国务院扶贫办关于切实做好社会保险扶贫工作的意见》（人社部发〔2017〕59号）规定，对建档立卡未标注脱贫的贫困人口、低保对象、特困人员等困难群体，参加城乡居民基本养老保险的，地方人民政府为其代缴部分或全部最低标准养老保险费。","score":1.0,"userAnswer":"C","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"01fd096f47de415fa71d75af3e46f449","sort":1,"code":"A","content":"建档立卡未标注脱贫的贫困人口、优抚对象、特困人员"},{"id":"bb3b6e5c774248de8873afb132d211d6","sort":2,"code":"B","content":"优抚对象、建档立卡人口、低保对象"},{"id":"6283f305de064710b9b4f51d294daf01","sort":3,"code":"C","content":"建档立卡未标注脱贫的贫困人口、低保对象、特困人员"},{"id":"b33992a1a7304d5cb9a16b33813a2a30","sort":4,"code":"D","content":"建档立卡贫困人口、低保对象、特困人员"}],"keywords":"null"},{"id":"65170","type":"001001","level":"003001","content":"\n档案管理服务机构在接收流动人员人事档案时，对于缺少非关键材料的，下列做法正确的是(    )。","answer":"B","analysis":"根据《人力资源社会保障部办公厅关于简化优化流动人员人事档案管理服务的通知》中第四点实行档案接收告知承诺制中“对缺少非关键材料的，采取先存后补方式予以接收”可知，答案为B。","score":1.0,"userAnswer":"B","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"175e62bedd6e4e98be3b208e5a4c3d5b","sort":1,"code":"A","content":"直接接收"},{"id":"9335f953d76c44d58128374f2f961576","sort":2,"code":"B","content":"先存后补方式接收"},{"id":"4517b39f14c64e2b91c25838de317e95","sort":3,"code":"C","content":"补充材料"},{"id":"27de18eb02594b8f8fa8616cd8918aca","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"65190","type":"001001","level":"003001","content":"\n人事档案中重点审核的“三龄”不包括以下哪项？(    )","answer":"A","analysis":"根据《干部人事档案工作条例》第三十六条“干部人事档案审核应当在全面审核档案内容的基础上，重点审核干部的出生日期、参加工作时间、入党时间、学历学位、工作经历、干部身份、家庭主要成员及重要社会关系、专业技术职务（职称）、学术评鉴、奖惩等基本信息，审核档案内容是否真实、档案材料是否齐全、档案材料记载内容之间的关联性是否合理以及是否有影响干部使用的情形等”，可知答案为D．。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8256a7ae03d34b3c90bcef353b3bcb3a","sort":1,"code":"A","content":"学龄"},{"id":"ef98450ad9c742e5b195e9fe13a803df","sort":2,"code":"B","content":"党龄"},{"id":"fda6edf045cb45208769f71907ee328a","sort":3,"code":"C","content":"工龄"},{"id":"d37a941a33144f1fba2376329f907c88","sort":4,"code":"D","content":"年龄"}],"keywords":"null"},{"id":"65962","type":"001001","level":"003001","content":"\n根据《劳动人事争议仲裁办案规则》，当事人撤回仲裁审查申请或者仲裁委员会决定不予制作调解书的，应当(    )仲裁审查。\n","answer":"D","analysis":"根据《劳动人事争议仲裁办案规则》第七十九条规定，当事人撤回仲裁审查申请或者仲裁委员会决定不予制作调解书的，应当终止仲裁审查。","score":1.0,"userAnswer":"D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e907e1672b2b4dbf8bfe535d364fc034","sort":1,"code":"A","content":"中止"},{"id":"738a0f98cdab43fe805a254ab164ddba","sort":2,"code":"B","content":"继续"},{"id":"45ecd8fb910c46c0bfddd593e1b1efc7","sort":3,"code":"C","content":"结束"},{"id":"9d76dfe6533e47b891092ffe29c825e1","sort":4,"code":"D","content":"终止"}],"keywords":"null"},{"id":"65150","type":"001001","level":"003001","content":"\n《人力资源市场暂行条例》规定，(    )以上地方人民政府人力资源社会保障行政部门负责本行政区域人力资源市场的管理工作。","answer":"D","analysis":"《人力资源市场暂行条例》第四条规定，县级以上地方人民政府人力资源社会保障行政部门负责本行政区域人力资源市场的管理工作。","score":1.0,"userAnswer":"D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c68bf083e31f4400b6781976c3dfc6b2","sort":1,"code":"A","content":"省级"},{"id":"b411a8a249664517a7bc96e277b873e7","sort":2,"code":"B","content":"乡镇级"},{"id":"0814490df1064f4d8617c2ef9525fc8f","sort":3,"code":"C","content":"市级"},{"id":"3a83bfa636e447c593a5fabd8efe43db","sort":4,"code":"D","content":"县级"}],"keywords":"null"},{"id":"65893","type":"001001","level":"003001","content":"&amp;2526lt;p&amp;2526gt;劳动者可以随时解除劳动合同的法定情形是( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"C","analysis":"&amp;2526lt;p&amp;2526gt;《劳动合同法》第三十八条规定：用人单位有下列情形之一的，劳动者可以解除劳动合同：\n（一）未按照劳动合同约定提供劳动保护或者劳动条件的；\n（二）未及时足额支付劳动报酬的；\n（三）未依法为劳动者缴纳社会保险费的；\n（四）用人单位的规章制度违反法律、法规的规定，损害劳动者权益的；\n（五）因本法第二十六条第一款规定的情形致使劳动合同无效的；\n（六）法律、行政法规规定劳动者可以解除劳动合同的其他情形。&amp;2526lt;/p&amp;2526gt;","score":1.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":0,"userScore":"0.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"17e5dc974bb0449a872529097794dd36","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;用人单位变更投资人&amp;2526lt;/p&amp;2526gt;"},{"id":"130465789ed040bfa22c5018440b3c83","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;用人单位发生合并或者分立&amp;2526lt;/p&amp;2526gt;"},{"id":"0844683e48df4d0c80fb923fc3181bff","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;用人单位未依法为劳动者缴纳社会保险费&amp;2526lt;/p&amp;2526gt;"},{"id":"fc03b303849d4f61b7a632fee7fd9caf","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;用人单位变更名称、法定代表人、主要负责人&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"65169","type":"001001","level":"003001","content":"\n自(    )起，取消人力资源社会保障等部门所属公共就业和人才服务机构的人才集体户口管理服务费（包括经营服务性质的收费）。","answer":"A","analysis":"根据《人力资源社会保障部办公厅国家发展改革委办公厅公安部办公厅财政部办公厅关于做好人才集体户口管理服务工作的通知》中“根据《财政部国家发展改革委关于取消和暂停征收一批行政事业性性收费有关问题的通知》（财税[2015]102号）规定，自2016年1月1日起，取消人力资源社会保障等部门所属公共就业和人才服务机构的人才集体户口管理服务费（包括经营服务性质的收费）”可知，答案为B。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"7ef56b2f009246e69afb24d7aa568cbf","sort":1,"code":"A","content":"2016年1月1日"},{"id":"8e36c3591b854db0a92c1d0cfb125cb6","sort":2,"code":"B","content":"2015年12月1日"},{"id":"16bd0b4570eb4ca6b7bf624d405c3570","sort":3,"code":"C","content":"2016年5月1日"},{"id":"322e8a105dce46ad8ff643dddfa861a4","sort":4,"code":"D","content":"2015年1月1日"}],"keywords":"null"},{"id":"66050","type":"001001","level":"003001","content":" 根据《中国人民解放军文职人员条例》，不属于中国人民解放军文职人员基本条件的是（    ）。","answer":"A","analysis":"解析：《中国人民解放军文职人员条例》第九条规定：文职人员应当具备下列基本条件：（一）具有中华人民共和国国籍；（二）年满18周岁；（三）符合军队招录聘用文职人员的政治条件；（四）符合岗位要求的资格条件；（五）身体和心理健康；（六）法律、法规规定的其他条件。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9003fcd877a042df95755790637b3ae4","sort":1,"code":"A","content":"年满16周岁"},{"id":"5b9c5091a56d425396be5b9eb1f9c179","sort":2,"code":"B","content":"具有中华人民共和国国籍"},{"id":"5b41006af2f6403881aad1056998b81b","sort":3,"code":"C","content":"符合军队招录聘用文职人员的政治条件"},{"id":"51d798df5a6f4ff29d8cc6edefb13d92","sort":4,"code":"D","content":"符合岗位要求的资格条件"}],"keywords":"null"},{"id":"66392","type":"001001","level":"003001","content":"\n社会保障卡在养老保险工作中的主要业务应用包括：养老待遇申领、(    )、待遇领取资格自助认证、享受各项养老保险服务、查询社保权益信息、打印参保证明等。\n","answer":"B","analysis":"《人力资源社会保障部办公厅关于在养老保险工作中全面推进社会保障卡应用的通知》（人社厅发〔2019〕13号）规定，要使社保卡成为参保人员办理退休审核、养老保险待遇申领、待遇领取资格自助认证和享受各项养老保险服务的主要凭证，实现卡证合一、持卡办事。发展自助服务，通过自助一体机等设备读卡确定个人身份后，提供查询社保权益信息、打印参保证明等服务。","score":1.0,"userAnswer":"B","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9655b807e1a04afaab6150d409bd3b3b","sort":1,"code":"A","content":"持卡办事"},{"id":"5d2d08d5c05b4bf28f1a6ac20ebf6aed","sort":2,"code":"B","content":"退休审核"},{"id":"0592bba6d88a485c9ea4ea8f70b039fc","sort":3,"code":"C","content":"就医凭证"},{"id":"545b6b24d4734c97bb051808f536fb06","sort":4,"code":"D","content":"金融服务"}],"keywords":"null"},{"id":"65968","type":"001001","level":"003001","content":"\n根据《企业劳动争议协商调解规定》，(    )企业应当依法设立调解委员会，并配备专职或者兼职工作人员。\n","answer":"B","analysis":"根据《企业劳动争议协商调解规定》第十三条规定，大中型企业应当依法设立调解委员会，并配备专职或者兼职工作人员","score":1.0,"userAnswer":"B","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3d5196151f9e4fbba1d3e512c6eeb97a","sort":1,"code":"A","content":"中小型"},{"id":"eacf84c3618849ed857e44e975c516f0","sort":2,"code":"B","content":"大中型"},{"id":"4c0dbd8f5bd54f9697ddad635839ef9f","sort":3,"code":"C","content":"小型"},{"id":"79324acc617c4455a389630910ea4f13","sort":4,"code":"D","content":"小微型"}],"keywords":"null"}]},{"type":"001002","score":1.0,"totalScores":8.0,"totalNumbers":8,"description":"多选题","questions":[{"id":"66910","type":"001002","level":"003001","content":"&nbsp;\n根据《关于解决部分退役士兵社会保险问题的意见》，说法正确的是（    ）","answer":"A,C,D","analysis":"中共中央办公厅 国务院办公厅印发的《关于解决部分退役士兵社会保险问题的意见》规定：退役士兵参加社会保险缴纳费用，原则上单位缴费部分由所在单位负担，个人缴费部分由个人负担。城镇职工基本养老保险，缴费工资基数由安置地按照补缴时上年度职工平均工资的60%予以确定，单位缴费费率也按补缴时安置地规定执行。故ABC表述正确。\n中共中央办公厅 国务院办公厅印发的《关于解决部分退役士兵社会保险问题的意见》规定：达到法定退休年龄、基本养老保险累计缴费年限（含军龄）未达到国家规定的最低缴费年限的，允许延长缴费至最低缴费年限；2011年7月1日《中华人民共和国社会保险法》实施前首次参保、延长缴费5年后仍不足最低缴费年限的，允许一次性缴费至最低缴费年限。故D表述不正确。","score":1.0,"userAnswer":"A,C,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64638cabac8d43a3b68db54ea8028a97","sort":1,"code":"A","content":"补缴基本养老保险，单位缴费费率按补缴时安置地规定执行"},{"id":"3e1e3b33d0cb450f859d1ab517ba1924","sort":2,"code":"B","content":"达到法定退休年龄、基本养老保险累计缴费年限（含军龄）未达到国家规定最低缴费年限的，允许一次性缴费至最低缴费年限"},{"id":"cdf82a68cd534457b92c455cc85b7825","sort":3,"code":"C","content":"退役士兵参加社会保险缴纳费用，原则上单位缴费部分由所在单位负担，个人缴费部分由个人承担"},{"id":"5d8b40b86eef463983fb933a1a64d5ff","sort":4,"code":"D","content":"补缴基本养老保险，缴费工资基数由安置地按照上年度职工平均工资的60%确定"}],"keywords":"null"},{"id":"66749","type":"001002","level":"003001","content":"\n《就业促进法》规定，从事职业中介活动，应当遵循（    ）的原则。","answer":"A,B,C,D","analysis":"《就业促进法》第三十九条规定，从事职业中介活动，应当遵循合法、诚实信用、公平、公开的原则。","score":1.0,"userAnswer":"A,B,C,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6feea7cc4e374715a4b2287f69f7ac42","sort":1,"code":"A","content":"公开"},{"id":"8496e65e888144058da95fb6c6ca6efc","sort":2,"code":"B","content":"诚实信用"},{"id":"4e0eb8b9713146db92a0c8c05b936e03","sort":3,"code":"C","content":"合法"},{"id":"2fb1ed07baf1445799f3fde1e6f2e585","sort":4,"code":"D","content":"公平"}],"keywords":"null"},{"id":"66673","type":"001002","level":"003001","content":"\n地方各级人民政府、政府统计机构和有关部门以及各单位的负责人不得（    ）。\n","answer":"A,B,C","analysis":"《中华人民共和国统计法》第六条规定，地方各级人民政府、政府统计机构和有关部门以及各单位的负责人，不得自行修改统计机构和统计人员依法搜集、整理的统计资料，不得以任何方式要求统计机构、统计人员及其他机构、人员伪造、篡改统计资料，不得对依法履行职责或者拒绝、抵制统计违法行为的统计人员打击报复。","score":1.0,"userAnswer":"A,B,C","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cce4ebec41104ce586116b51b75dd501","sort":1,"code":"A","content":"对依法履行职责或者拒绝、抵制统计违法行为的统计人员打击报复"},{"id":"0cf625db0c8b442b9aca11474de7ae8a","sort":2,"code":"B","content":"以任何方式要求统计机构、统计人员及其他机构、人员伪造、篡改统计资料"},{"id":"e856925676cd44de8bdd46c9569509c1","sort":3,"code":"C","content":"自行修改统计机构和统计人员依法搜集、整理的统计资料"},{"id":"48c8d429a0824d49a3d0ab0460052693","sort":4,"code":"D","content":"对本部门、本地方、本单位执行统计法的情况进行监督"}],"keywords":"null"},{"id":"66622","type":"001002","level":"003001","content":"\n《事业单位工作人员奖励规定》规定，事业单位工作人员集体是指（    ）。\n","answer":"A,B,C,D","analysis":"《事业单位工作人员奖励规定》第二条规定，事业单位工作人员、事业单位工作人员集体可依据本规定给予奖励，其中，事业单位工作人员集体是指事业单位法人组织、内设机构、派出机构或者为完成专项任务组成的工作团队。","score":1.0,"userAnswer":"A,B,C,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1b646e4cb91e4b128c2938c94478a214","sort":1,"code":"A","content":"为完成专项任务组成的工作团队"},{"id":"03c4f0e2b48541cab3d3a9c8473064eb","sort":2,"code":"B","content":"事业单位法人组织"},{"id":"31e360c32e9a4356a5f8b34130d5ef8f","sort":3,"code":"C","content":"事业单位内设机构"},{"id":"9ff5d3523bf045cc8e0b8094987a592c","sort":4,"code":"D","content":"事业单位派出机构"}],"keywords":"null"},{"id":"66514","type":"001002","level":"003001","content":"\n下列表述中正确的有（    ）\n","answer":"B,C,D","analysis":"根据《劳动人事争议仲裁组织规则》第八条规定，仲裁委员会应当每年至少召开两次全体会议，研究本仲裁委员会职责履行情况和重要工作事项。仲裁委员会主任或者三分之一以上的仲裁委员会组成人员提议召开仲裁委员会会议的，应当召开。仲裁委员会的决定实行少数服从多数原则。","score":1.0,"userAnswer":"B,C,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e9dc7eca4864432c97d106057104110d","sort":1,"code":"A","content":"仲裁委员会应当每年至少召开一次全体会议，研究本仲裁委员会职责履行情况和重要工作事项"},{"id":"fc5a5ece216141b79a2fc3089dbbffb6","sort":2,"code":"B","content":"仲裁委员会的决定实行少数服从多数原则"},{"id":"9b3b898800c644ecba822beda556bda8","sort":3,"code":"C","content":"仲裁委员会主任提议召开仲裁委员会会议的，应当召开"},{"id":"70cedc40a68d4835994dbab6fff95943","sort":4,"code":"D","content":"三分之一以上的仲裁委员会组成人员提议召开仲裁委员会会议的，应当召开"}],"keywords":"null"},{"id":"66888","type":"001002","level":"003001","content":"&nbsp;\n在中国境内就业的外国人，是指依法获得（    ）等就业证件和外国人居留证件，以及持有《外国人永久居留证》，在中国境内合法就业的非中国国籍的人员。","answer":"B,C,D","analysis":"《在中国境内就业的外国人参加社会保险暂行办法》（人力资源和社会保障部令第16号）规定，在中国境内就业的外国人，是指依法获得《外国人就业证》、《外国专家证》、《外国常驻记者证》等就业证件和外国人居留证件，以及持有《外国人永久居留证》，在中国境内合法就业的非中国国籍的人员。","score":1.0,"userAnswer":"B,C,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f539de618a894b74829e363f3d8e1633","sort":1,"code":"A","content":"《外国人中国签证》"},{"id":"0ad3f009b5174f42945712c2f670056e","sort":2,"code":"B","content":"《外国人就业证》"},{"id":"afa768d5811448bf819d2ff1edab4aaf","sort":3,"code":"C","content":"《外国专家证》"},{"id":"5885161da6264016bc27f97f626e1270","sort":4,"code":"D","content":"《外国常驻记者证》"}],"keywords":"null"},{"id":"66951","type":"001002","level":"003001","content":"\n职工与用人单位发生工伤保险争议的，可以依照相关规定，采取（    ）方式解决。","answer":"A,B,D","analysis":"《实施<中华人民共和国社会保险法>若干规定》的规定，职工与用人单位发生社会保险争议的，可以依照《中华人民共和国劳动争议调解仲裁法》、《劳动人事争议仲裁办案规则》的规定，申请调解、仲裁，提起诉讼。","score":1.0,"userAnswer":"A,B,D","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4289688e06e14b34bf32683020197b85","sort":1,"code":"A","content":"诉讼"},{"id":"4d7d50472b544ee2be5b5234b12152f1","sort":2,"code":"B","content":"调解"},{"id":"68d5474f4f544f918fe229eabc18b489","sort":3,"code":"C","content":"上访"},{"id":"49c40505deda4c05bc5f0f7f7abd396d","sort":4,"code":"D","content":"仲裁"}],"keywords":"null"},{"id":"66504","type":"001002","level":"003001","content":"\n根据《劳动人事争议仲裁办案规则》，表述错误的是（    ）。\n","answer":"B,C","analysis":"根据《劳动人事争议仲裁办案规则》第三十八条规定，仲裁庭应当在开庭五日前，将开庭日期、地点书面通知双方当事人。当事人有正当理由的，可以在开庭三日前请求延期开庭。是否延期，由仲裁委员会根据实际情况决定。","score":1.0,"userAnswer":"B,C","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7bc86baaa67494bb3c7373df176a089","sort":1,"code":"A","content":"是否延期，由仲裁委员会根据实际情况决定"},{"id":"9a359107589a474990a7906e7fdffbd9","sort":2,"code":"B","content":"仲裁庭应当在开庭十日前，将地点书面通知双方当事人"},{"id":"ecdb74cf3fa64963b208a72ffdcff08e","sort":3,"code":"C","content":"当事人任何情况下都可以在开庭三日前请求延期开庭"},{"id":"8893768f647c42be81c9a1afec71d08a","sort":4,"code":"D","content":"仲裁庭应当在开庭五日前，将开庭日期书面通知双方当事人"}],"keywords":"null"}]},{"type":"001003","score":1.0,"totalScores":4.0,"totalNumbers":4,"description":"判断题","questions":[{"id":"67826","type":"001003","level":"003001","content":"\n民生持续改善能为经济发展创造更多有效需求，为推进供给侧结构性改革提供强大内生动力。（    ）","answer":"A","analysis":"《国务院关于印发“十三五”推进基本公共服务均等化规划的通知》要求，民生持续改善能为经济发展创造更多有效需求，为推进供给侧结构性改革提供强大内生动力。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5666c8c612784db3986f09240c007041","sort":1,"code":"A","content":"正确"},{"id":"233e15702a524b8380d91844a1445da0","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"67414","type":"001003","level":"003001","content":"\n用人单位招聘劳动者，不得将妊娠测试作为入职体检项目。（    ）","answer":"A","analysis":"人力资源社会保障部 教育部等九部门《关于进一步规范招聘行为促进妇女就业的通知》\n（人社部发〔2019〕17号）规定，用人单位招聘劳动者，不得将妊娠测试作为入职体检项目。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5d6b34bb10f74b8cae5f910949a18ba6","sort":1,"code":"A","content":"正确"},{"id":"4c59a05f44f147578544c2497da73d1a","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"67748","type":"001003","level":"003001","content":"\n研究工作可以在国外，也可长期或短期回国内进行，国家鼓励留学人员与国内企事业单位合作，在国内或国外建立合作研究开发基地。（    ）","answer":"A","analysis":"《人事部教育部科技部公安部财政部关于印发〈关于鼓励海外留学人员以多种形式为国服务的若干意见〉的通知》（人发〔2001〕49号）规定，研究工作可以在国外，也可长期或短期回国内进行，国家鼓励留学人员与国内企事业单位合作，在国内或国外建立合作研究开发基地。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fca444e54c1c4fd09954bc73ad264fa7","sort":1,"code":"A","content":"正确"},{"id":"7ec377001e084d87b557ffc615c35be4","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"67446","type":"001003","level":"003001","content":"\n申请设立中外合资人才中介机构的中方投资者应当是成立3年以上的人才中介机构，外方出资者也应当是从事3年以上人才中介服务的外国公司、企业和其他经济组织。","answer":"A","analysis":"《外商投资人才中介机构管理暂行规定》已取消了申请设立中外合资人才中介机构投资各方从业年限的限制。","score":1.0,"userAnswer":"A","blanksNumber":"null","signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ba8dd2f7d2894299a36dfbdcc3ccaf3c","sort":1,"code":"A","content":"错误"},{"id":"4d27f879f6004b148d6dae4fe89eb286","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]},{"type":"001004","score":1.0,"totalScores":6.0,"totalNumbers":6,"description":"null","questions":[{"id":"67962","type":"001004","level":"003001","content":"\n对同一职业（工种）同一技能等级通过初次职业技能鉴定并取得证书（不含培训合格证书）的参训人员，（    ）。","answer":"给予职业技能鉴定补贴","analysis":"《人力资源社会保障部办公厅财政部办公厅关于做好职业技能提升行动专账资金使用管理工作的通知》明确，对同一职业（工种）同一技能等级通过初次职业技能鉴定并取得证书（不含培训合格证书）的参训人员，给予职业技能鉴定补贴。","score":1.0,"userAnswer":"给予职业技能鉴定补贴","blanksNumber":1,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"},{"id":"67867","type":"001004","level":"003001","content":"（  ）是中国特色社会主义最本质的特征。","answer":"中国共产党领导","analysis":"中国共产党领导是中国特色社会主义最本质的特征。（《习近平新时代中国特色社会主义思想三十讲》）","score":1.0,"userAnswer":"中国共产党领导","blanksNumber":1,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"},{"id":"67917","type":"001004","level":"003001","content":"&amp;2526lt;p&amp;2526gt;加快推进流动人员人事档案信息化建设的总体原则是数据（ &nbsp; &nbsp;）集中、服务（ &nbsp; &nbsp;）延伸、信息全国共享。&amp;2526lt;/p&amp;2526gt;","answer":"向上,向下","analysis":"&amp;2526lt;p&amp;2526gt;根据《人力资源社会保障部办公厅关于加快推进流动人员人事档案信息化建设的指导意见》中第一点总体要求中“按照数据向上集中、服务向下延伸、信息全国共享的原则”可知答案。&amp;2526lt;/p&amp;2526gt;","score":1.0,"userAnswer":"向上,向下","blanksNumber":2,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"},{"id":"68238","type":"001004","level":"003001","content":"\n进站前无工作经历的博士后研究人员参加工作时间从（    ）之日算起。","answer":"进站","analysis":"《人力资源和社会保障部全国博士后管理委员会关于贯彻落实〈国务院办公厅关于改革完善博士后制度的意见〉有关问题的通知》（人社部发〔2017〕20号）三、提升博士后工作服务水平提出：进站前无工作经历的博士后研究人员参加工作时间从进站之日算起。","score":1.0,"userAnswer":"进站","blanksNumber":1,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"},{"id":"68310","type":"001004","level":"003001","content":"\n健全（    ）机制，把社会稳定风险评估作为重大决策出台前的前置程序和刚性门槛，对决策可能引发的各种风险进行科学预测、综合研判。","answer":"重大决策社会稳定风险评估","analysis":"《人力资源社会保障部关于进一步加强人力资源和社会保障信访工作的意见》规定，健全重大决策社会稳定风险评估机制，把社会稳定风险评估作为重大决策出台前的前置程序和刚性门槛，对决策可能引发的各种风险进行科学预测、综合研判。","score":1.0,"userAnswer":"重大决策社会稳定风险评估","blanksNumber":1,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"},{"id":"68113","type":"001004","level":"003001","content":"\n按照《香港澳门台湾居民在内地（大陆）参加社会保险暂行办法》规定，港澳台居民在内地办理社会保险登记的有效证件包括港澳居民来往内地通行证和（    ）。","answer":"港澳台居民居住证","analysis":"《香港澳门台湾居民在内地（大陆）参加社会保险暂行办法》第十四条规定，办法所称“港澳台居民有效证件”，指港澳居民来往内地通行证、港澳台居民居住证。","score":1.0,"userAnswer":"港澳台居民居住证","blanksNumber":1,"signed":0,"checkResult":1,"userScore":"1.0","tag":"008001","chapterName":"null","inCollection":0,"choices":"null","keywords":"null"}]}],"ifDisplayResult":1,"ifDisplayAnswer":1,"ifDisplayDefeatPercent":0,"ifDisplayDefeatTerm":0,"ifDisplayShare":0,"displayResultTime":"2020-04-14 00:00:00","beginTime":"2020-06-01 00:42:27","endTime":"2020-06-01 00:42:27"},"code":"SUCCESS"}


def get_text(jsons):
    json_str = json.loads(json.dumps(jsons, ensure_ascii=False))
    duoxuans = json_str['data']['questionTypeSummaries'][0]['questions']
    panduans = json_str['data']['questionTypeSummaries'][1]['questions']

    for q in duoxuans:
        id = get_new(q['id'])
        content = get_new(q['content'])
        optionA = get_new(q['choices'][0]['content'])
        optionB = get_new(q['choices'][1]['content'])
        optionC = get_new(q['choices'][2]['content'])
        optionD = get_new(q['choices'][3]['content'])
        answer = get_new(q['answer'])
        analysis = ""
        optionE = ""
        chapterId = "0000"
        questionType = "001007"
        res = "{\"_id\":\"" + id + "\",\"content\":\"" + content + "\",\"answer\":\"" + answer + "\",\"analysis\":\"" + analysis + "\",\"optionA\":\"" + optionA + "\",\"optionB\":\"" + optionB + "\",\"optionC\":\"" + optionC + "\",\"optionD\":\"" + optionD + "\",\"optionE\":\"" + optionE + "\",\"chapterId\":\"" + chapterId + "\",\"questionType\":\"" + questionType + "\"}"
        print(res)

    for q in panduans:
        id = get_new(q['id'])
        content = get_new(q['content'])
        optionA = get_new(q['choices'][0]['content'])
        optionB = get_new(q['choices'][1]['content'])
        optionC = ""
        optionD = ""
        answer = get_new(q['answer'])
        analysis = ""
        optionE = ""
        chapterId = "0000"
        questionType = "001007"
        res = "{\"_id\":\"" + id + "\",\"content\":\"" + content + "\",\"answer\":\"" + answer + "\",\"analysis\":\"" + analysis + "\",\"optionA\":\"" + optionA + "\",\"optionB\":\"" + optionB + "\",\"optionC\":\"" + optionC + "\",\"optionD\":\"" + optionD + "\",\"optionE\":\"" + optionE + "\",\"chapterId\":\"" + chapterId + "\",\"questionType\":\"" + questionType + "\"}"
        print(res)


get_text(j)
