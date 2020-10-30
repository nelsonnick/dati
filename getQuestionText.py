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


json_0530_test = {
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
json_0531_test = {
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
json_0627_test = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"a51036c57d1140efac0162145f6c69e9","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599846,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":1,"code":"A","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":2,"code":"B","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":3,"code":"C","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":4,"code":"D","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"}],"keywords":"null"},{"id":"68726","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年政府工作报告指出，今年有关目标为：城镇新增就业（&nbsp;&nbsp;&nbsp; ）人以上，城镇调查失业率（&nbsp;&nbsp;&nbsp; ）左右，城镇登记失业率（&nbsp;&nbsp;&nbsp; ）左右。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9c5807f503084d8daaec7e16c3fc6772","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6.5%；5.5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fd0cd6f2d8714db2a00254d9bfb292a5","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6%；5.5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"106ca254439f4238a1a51f9b28628025","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6.5%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"a25ef3d52bf14b9eb77f995697c9c17c","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":1,"code":"A","content":"农村劳动力"},{"id":"20775075cd5b451b827342aa85304fc7","sort":2,"code":"B","content":"城镇劳动力"},{"id":"f1fb45ece27943f1b08b0390638b8438","sort":3,"code":"C","content":"城乡劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":4,"code":"D","content":"高校劳动力"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6a937d1dcae9447cac94ce236451b132","sort":1,"code":"A","content":"4"},{"id":"84f5476d5068448f8d760b6187a1bb35","sort":2,"code":"B","content":"5"},{"id":"40e7e2db81604a22aa8cab33cc970533","sort":3,"code":"C","content":"3"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":4,"code":"D","content":"6"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bcbfd8add87943f0ace414c4194d3546","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e3125d07cd0446a89213ec98e18812ab","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68725","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年5月至12月，对2019年1月1日之后参保不满( &nbsp;&nbsp;)的失业农民工，参照参保地城市低保标准，按月发放不超过( &nbsp;&nbsp;)个月的临时生活补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c16cbd2548cd4f78b46e6a212158fa32","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e6643bbfec93471f888bb4891304f525","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"97071a22bb11498384baf737fd2d7635","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9bcba69d0e274fd4ade1bb6e44238fd8","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":1,"code":"A","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":2,"code":"B","content":"按照小李的要求为其办理转正定级手续"},{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":3,"code":"C","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":4,"code":"D","content":"与档案接收机构协商，想办法为小李办理。"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"57d05cea438c42ceabf4ec28047254c3","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"38ac1534bac04628b824eee9c740e6ed","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68592","type":"001007","level":"003001","content":"属于行政审批项目的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6d0991298d834283ace6da359767410e","sort":1,"code":"A","content":"职业技能考核鉴定机构设立审批"},{"id":"a51751a0bd244b29b28eedbe23089ba7","sort":2,"code":"B","content":"民办职业培训机构变更审批"},{"id":"64660271849e44af98a09ce7791f55dc","sort":3,"code":"C","content":"劳务派遣经营"},{"id":"94a8395b864240348475edc5c522c30e","sort":4,"code":"D","content":"标准工时制度"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":1,"code":"A","content":"5"},{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":2,"code":"B","content":"50"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":3,"code":"C","content":"40"},{"id":"03b1512043044934a2d266cff87749f7","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68620","type":"001007","level":"003001","content":"在办理机关事业单位职业年金转移接续时，无需转移的基金项目包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4038e407cd32415e941dc64bc86f7969","sort":1,"code":"A","content":"个人缴费本息"},{"id":"83c5e0f5fd124299b2aadccc4da44c6e","sort":2,"code":"B","content":"原转入的企业年金"},{"id":"f7c56f8bb62f4a2eae54ee2e7da8edff","sort":3,"code":"C","content":"补记的职业年金"},{"id":"cc0fe7a8998f46a4b1392c42b28a687a","sort":4,"code":"D","content":"缴费形成的职业年金"}],"keywords":"null"},{"id":"68556","type":"001007","level":"003001","content":"A省人才中心实行了档案接收告知承诺制，其在接收某企业员工小张的档案时，发现缺少核定小张学历学位的材料。该人才中心正确做法是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bfd6c9e1fa7e406bb2942347175c6f48","sort":1,"code":"A","content":"一次性告知所缺材料及其可能造成的影响后，采取先存后补方式予以接收"},{"id":"cbbf941b0d784fa991ed21d2c952eb10","sort":2,"code":"B","content":"一次性告知所缺材料及其可能造成的影响，经本人作出书面知情说明、承诺补充材料后予以接收"},{"id":"7c3dba49ff6f4b128d475f7192c7fe73","sort":3,"code":"C","content":"与原单位协商退回并补充材料"},{"id":"3927d7aff6fa4c848316890cccf2f613","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"68567","type":"001007","level":"003001","content":"按照现行企业年金制度，某企业当年年度工资总额为500万元，该企业当年度缴纳企业年金的额度，不符合规定的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e1171cc6d05742a18d04fb02b1fcfcc8","sort":1,"code":"A","content":"20万元"},{"id":"f0c637e8214e4881b3a497b10801045a","sort":2,"code":"B","content":"40万元"},{"id":"d6da7cd4c58e4d47966177125dc00cf6","sort":3,"code":"C","content":"80万元"},{"id":"62ff517715bf4207a464dfc56e981f84","sort":4,"code":"D","content":"100万元"}],"keywords":"null"},{"id":"68604","type":"001007","level":"003001","content":"职称评审委员会评审专家应当具备的条件是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"81cf1c608d3c4bdc93132ae6628e52ac","sort":1,"code":"A","content":"本职称系列或者专业相应层级的职称"},{"id":"f8ec40175498465794628d3e215aafc9","sort":2,"code":"B","content":"从事本领域专业技术工作"},{"id":"da2f030fb71e4d2da7b4c5b08e522d9f","sort":3,"code":"C","content":"年龄不超过65周"},{"id":"9a5838e7b40042d995e4fe69cb34086a","sort":4,"code":"D","content":"良好的职业道德"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0a552d4343a044648aa59cb70df04f39","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":1,"code":"A","content":"10"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":2,"code":"B","content":"8"},{"id":"8e5fd62e7b12443db02196646c2f3315","sort":3,"code":"C","content":"5"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":4,"code":"D","content":"12"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":1,"code":"A","content":"省级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":2,"code":"B","content":"经人力资源社会保障部门授权的单位"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":3,"code":"C","content":"县级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":4,"code":"D","content":"流动人员本人"}],"keywords":"null"},{"id":"68600","type":"001007","level":"003001","content":"按照现行规定，面向个人发放的创业担保贷款期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"24092da8dfdf4c9e910f8421d51e885c","sort":1,"code":"A","content":"2"},{"id":"414a064395064954a551f10efd6a73d9","sort":2,"code":"B","content":"3"},{"id":"d7d57727a08f4884950a0f667f43caf4","sort":3,"code":"C","content":"4"},{"id":"cfb5ba55490b49fd91dd7d7e0a82de7d","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":1,"code":"A","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"377c82a0fae341139629ddee8f6a400e","sort":2,"code":"B","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":3,"code":"C","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":4,"code":"D","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":1,"code":"A","content":"145"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"c5bf34b901e04adeb4129feb04f01116","sort":3,"code":"C","content":"195"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":4,"code":"D","content":"139"}],"keywords":"null"},{"id":"68582","type":"001007","level":"003001","content":"老王因工伤生活不能自理，现停工留薪期需要护理。老王的（   ）可以从工伤保险基金支出。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ad60dee7c6a1413b9b8ee7555bd84922","sort":1,"code":"A","content":"伙食补助费"},{"id":"bd8a68d0a39b4dd8bb431ded378294b9","sort":2,"code":"B","content":"赴统筹地区以外就医所需交通、食宿费"},{"id":"5a143c14dde44889bb20d45be1c5adf5","sort":3,"code":"C","content":"生活护理费"},{"id":"66b9b5278b7d4a428a4e2f9f6d307925","sort":4,"code":"D","content":"工伤医疗待遇"}],"keywords":"null"},{"id":"68597","type":"001007","level":"003001","content":"属于高校毕业生基层服务项目的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b8f6e68bbba84a7ba269bfaefaefe9c3","sort":1,"code":"A","content":"“凤凰飞翔”计划"},{"id":"a3d35ea01e424f67ac8b84525f318ca7","sort":2,"code":"B","content":"“三支一扶”计划"},{"id":"1c1f46c89b06468eb1497d0825bd0658","sort":3,"code":"C","content":"志愿服务西部计划"},{"id":"a9983ec2a62b48e9915eb0112bc48a3c","sort":4,"code":"D","content":"公益就业行动计划"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":1,"code":"A","content":"60000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":2,"code":"B","content":"84000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":3,"code":"C","content":"96000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":4,"code":"D","content":"108000元"}],"keywords":"null"},{"id":"68591","type":"001007","level":"003001","content":"用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"96175f4056be4936b13f9307e2eb2ae0","sort":1,"code":"A","content":"公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理"},{"id":"3372645120c247f4b83b3120312dbd92","sort":2,"code":"B","content":"员工承诺，在本公司工作期间遵守规章制度"},{"id":"741b8f627d864ab3999fe4d9cea6ae87","sort":3,"code":"C","content":"按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同"},{"id":"107b86939e514a7f8f50b7d96b2507a1","sort":4,"code":"D","content":"员工自愿承诺，在本公司工作期间不结婚"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1045b445dbf340f992680615412a2c36","sort":1,"code":"A","content":"10000元"},{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":2,"code":"B","content":"8000元"},{"id":"1e922892adfa4cc291ccc8e08086313f","sort":3,"code":"C","content":"6000元"},{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":4,"code":"D","content":"4000元"}],"keywords":"null"},{"id":"68583","type":"001007","level":"003001","content":"城乡居民基本养老保险最高缴费档次标准原则上不超过当地(    )参加职工基本养老保险的年缴费额。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e389eef064b8405488a2e37fcd58d4ea","sort":1,"code":"A","content":"企业职工"},{"id":"d57337d54ad1408bac0f4626029888d4","sort":2,"code":"B","content":"灵活就业人员"},{"id":"69e21d5c8f1744b189967826d3bda008","sort":3,"code":"C","content":"社会组织人员"},{"id":"5373234878474becb562233802a15c39","sort":4,"code":"D","content":"机关事业单位人员"}],"keywords":"null"},{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cd44e594750548e8a9b814d8744f4121","sort":1,"code":"A","content":"需要经常出差，男士优先"},{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":2,"code":"B","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"},{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":3,"code":"C","content":"具有互联网工作经验优先"},{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":4,"code":"D","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":1,"code":"A","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":2,"code":"B","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":3,"code":"C","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":4,"code":"D","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":1,"code":"A","content":"补贴标准根据乡村生活费用确定"},{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":2,"code":"B","content":"应当为安置人员购买意外伤害商业保险"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":3,"code":"C","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":4,"code":"D","content":"可以签订劳动合同也可以签订劳务协议"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":1,"code":"A","content":"9；2；3"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":2,"code":"B","content":"10；4；5"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":3,"code":"C","content":"10；5；6"},{"id":"b34b2d30e563409e9615ece5765d7739","sort":4,"code":"D","content":"9；3；4"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3413d86553634b5c958740b3ec761da0","sort":1,"code":"A","content":"制定企业年金基金战略资产配置策略"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":2,"code":"B","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"5f415af62962421ebe130734f5103ae3","sort":3,"code":"C","content":"安全保管企业年金基金财产"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":4,"code":"D","content":"及时办理清算、交割事宜"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a6937611ca064abfb27cba90c8064169","sort":1,"code":"A","content":"入境权"},{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":2,"code":"B","content":"工作权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":3,"code":"C","content":"定居权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":4,"code":"D","content":"民事权"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c663276dfd0b4d2c93e4177521a14071","sort":1,"code":"A","content":"原单位注册地；常住地"},{"id":"5a22297e9c5e42588338374f2db13853","sort":2,"code":"B","content":"出生地；户籍地"},{"id":"583b9bc056c641ffa095ef97015a8380","sort":3,"code":"C","content":"常住地；出生地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":4,"code":"D","content":"常住地；常住地"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":1,"code":"A","content":"正常运营3个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":2,"code":"B","content":"正常运营5个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":3,"code":"C","content":"正常运营1个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":4,"code":"D","content":"正常运营7个月"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"defeb3d10031449d86eaf10f6271a331","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f6cf14fd2b249109922524a550c021b","sort":1,"code":"A","content":"个人自带"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":2,"code":"B","content":"可直接从学校转递到企业"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":3,"code":"C","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"3ae4a91f95a049629966229077ae4831","sort":4,"code":"D","content":"可以弃档不管"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":1,"code":"A","content":"按照本人工资的60%支付伤残津贴"},{"id":"4f9b228b803e481b9aed1047772b5845","sort":2,"code":"B","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"2c3304f118214840a8944ef614188916","sort":3,"code":"C","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"},{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":4,"code":"D","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"}],"keywords":"null"},{"id":"68722","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对&amp;2526lt;/span&amp;2526gt;2020年3月至12月，领取失业保险金期满仍未就业的失业人员、不符合领取失业保险金条件的参保失业人员，发放（ &nbsp;&nbsp;）个月的失业补助金，标准不高于当地失业保险金的（ &nbsp;&nbsp;&nbsp;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d8243054793d442c9577daac5446188a","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c2c76fcab56746099f6e0020afb20110","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"7383c2af02604820b6882b632b404923","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"b49f0e5f79a8463cbb91d053a19a69cc","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8df6381555cb4de9883763e7239ed809","sort":1,"code":"A","content":"6个"},{"id":"713eaa07fb8042eea09409619ff0f619","sort":2,"code":"B","content":"8个"},{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":3,"code":"C","content":"7个"},{"id":"88f1f34a065f44dea656d7797a9edc11","sort":4,"code":"D","content":"5个"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":1,"code":"A","content":"集体合同约定的工资增幅是否合理"},{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":2,"code":"B","content":"补充保险和福利约定是否符合国家有关规"},{"id":"d76d9d824b1348c190e381f06a178776","sort":3,"code":"C","content":"协商程序是否履行《集体合同规定》所规定的具体程序"},{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":4,"code":"D","content":"职工一方协商代表资格是否符合国家有关规定"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":2,"code":"B","content":"2"},{"id":"394106514712430bad66fd4bf853deb1","sort":3,"code":"C","content":"3"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":1,"code":"A","content":"累计参保缴费满三年"},{"id":"84fdcd3629f2496597b7906039f6acaf","sort":2,"code":"B","content":"累计参保缴费满二年"},{"id":"df3ec29881de4e89a74191f1b922cccb","sort":3,"code":"C","content":"累计参保缴费满一年"},{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":4,"code":"D","content":"不设参保年限"}],"keywords":"null"},{"id":"68619","type":"001007","level":"003001","content":"《领取社会保险待遇资格确认经办规程（暂行）》规定，属于丧失领取养老保险待遇资格的人员包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"484dea31f666461bac6a785a1438af2e","sort":1,"code":"A","content":"全民参保登记数据库标识为健在但服刑的人员"},{"id":"10707a5ed75745b89d87077d51a0d5bd","sort":2,"code":"B","content":"国家人口库中标识为死亡、有高铁出行记录的人员"},{"id":"2425ab1a2e5e4efbbb517cb94f9745bb","sort":3,"code":"C","content":"人力资源社会保障服务平台确认及上报的死亡人员"},{"id":"ffe16158fb314d6885bb622fbdf0e9d4","sort":4,"code":"D","content":"家属反映其父母仍然健在的人员"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f1a18478c3554009833aa2d6993ded3a","sort":1,"code":"A","content":"不属于本仲裁委员会管辖"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":2,"code":"B","content":"不属于本仲裁委员会管辖"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":3,"code":"C","content":"超出规定的仲裁审查申请期间的"},{"id":"adfa6de440ea42a588db9548679b987a","sort":4,"code":"D","content":"不属于仲裁委员会受理争议范围"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":1,"code":"A","content":"五至七"},{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":2,"code":"B","content":"四至六"},{"id":"e39693a21869498da8aa63f62ffaaa91","sort":3,"code":"C","content":"三至五"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":4,"code":"D","content":"六至八"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":1,"code":"A","content":"“三区三州”等深度贫困地区安置区"},{"id":"846e95aa078f4798b9f2adda36932a45","sort":2,"code":"B","content":"人口规模1000人以上大型安置区"},{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":3,"code":"C","content":"高寒、高海拔安置区"},{"id":"973b9a79351146a4acac647acc0331ff","sort":4,"code":"D","content":"地市级城市安置区"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68626","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;地方各级人民政府和有关部门、公共就业服务机构举办的招聘会，不得向劳动者和用人单位收取费用。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3721c379c2234614901770842b2364d8","sort":1,"code":"A","content":"错误"},{"id":"e45d789984ba4d87b23af1578f8d6635","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68633","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;生效了的专项集体合同，应当自生效之日起由协商代表及时以适当的方式向本方全体人员公布。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"591f2e658eea491e936cb7ef47084f89","sort":1,"code":"A","content":"错误"},{"id":"590f278ac32a4a979247de53953c62f3","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68627","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce4efa5b214748c78c355df38da717a2","sort":1,"code":"A","content":"错误"},{"id":"1be729e13a1945bab354d0faf4c3492c","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]}]},"code":"SUCCESS"}
json_0627_answer = {"httpStatus":"OK","status":0,"message":"成功","data":[{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"A,B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":1,"code":"A","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"},{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":2,"code":"B","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":3,"code":"C","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":4,"code":"D","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"}],"keywords":"null"},{"id":"68726","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年政府工作报告指出，今年有关目标为：城镇新增就业（&nbsp;&nbsp;&nbsp; ）人以上，城镇调查失业率（&nbsp;&nbsp;&nbsp; ）左右，城镇登记失业率（&nbsp;&nbsp;&nbsp; ）左右。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a25ef3d52bf14b9eb77f995697c9c17c","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"106ca254439f4238a1a51f9b28628025","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6.5%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9c5807f503084d8daaec7e16c3fc6772","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6.5%；5.5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fd0cd6f2d8714db2a00254d9bfb292a5","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6%；5.5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":1,"code":"A","content":"农村劳动力"},{"id":"f1fb45ece27943f1b08b0390638b8438","sort":2,"code":"B","content":"城乡劳动力"},{"id":"20775075cd5b451b827342aa85304fc7","sort":3,"code":"C","content":"城镇劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":4,"code":"D","content":"高校劳动力"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"A,B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"40e7e2db81604a22aa8cab33cc970533","sort":1,"code":"A","content":"3"},{"id":"6a937d1dcae9447cac94ce236451b132","sort":2,"code":"B","content":"4"},{"id":"84f5476d5068448f8d760b6187a1bb35","sort":3,"code":"C","content":"5"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":4,"code":"D","content":"6"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e3125d07cd0446a89213ec98e18812ab","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bcbfd8add87943f0ace414c4194d3546","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68725","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年5月至12月，对2019年1月1日之后参保不满( &nbsp;&nbsp;)的失业农民工，参照参保地城市低保标准，按月发放不超过( &nbsp;&nbsp;)个月的临时生活补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9bcba69d0e274fd4ade1bb6e44238fd8","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"97071a22bb11498384baf737fd2d7635","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e6643bbfec93471f888bb4891304f525","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c16cbd2548cd4f78b46e6a212158fa32","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":1,"code":"A","content":"按照小李的要求为其办理转正定级手续"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":2,"code":"B","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":3,"code":"C","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":4,"code":"D","content":"与档案接收机构协商，想办法为小李办理。"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"38ac1534bac04628b824eee9c740e6ed","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"57d05cea438c42ceabf4ec28047254c3","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68592","type":"001007","level":"003001","content":"属于行政审批项目的是（   ）","answer":"A,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a51751a0bd244b29b28eedbe23089ba7","sort":1,"code":"A","content":"民办职业培训机构变更审批"},{"id":"6d0991298d834283ace6da359767410e","sort":2,"code":"B","content":"职业技能考核鉴定机构设立审批"},{"id":"64660271849e44af98a09ce7791f55dc","sort":3,"code":"C","content":"劳务派遣经营"},{"id":"94a8395b864240348475edc5c522c30e","sort":4,"code":"D","content":"标准工时制度"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":1,"code":"A","content":"50"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":2,"code":"B","content":"40"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":3,"code":"C","content":"5"},{"id":"03b1512043044934a2d266cff87749f7","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68620","type":"001007","level":"003001","content":"在办理机关事业单位职业年金转移接续时，无需转移的基金项目包括（    ）","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cc0fe7a8998f46a4b1392c42b28a687a","sort":1,"code":"A","content":"缴费形成的职业年金"},{"id":"4038e407cd32415e941dc64bc86f7969","sort":2,"code":"B","content":"个人缴费本息"},{"id":"f7c56f8bb62f4a2eae54ee2e7da8edff","sort":3,"code":"C","content":"补记的职业年金"},{"id":"83c5e0f5fd124299b2aadccc4da44c6e","sort":4,"code":"D","content":"原转入的企业年金"}],"keywords":"null"},{"id":"68556","type":"001007","level":"003001","content":"A省人才中心实行了档案接收告知承诺制，其在接收某企业员工小张的档案时，发现缺少核定小张学历学位的材料。该人才中心正确做法是(    )。","answer":"A,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cbbf941b0d784fa991ed21d2c952eb10","sort":1,"code":"A","content":"一次性告知所缺材料及其可能造成的影响，经本人作出书面知情说明、承诺补充材料后予以接收"},{"id":"bfd6c9e1fa7e406bb2942347175c6f48","sort":2,"code":"B","content":"一次性告知所缺材料及其可能造成的影响后，采取先存后补方式予以接收"},{"id":"7c3dba49ff6f4b128d475f7192c7fe73","sort":3,"code":"C","content":"与原单位协商退回并补充材料"},{"id":"3927d7aff6fa4c848316890cccf2f613","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"68567","type":"001007","level":"003001","content":"按照现行企业年金制度，某企业当年年度工资总额为500万元，该企业当年度缴纳企业年金的额度，不符合规定的是(    )。","answer":"C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e1171cc6d05742a18d04fb02b1fcfcc8","sort":1,"code":"A","content":"20万元"},{"id":"f0c637e8214e4881b3a497b10801045a","sort":2,"code":"B","content":"40万元"},{"id":"d6da7cd4c58e4d47966177125dc00cf6","sort":3,"code":"C","content":"80万元"},{"id":"62ff517715bf4207a464dfc56e981f84","sort":4,"code":"D","content":"100万元"}],"keywords":"null"},{"id":"68604","type":"001007","level":"003001","content":"职称评审委员会评审专家应当具备的条件是（    ）。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9a5838e7b40042d995e4fe69cb34086a","sort":1,"code":"A","content":"良好的职业道德"},{"id":"81cf1c608d3c4bdc93132ae6628e52ac","sort":2,"code":"B","content":"本职称系列或者专业相应层级的职称"},{"id":"f8ec40175498465794628d3e215aafc9","sort":3,"code":"C","content":"从事本领域专业技术工作"},{"id":"da2f030fb71e4d2da7b4c5b08e522d9f","sort":4,"code":"D","content":"年龄不超过65周"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"0a552d4343a044648aa59cb70df04f39","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8e5fd62e7b12443db02196646c2f3315","sort":1,"code":"A","content":"5"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":2,"code":"B","content":"8"},{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":3,"code":"C","content":"10"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":4,"code":"D","content":"12"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1218cb6efe284f6c8956e734857815fe","sort":1,"code":"A","content":"县级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":2,"code":"B","content":"经人力资源社会保障部门授权的单位"},{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":3,"code":"C","content":"省级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":4,"code":"D","content":"流动人员本人"}],"keywords":"null"},{"id":"68626","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;地方各级人民政府和有关部门、公共就业服务机构举办的招聘会，不得向劳动者和用人单位收取费用。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e45d789984ba4d87b23af1578f8d6635","sort":1,"code":"A","content":"正确"},{"id":"3721c379c2234614901770842b2364d8","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68600","type":"001007","level":"003001","content":"按照现行规定，面向个人发放的创业担保贷款期限可以是(    )年。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cfb5ba55490b49fd91dd7d7e0a82de7d","sort":1,"code":"A","content":"1"},{"id":"24092da8dfdf4c9e910f8421d51e885c","sort":2,"code":"B","content":"2"},{"id":"414a064395064954a551f10efd6a73d9","sort":3,"code":"C","content":"3"},{"id":"d7d57727a08f4884950a0f667f43caf4","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":1,"code":"A","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":2,"code":"B","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"377c82a0fae341139629ddee8f6a400e","sort":3,"code":"C","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":4,"code":"D","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5bf34b901e04adeb4129feb04f01116","sort":1,"code":"A","content":"195"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":3,"code":"C","content":"145"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":4,"code":"D","content":"139"}],"keywords":"null"},{"id":"68582","type":"001007","level":"003001","content":"老王因工伤生活不能自理，现停工留薪期需要护理。老王的（   ）可以从工伤保险基金支出。","answer":"A,B,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ad60dee7c6a1413b9b8ee7555bd84922","sort":1,"code":"A","content":"伙食补助费"},{"id":"bd8a68d0a39b4dd8bb431ded378294b9","sort":2,"code":"B","content":"赴统筹地区以外就医所需交通、食宿费"},{"id":"5a143c14dde44889bb20d45be1c5adf5","sort":3,"code":"C","content":"生活护理费"},{"id":"66b9b5278b7d4a428a4e2f9f6d307925","sort":4,"code":"D","content":"工伤医疗待遇"}],"keywords":"null"},{"id":"68597","type":"001007","level":"003001","content":"属于高校毕业生基层服务项目的是(    )。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b8f6e68bbba84a7ba269bfaefaefe9c3","sort":1,"code":"A","content":"“凤凰飞翔”计划"},{"id":"a3d35ea01e424f67ac8b84525f318ca7","sort":2,"code":"B","content":"“三支一扶”计划"},{"id":"1c1f46c89b06468eb1497d0825bd0658","sort":3,"code":"C","content":"志愿服务西部计划"},{"id":"a9983ec2a62b48e9915eb0112bc48a3c","sort":4,"code":"D","content":"公益就业行动计划"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":1,"code":"A","content":"60000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":2,"code":"B","content":"84000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":3,"code":"C","content":"96000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":4,"code":"D","content":"108000元"}],"keywords":"null"},{"id":"68591","type":"001007","level":"003001","content":"用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（    ）。","answer":"A,B,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"741b8f627d864ab3999fe4d9cea6ae87","sort":1,"code":"A","content":"按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同"},{"id":"96175f4056be4936b13f9307e2eb2ae0","sort":2,"code":"B","content":"公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理"},{"id":"3372645120c247f4b83b3120312dbd92","sort":3,"code":"C","content":"员工承诺，在本公司工作期间遵守规章制度"},{"id":"107b86939e514a7f8f50b7d96b2507a1","sort":4,"code":"D","content":"员工自愿承诺，在本公司工作期间不结婚"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":1,"code":"A","content":"4000元"},{"id":"1e922892adfa4cc291ccc8e08086313f","sort":2,"code":"B","content":"6000元"},{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":3,"code":"C","content":"8000元"},{"id":"1045b445dbf340f992680615412a2c36","sort":4,"code":"D","content":"10000元"}],"keywords":"null"},{"id":"68583","type":"001007","level":"003001","content":"城乡居民基本养老保险最高缴费档次标准原则上不超过当地(    )参加职工基本养老保险的年缴费额。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e389eef064b8405488a2e37fcd58d4ea","sort":1,"code":"A","content":"企业职工"},{"id":"69e21d5c8f1744b189967826d3bda008","sort":2,"code":"B","content":"社会组织人员"},{"id":"d57337d54ad1408bac0f4626029888d4","sort":3,"code":"C","content":"灵活就业人员"},{"id":"5373234878474becb562233802a15c39","sort":4,"code":"D","content":"机关事业单位人员"}],"keywords":"null"},{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cd44e594750548e8a9b814d8744f4121","sort":1,"code":"A","content":"需要经常出差，男士优先"},{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":2,"code":"B","content":"具有互联网工作经验优先"},{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":3,"code":"C","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"},{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":4,"code":"D","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":1,"code":"A","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":2,"code":"B","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":3,"code":"C","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":4,"code":"D","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"A,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2fd776cc724e464e9d4fd529d781815f","sort":1,"code":"A","content":"可以签订劳动合同也可以签订劳务协议"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":2,"code":"B","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":3,"code":"C","content":"应当为安置人员购买意外伤害商业保险"},{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":4,"code":"D","content":"补贴标准根据乡村生活费用确定"}],"keywords":"null"},{"id":"68633","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;生效了的专项集体合同，应当自生效之日起由协商代表及时以适当的方式向本方全体人员公布。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"590f278ac32a4a979247de53953c62f3","sort":1,"code":"A","content":"正确"},{"id":"591f2e658eea491e936cb7ef47084f89","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":1,"code":"A","content":"9；2；3"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":2,"code":"B","content":"10；5；6"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":3,"code":"C","content":"10；4；5"},{"id":"b34b2d30e563409e9615ece5765d7739","sort":4,"code":"D","content":"9；3；4"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"A,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5f415af62962421ebe130734f5103ae3","sort":1,"code":"A","content":"安全保管企业年金基金财产"},{"id":"3413d86553634b5c958740b3ec761da0","sort":2,"code":"B","content":"制定企业年金基金战略资产配置策略"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":3,"code":"C","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":4,"code":"D","content":"及时办理清算、交割事宜"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":1,"code":"A","content":"工作权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":2,"code":"B","content":"定居权"},{"id":"a6937611ca064abfb27cba90c8064169","sort":3,"code":"C","content":"入境权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":4,"code":"D","content":"民事权"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5a22297e9c5e42588338374f2db13853","sort":1,"code":"A","content":"出生地；户籍地"},{"id":"c663276dfd0b4d2c93e4177521a14071","sort":2,"code":"B","content":"原单位注册地；常住地"},{"id":"583b9bc056c641ffa095ef97015a8380","sort":3,"code":"C","content":"常住地；出生地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":4,"code":"D","content":"常住地；常住地"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":1,"code":"A","content":"正常运营1个月"},{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":2,"code":"B","content":"正常运营3个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":3,"code":"C","content":"正常运营5个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":4,"code":"D","content":"正常运营7个月"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"defeb3d10031449d86eaf10f6271a331","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68627","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1be729e13a1945bab354d0faf4c3492c","sort":1,"code":"A","content":"正确"},{"id":"ce4efa5b214748c78c355df38da717a2","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"623bf52e22c84515b275a537283e7b8e","sort":1,"code":"A","content":"可直接从学校转递到企业"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":2,"code":"B","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"4f6cf14fd2b249109922524a550c021b","sort":3,"code":"C","content":"个人自带"},{"id":"3ae4a91f95a049629966229077ae4831","sort":4,"code":"D","content":"可以弃档不管"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":1,"code":"A","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"},{"id":"4f9b228b803e481b9aed1047772b5845","sort":2,"code":"B","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":3,"code":"C","content":"按照本人工资的60%支付伤残津贴"},{"id":"2c3304f118214840a8944ef614188916","sort":4,"code":"D","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"}],"keywords":"null"},{"id":"68722","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对&amp;2526lt;/span&amp;2526gt;2020年3月至12月，领取失业保险金期满仍未就业的失业人员、不符合领取失业保险金条件的参保失业人员，发放（ &nbsp;&nbsp;）个月的失业补助金，标准不高于当地失业保险金的（ &nbsp;&nbsp;&nbsp;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b49f0e5f79a8463cbb91d053a19a69cc","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"7383c2af02604820b6882b632b404923","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c2c76fcab56746099f6e0020afb20110","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"d8243054793d442c9577daac5446188a","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"88f1f34a065f44dea656d7797a9edc11","sort":1,"code":"A","content":"5个"},{"id":"8df6381555cb4de9883763e7239ed809","sort":2,"code":"B","content":"6个"},{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":3,"code":"C","content":"7个"},{"id":"713eaa07fb8042eea09409619ff0f619","sort":4,"code":"D","content":"8个"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"A,B,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":1,"code":"A","content":"职工一方协商代表资格是否符合国家有关规定"},{"id":"d76d9d824b1348c190e381f06a178776","sort":2,"code":"B","content":"协商程序是否履行《集体合同规定》所规定的具体程序"},{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":3,"code":"C","content":"集体合同约定的工资增幅是否合理"},{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":4,"code":"D","content":"补充保险和福利约定是否符合国家有关规"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"394106514712430bad66fd4bf853deb1","sort":2,"code":"B","content":"3"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":3,"code":"C","content":"2"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"df3ec29881de4e89a74191f1b922cccb","sort":1,"code":"A","content":"累计参保缴费满一年"},{"id":"84fdcd3629f2496597b7906039f6acaf","sort":2,"code":"B","content":"累计参保缴费满二年"},{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":3,"code":"C","content":"累计参保缴费满三年"},{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":4,"code":"D","content":"不设参保年限"}],"keywords":"null"},{"id":"68619","type":"001007","level":"003001","content":"《领取社会保险待遇资格确认经办规程（暂行）》规定，属于丧失领取养老保险待遇资格的人员包括（    ）","answer":"B,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ffe16158fb314d6885bb622fbdf0e9d4","sort":1,"code":"A","content":"家属反映其父母仍然健在的人员"},{"id":"484dea31f666461bac6a785a1438af2e","sort":2,"code":"B","content":"全民参保登记数据库标识为健在但服刑的人员"},{"id":"10707a5ed75745b89d87077d51a0d5bd","sort":3,"code":"C","content":"国家人口库中标识为死亡、有高铁出行记录的人员"},{"id":"2425ab1a2e5e4efbbb517cb94f9745bb","sort":4,"code":"D","content":"人力资源社会保障服务平台确认及上报的死亡人员"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"A,B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"adfa6de440ea42a588db9548679b987a","sort":1,"code":"A","content":"不属于仲裁委员会受理争议范围"},{"id":"f1a18478c3554009833aa2d6993ded3a","sort":2,"code":"B","content":"不属于本仲裁委员会管辖"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":3,"code":"B","content":"不属于本仲裁委员会管辖"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":4,"code":"D","content":"超出规定的仲裁审查申请期间的"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e39693a21869498da8aa63f62ffaaa91","sort":1,"code":"A","content":"三至五"},{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":2,"code":"B","content":"四至六"},{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":3,"code":"C","content":"五至七"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":4,"code":"D","content":"六至八"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"973b9a79351146a4acac647acc0331ff","sort":1,"code":"A","content":"地市级城市安置区"},{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":2,"code":"B","content":"“三区三州”等深度贫困地区安置区"},{"id":"846e95aa078f4798b9f2adda36932a45","sort":3,"code":"C","content":"人口规模1000人以上大型安置区"},{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":4,"code":"D","content":"高寒、高海拔安置区"}],"keywords":"null"}],"code":"SUCCESS"}

json_0627_test2 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"b856cb9693e74cb0920f4e3cf74572c1","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599196,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":1,"code":"A","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":2,"code":"B","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":3,"code":"C","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":4,"code":"D","content":"约定王某工资为1000元/月，试用期工资为700元/月"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"defeb3d10031449d86eaf10f6271a331","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"648f6280ed78408a955bb9d932535e11","sort":1,"code":"A","content":"流动人员本人"},{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":2,"code":"B","content":"省级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":3,"code":"C","content":"经人力资源社会保障部门授权的单位"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":4,"code":"D","content":"县级公共就业和人才服务机构"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":1,"code":"A","content":"累计参保缴费满三年"},{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":2,"code":"B","content":"不设参保年限"},{"id":"df3ec29881de4e89a74191f1b922cccb","sort":3,"code":"C","content":"累计参保缴费满一年"},{"id":"84fdcd3629f2496597b7906039f6acaf","sort":4,"code":"D","content":"累计参保缴费满二年"}],"keywords":"null"},{"id":"68723","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对于消杀防疫、保洁环卫等临时性公益岗位，根据工作任务和工作时间，给予一定的岗位补贴和社会保险补贴，补贴期限最长不超过（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）个月。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9f9527074b2f45a68a54fecfb938b402","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"},{"id":"838276c3b20e40b592f138faded1ffab","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;7&amp;2526lt;/p&amp;2526gt;"},{"id":"72cd2c8aac9e49fa94bc5fc4f351682f","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"},{"id":"0c0e8fb4121b4399832df59d6534cb05","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":1,"code":"A","content":"8000元"},{"id":"1e922892adfa4cc291ccc8e08086313f","sort":2,"code":"B","content":"6000元"},{"id":"1045b445dbf340f992680615412a2c36","sort":3,"code":"C","content":"10000元"},{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":4,"code":"D","content":"4000元"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"846e95aa078f4798b9f2adda36932a45","sort":1,"code":"A","content":"人口规模1000人以上大型安置区"},{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":2,"code":"B","content":"“三区三州”等深度贫困地区安置区"},{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":3,"code":"C","content":"高寒、高海拔安置区"},{"id":"973b9a79351146a4acac647acc0331ff","sort":4,"code":"D","content":"地市级城市安置区"}],"keywords":"null"},{"id":"68593","type":"001007","level":"003001","content":"无法进行失业登记的人员包括(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"abc9ac31fc81493a87535e02f62700c2","sort":1,"code":"A","content":"退出现役军人"},{"id":"097dc10304544df2ac34a71a406871e5","sort":2,"code":"B","content":"刑满释放人员"},{"id":"d3f9679e86b348109957df6809b90dd5","sort":3,"code":"C","content":"个体工商户业主或私营企业业主停业、破产停止经营的"},{"id":"709fbe517f27498a837fd51f6e23730f","sort":4,"code":"D","content":"年满16周岁，从各类学校毕业、肄业的"}],"keywords":"null"},{"id":"68608","type":"001007","level":"003001","content":"博士后设站单位可以将在站博士后予以退站的情形包括（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b6a870373e994075884b5516965e7050","sort":1,"code":"A","content":"出国逾期不归超过15日的"},{"id":"fe600c99ad2f409396e87e26c02b01e0","sort":2,"code":"B","content":"提供虚假材料获得进站资格的"},{"id":"cf8aa510cd684d9a932ef0d10284a4a9","sort":3,"code":"C","content":"因患病等原因难以完成工作的"},{"id":"0bc09acfdb2742a1952906a39c23afd7","sort":4,"code":"D","content":"进站一年仍未取得国家承认的博士学位证书的"}],"keywords":"null"},{"id":"68574","type":"001007","level":"003001","content":"老王在领取失业保险金期间因达到退休年龄办理了退休手续，并开始领取养老金。那么(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"51829768776847d1995a7bf0331eedc6","sort":1,"code":"A","content":"他可以继续领取剩余的失业保险金"},{"id":"0dc709dd74274fedbb89a08feb023003","sort":2,"code":"B","content":"他不可以继续领失业保险金，但可以享受其他失业保险待遇"},{"id":"73f7985a40e6455786c037381bf05164","sort":3,"code":"C","content":"他不可以继续领失业保险金"},{"id":"5c9fb3c9a8704de88fd7be3be4cab922","sort":4,"code":"D","content":"他可以再领取一个月的失业保险金"}],"keywords":"null"},{"id":"68624","type":"001007","level":"003001","content":"根据《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》，严重失信、失范行为包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b4b68d4fccf44ed484f8a7922ea94cd5","sort":1,"code":"A","content":"社保服务机构违反服务协议的"},{"id":"42e37dfb02bf4ffcb42f2a8c48234005","sort":2,"code":"B","content":"非法获取社保个人权益数据的"},{"id":"14af74be5a8c4080ae67f4d0a37e7dc0","sort":3,"code":"C","content":"隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的"},{"id":"c937f322d72945d6be8d65d0d3edc7e4","sort":4,"code":"D","content":"应缴纳社会保险费却拒不缴纳的"}],"keywords":"null"},{"id":"68576","type":"001007","level":"003001","content":"以建设项目为单位参保的建筑企业，可以按照(    )的一定比例计算缴纳工伤保险费。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e9aadb1f63024e34a14885585a223fa9","sort":1,"code":"A","content":"当地平均工资"},{"id":"1517719a0cda40b0ab282c74e67368d8","sort":2,"code":"B","content":"工资总额"},{"id":"af3b6737393c465599080524c7cce70d","sort":3,"code":"C","content":"以上皆可"},{"id":"bbe9b096e1b54c6a92643641bca1f5f6","sort":4,"code":"D","content":"项目工程总造价"}],"keywords":"null"},{"id":"68591","type":"001007","level":"003001","content":"用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3372645120c247f4b83b3120312dbd92","sort":1,"code":"A","content":"员工承诺，在本公司工作期间遵守规章制度"},{"id":"96175f4056be4936b13f9307e2eb2ae0","sort":2,"code":"B","content":"公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理"},{"id":"107b86939e514a7f8f50b7d96b2507a1","sort":3,"code":"C","content":"员工自愿承诺，在本公司工作期间不结婚"},{"id":"741b8f627d864ab3999fe4d9cea6ae87","sort":4,"code":"D","content":"按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"38ac1534bac04628b824eee9c740e6ed","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"57d05cea438c42ceabf4ec28047254c3","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":1,"code":"A","content":"1"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":2,"code":"B","content":"2"},{"id":"394106514712430bad66fd4bf853deb1","sort":3,"code":"C","content":"3"},{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b34b2d30e563409e9615ece5765d7739","sort":1,"code":"A","content":"9；3；4"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":2,"code":"B","content":"10；5；6"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":3,"code":"C","content":"10；4；5"},{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":4,"code":"D","content":"9；2；3"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":1,"code":"A","content":"补贴标准根据乡村生活费用确定"},{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":2,"code":"B","content":"应当为安置人员购买意外伤害商业保险"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":3,"code":"C","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":4,"code":"D","content":"可以签订劳动合同也可以签订劳务协议"}],"keywords":"null"},{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":1,"code":"A","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"},{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":2,"code":"B","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"},{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":3,"code":"C","content":"具有互联网工作经验优先"},{"id":"cd44e594750548e8a9b814d8744f4121","sort":4,"code":"D","content":"需要经常出差，男士优先"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":1,"code":"A","content":"8"},{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":2,"code":"B","content":"10"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":3,"code":"C","content":"12"},{"id":"8e5fd62e7b12443db02196646c2f3315","sort":4,"code":"D","content":"5"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":1,"code":"A","content":"在居住地参加社会保险"},{"id":"a1b641859d98482e920a476122b69775","sort":2,"code":"B","content":"可以参加职工基本养老保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":3,"code":"C","content":"可以参加职工基本医疗保险"},{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":4,"code":"D","content":"在注册地参加社会保险"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2c3304f118214840a8944ef614188916","sort":1,"code":"A","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"},{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":2,"code":"B","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"},{"id":"4f9b228b803e481b9aed1047772b5845","sort":3,"code":"C","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":4,"code":"D","content":"按照本人工资的60%支付伤残津贴"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":1,"code":"A","content":"山东"},{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":2,"code":"B","content":"职工户籍所在地"},{"id":"55180558f6bc48c5bebed340833a779f","sort":3,"code":"C","content":"天津"},{"id":"b2b033f986284933a47b14d742bfa453","sort":4,"code":"D","content":"北京"}],"keywords":"null"},{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5041b2322d4e46ecb88c5ee258187797","sort":1,"code":"A","content":"伤残津贴"},{"id":"1161f371d32547158ebc4d0779992cde","sort":2,"code":"B","content":"6个月本人工资的丧葬补助金"},{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":3,"code":"C","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"},{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":4,"code":"D","content":"一次性工亡补助金"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f741138316654c55b9c78bf21488a952","sort":1,"code":"A","content":"10000元"},{"id":"16f20c281c794a91a6c95a3b39906a17","sort":2,"code":"B","content":"30000元"},{"id":"f507bc94dcde431cb1b0717eef448115","sort":3,"code":"C","content":"40000元"},{"id":"25f07a9858854902a7f5513177500991","sort":4,"code":"D","content":"60000元"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"adfa6de440ea42a588db9548679b987a","sort":1,"code":"A","content":"不属于仲裁委员会受理争议范围"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":2,"code":"B","content":"超出规定的仲裁审查申请期间的"},{"id":"f1a18478c3554009833aa2d6993ded3a","sort":3,"code":"C","content":"不属于本仲裁委员会管辖"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":4,"code":"D","content":"不属于本仲裁委员会管辖"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":1,"code":"A","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"},{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":2,"code":"B","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"},{"id":"d4c856b634ba4590b329500c0fd45234","sort":3,"code":"C","content":"罚款金额最高不得超过5万元"},{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":4,"code":"D","content":"罚款金额为违法所得的50%至200%"}],"keywords":"null"},{"id":"68618","type":"001007","level":"003001","content":"甲公司介绍三名13周岁未成年人到乙公司工作。甲公司应被罚款(    )元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"91dd009201e2490a924cab882346306d","sort":1,"code":"A","content":"4000"},{"id":"d40b2572feab4410b822d497ee817674","sort":2,"code":"B","content":"15000"},{"id":"f8fee2535baa4419bb4bf460573f232a","sort":3,"code":"C","content":"8000"},{"id":"fc2a44ec470d4c389cd50befa6053a2a","sort":4,"code":"D","content":"10000"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":1,"code":"A","content":"50"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":2,"code":"B","content":"5"},{"id":"03b1512043044934a2d266cff87749f7","sort":3,"code":"C","content":"4"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":4,"code":"D","content":"40"}],"keywords":"null"},{"id":"68604","type":"001007","level":"003001","content":"职称评审委员会评审专家应当具备的条件是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"81cf1c608d3c4bdc93132ae6628e52ac","sort":1,"code":"A","content":"本职称系列或者专业相应层级的职称"},{"id":"da2f030fb71e4d2da7b4c5b08e522d9f","sort":2,"code":"B","content":"年龄不超过65周"},{"id":"f8ec40175498465794628d3e215aafc9","sort":3,"code":"C","content":"从事本领域专业技术工作"},{"id":"9a5838e7b40042d995e4fe69cb34086a","sort":4,"code":"D","content":"良好的职业道德"}],"keywords":"null"},{"id":"68596","type":"001007","level":"003001","content":"对公益性岗位安置就业困难人员给予（    ）补贴，补贴标准参照当地最低工资标准执行。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"75cff79c4fa4442984d5b9b8cd41f29c","sort":1,"code":"A","content":"生活"},{"id":"fffaae54e22b4080a0cdd4b54084847f","sort":2,"code":"B","content":"交通"},{"id":"24867d24ce5a467e9d86aa5e02d16624","sort":3,"code":"C","content":"救济"},{"id":"fd638b2f28974d8bb2e636ba9c6cabff","sort":4,"code":"D","content":"岗位"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":1,"code":"A","content":"四至六"},{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":2,"code":"B","content":"五至七"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":3,"code":"C","content":"六至八"},{"id":"e39693a21869498da8aa63f62ffaaa91","sort":4,"code":"D","content":"三至五"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"faed1327f3e646e5be24adc94103c3d7","sort":1,"code":"A","content":"正常运营5个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":2,"code":"B","content":"正常运营7个月"},{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":3,"code":"C","content":"正常运营3个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":4,"code":"D","content":"正常运营1个月"}],"keywords":"null"},{"id":"68568","type":"001007","level":"003001","content":"企业年金基金实行(    )，为每个参加企业年金的职工建立(    )账户，按照国家有关规定投资运营","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"470088804e84487cacee7b3dba040eff","sort":1,"code":"A","content":"部分积累；统筹"},{"id":"9afce32f3f77465d9609afe5a1753be1","sort":2,"code":"B","content":"部分积累；个人"},{"id":"d0a70c4107fc4b84833e6d569b1cfb55","sort":3,"code":"C","content":"完全积累；统筹"},{"id":"2b00cc5fbeab473f81afdef2be929b0b","sort":4,"code":"D","content":"完全积累；个人"}],"keywords":"null"},{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f021e857a2dc490caeb862efdbe11e28","sort":1,"code":"A","content":"单位择优使用"},{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":2,"code":"B","content":"政府依法认定"},{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":3,"code":"C","content":"业内公正评价"},{"id":"37617262af704c8a9268a3f473b5ba53","sort":4,"code":"D","content":"个人自主申报"}],"keywords":"null"},{"id":"68620","type":"001007","level":"003001","content":"在办理机关事业单位职业年金转移接续时，无需转移的基金项目包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4038e407cd32415e941dc64bc86f7969","sort":1,"code":"A","content":"个人缴费本息"},{"id":"cc0fe7a8998f46a4b1392c42b28a687a","sort":2,"code":"B","content":"缴费形成的职业年金"},{"id":"83c5e0f5fd124299b2aadccc4da44c6e","sort":3,"code":"C","content":"原转入的企业年金"},{"id":"f7c56f8bb62f4a2eae54ee2e7da8edff","sort":4,"code":"D","content":"补记的职业年金"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"659b0e46772647ffb997df394f735d00","sort":1,"code":"A","content":"上一年度全国城镇居民人均可支配收入"},{"id":"a7ae703580c542398303612d32f10288","sort":2,"code":"B","content":"上一年度全省城镇居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":3,"code":"C","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"},{"id":"da0164df20a6444ea9c06df863038525","sort":4,"code":"D","content":"上一年度全国居民人均可支配收入"}],"keywords":"null"},{"id":"68586","type":"001007","level":"003001","content":"《职业年金基金管理暂行办法》规定，(    )是指接受受托人委托投资管理职业年金基金财产的专业机构。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f91cd557c0454e90807926a4ac38a909","sort":1,"code":"A","content":"投资管理人"},{"id":"b14de9c6fd2d4d4287d3ecfb43a24b0f","sort":2,"code":"B","content":"受托人"},{"id":"ba109ee6879246269a64d7ec24a58c46","sort":3,"code":"C","content":"托管人"},{"id":"fcb82e17cf9d4a1ca637084fdf3224ce","sort":4,"code":"D","content":"代理人"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":1,"code":"A","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":2,"code":"B","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":3,"code":"C","content":"与档案接收机构协商，想办法为小李办理。"},{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":4,"code":"D","content":"按照小李的要求为其办理转正定级手续"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":1,"code":"A","content":"职工一方协商代表资格是否符合国家有关规定"},{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":2,"code":"B","content":"补充保险和福利约定是否符合国家有关规"},{"id":"d76d9d824b1348c190e381f06a178776","sort":3,"code":"C","content":"协商程序是否履行《集体合同规定》所规定的具体程序"},{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":4,"code":"D","content":"集体合同约定的工资增幅是否合理"}],"keywords":"null"},{"id":"68560","type":"001007","level":"003001","content":"（    ）参加劳动预备制培训的，可以享受一定标准的生活费补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2050b405c33d4e62882bb572311fc967","sort":1,"code":"A","content":"困难家庭学员"},{"id":"6f9319af9c2c4dbbac85f623eb4cd331","sort":2,"code":"B","content":"城市低保家庭学员"},{"id":"0336f625724641558e729178184964c5","sort":3,"code":"C","content":"应届初高中毕业生"},{"id":"c9efc2fba21f4e0d8ab0f96d8fa16667","sort":4,"code":"D","content":"农村学员"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":1,"code":"A","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":2,"code":"B","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":3,"code":"C","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":4,"code":"D","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"}],"keywords":"null"},{"id":"68614","type":"001007","level":"003001","content":"企业裁减人员时，依法应当优先留用（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1fd8155b7ba64462ab9c9bd68a31a9ab","sort":1,"code":"A","content":"家庭有需要扶养的老人"},{"id":"77f2089cced8489a8c83c2ef45b7d43c","sort":2,"code":"B","content":"与本单位订立8年期限劳动合同的人员"},{"id":"8742eccd8e41413688b3941288fc3c41","sort":3,"code":"C","content":"与本单位订立无固定期限劳动合同的人员"},{"id":"23b4206865ef40298f20596679a00de0","sort":4,"code":"D","content":"掌握企业核心技术、对企业发展至关重要的人员"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"01c6716d57234e98960251fb42e1d28e","sort":1,"code":"A","content":"民事权"},{"id":"a6937611ca064abfb27cba90c8064169","sort":2,"code":"B","content":"入境权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":3,"code":"C","content":"定居权"},{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":4,"code":"D","content":"工作权"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f6cf14fd2b249109922524a550c021b","sort":1,"code":"A","content":"个人自带"},{"id":"3ae4a91f95a049629966229077ae4831","sort":2,"code":"B","content":"可以弃档不管"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":3,"code":"C","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":4,"code":"D","content":"可直接从学校转递到企业"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"0a552d4343a044648aa59cb70df04f39","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":1,"code":"A","content":"7个"},{"id":"713eaa07fb8042eea09409619ff0f619","sort":2,"code":"B","content":"8个"},{"id":"8df6381555cb4de9883763e7239ed809","sort":3,"code":"C","content":"6个"},{"id":"88f1f34a065f44dea656d7797a9edc11","sort":4,"code":"D","content":"5个"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68627","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1be729e13a1945bab354d0faf4c3492c","sort":1,"code":"A","content":"正确"},{"id":"ce4efa5b214748c78c355df38da717a2","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68634","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;女职工禁忌从事的劳动范围，可分类为经期禁忌从事的劳动范围、孕期禁忌从事的劳动范围和哺乳期禁忌从事的劳动范围三类&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3c1e199c66514c968fc690b4e01f3cdb","sort":1,"code":"A","content":"错误"},{"id":"82f483abf09142d8b6a69b29ebafadd7","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68629","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位的隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3f3bb9efec414414930731eea2e812a1","sort":1,"code":"A","content":"正确"},{"id":"bc4688d2e71b4c7cb641d78bd9022cbb","sort":2,"code":"B","content":"错误"}],"keywords":"null"}]}]},"code":"SUCCESS"}
json_0627_answer2 = {"httpStatus":"OK","status":0,"message":"成功","data":[{"id":"68723","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对于消杀防疫、保洁环卫等临时性公益岗位，根据工作任务和工作时间，给予一定的岗位补贴和社会保险补贴，补贴期限最长不超过（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）个月。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9f9527074b2f45a68a54fecfb938b402","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"},{"id":"0c0e8fb4121b4399832df59d6534cb05","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"},{"id":"72cd2c8aac9e49fa94bc5fc4f351682f","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"},{"id":"838276c3b20e40b592f138faded1ffab","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;7&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68593","type":"001007","level":"003001","content":"无法进行失业登记的人员包括(    )","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"709fbe517f27498a837fd51f6e23730f","sort":1,"code":"A","content":"年满16周岁，从各类学校毕业、肄业的"},{"id":"abc9ac31fc81493a87535e02f62700c2","sort":2,"code":"B","content":"退出现役军人"},{"id":"d3f9679e86b348109957df6809b90dd5","sort":3,"code":"C","content":"个体工商户业主或私营企业业主停业、破产停止经营的"},{"id":"097dc10304544df2ac34a71a406871e5","sort":4,"code":"D","content":"刑满释放人员"}],"keywords":"null"},{"id":"68608","type":"001007","level":"003001","content":"博士后设站单位可以将在站博士后予以退站的情形包括（   ）。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0bc09acfdb2742a1952906a39c23afd7","sort":1,"code":"A","content":"进站一年仍未取得国家承认的博士学位证书的"},{"id":"fe600c99ad2f409396e87e26c02b01e0","sort":2,"code":"B","content":"提供虚假材料获得进站资格的"},{"id":"cf8aa510cd684d9a932ef0d10284a4a9","sort":3,"code":"C","content":"因患病等原因难以完成工作的"},{"id":"b6a870373e994075884b5516965e7050","sort":4,"code":"D","content":"出国逾期不归超过15日的"}],"keywords":"null"},{"id":"68574","type":"001007","level":"003001","content":"老王在领取失业保险金期间因达到退休年龄办理了退休手续，并开始领取养老金。那么(    )","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"51829768776847d1995a7bf0331eedc6","sort":1,"code":"A","content":"他可以继续领取剩余的失业保险金"},{"id":"5c9fb3c9a8704de88fd7be3be4cab922","sort":2,"code":"B","content":"他可以再领取一个月的失业保险金"},{"id":"73f7985a40e6455786c037381bf05164","sort":3,"code":"C","content":"他不可以继续领失业保险金"},{"id":"0dc709dd74274fedbb89a08feb023003","sort":4,"code":"D","content":"他不可以继续领失业保险金，但可以享受其他失业保险待遇"}],"keywords":"null"},{"id":"68624","type":"001007","level":"003001","content":"根据《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》，严重失信、失范行为包括（    ）","answer":"A,B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"42e37dfb02bf4ffcb42f2a8c48234005","sort":1,"code":"A","content":"非法获取社保个人权益数据的"},{"id":"b4b68d4fccf44ed484f8a7922ea94cd5","sort":2,"code":"B","content":"社保服务机构违反服务协议的"},{"id":"c937f322d72945d6be8d65d0d3edc7e4","sort":3,"code":"C","content":"应缴纳社会保险费却拒不缴纳的"},{"id":"14af74be5a8c4080ae67f4d0a37e7dc0","sort":4,"code":"D","content":"隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的"}],"keywords":"null"},{"id":"68576","type":"001007","level":"003001","content":"以建设项目为单位参保的建筑企业，可以按照(    )的一定比例计算缴纳工伤保险费。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1517719a0cda40b0ab282c74e67368d8","sort":1,"code":"A","content":"工资总额"},{"id":"bbe9b096e1b54c6a92643641bca1f5f6","sort":2,"code":"B","content":"项目工程总造价"},{"id":"e9aadb1f63024e34a14885585a223fa9","sort":3,"code":"C","content":"当地平均工资"},{"id":"af3b6737393c465599080524c7cce70d","sort":4,"code":"D","content":"以上皆可"}],"keywords":"null"},{"id":"68634","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;女职工禁忌从事的劳动范围，可分类为经期禁忌从事的劳动范围、孕期禁忌从事的劳动范围和哺乳期禁忌从事的劳动范围三类&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"82f483abf09142d8b6a69b29ebafadd7","sort":1,"code":"A","content":"正确"},{"id":"3c1e199c66514c968fc690b4e01f3cdb","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"394106514712430bad66fd4bf853deb1","sort":2,"code":"B","content":"3"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":3,"code":"C","content":"2"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a1b641859d98482e920a476122b69775","sort":1,"code":"A","content":"可以参加职工基本养老保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":2,"code":"B","content":"可以参加职工基本医疗保险"},{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":3,"code":"C","content":"在注册地参加社会保险"},{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":4,"code":"D","content":"在居住地参加社会保险"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":1,"code":"A","content":"职工户籍所在地"},{"id":"b2b033f986284933a47b14d742bfa453","sort":2,"code":"B","content":"北京"},{"id":"55180558f6bc48c5bebed340833a779f","sort":3,"code":"C","content":"天津"},{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":4,"code":"D","content":"山东"}],"keywords":"null"},{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":1,"code":"A","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"},{"id":"1161f371d32547158ebc4d0779992cde","sort":2,"code":"B","content":"6个月本人工资的丧葬补助金"},{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":3,"code":"C","content":"一次性工亡补助金"},{"id":"5041b2322d4e46ecb88c5ee258187797","sort":4,"code":"D","content":"伤残津贴"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"25f07a9858854902a7f5513177500991","sort":1,"code":"A","content":"60000元"},{"id":"f507bc94dcde431cb1b0717eef448115","sort":2,"code":"B","content":"40000元"},{"id":"16f20c281c794a91a6c95a3b39906a17","sort":3,"code":"C","content":"30000元"},{"id":"f741138316654c55b9c78bf21488a952","sort":4,"code":"D","content":"10000元"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"A,B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":1,"code":"A","content":"罚款金额为违法所得的50%至200%"},{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":2,"code":"B","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"},{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":3,"code":"C","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"},{"id":"d4c856b634ba4590b329500c0fd45234","sort":4,"code":"D","content":"罚款金额最高不得超过5万元"}],"keywords":"null"},{"id":"68618","type":"001007","level":"003001","content":"甲公司介绍三名13周岁未成年人到乙公司工作。甲公司应被罚款(    )元。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"91dd009201e2490a924cab882346306d","sort":1,"code":"A","content":"4000"},{"id":"f8fee2535baa4419bb4bf460573f232a","sort":2,"code":"B","content":"8000"},{"id":"fc2a44ec470d4c389cd50befa6053a2a","sort":3,"code":"C","content":"10000"},{"id":"d40b2572feab4410b822d497ee817674","sort":4,"code":"D","content":"15000"}],"keywords":"null"},{"id":"68596","type":"001007","level":"003001","content":"对公益性岗位安置就业困难人员给予（    ）补贴，补贴标准参照当地最低工资标准执行。","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fd638b2f28974d8bb2e636ba9c6cabff","sort":1,"code":"A","content":"岗位"},{"id":"fffaae54e22b4080a0cdd4b54084847f","sort":2,"code":"B","content":"交通"},{"id":"75cff79c4fa4442984d5b9b8cd41f29c","sort":3,"code":"C","content":"生活"},{"id":"24867d24ce5a467e9d86aa5e02d16624","sort":4,"code":"D","content":"救济"}],"keywords":"null"},{"id":"68568","type":"001007","level":"003001","content":"企业年金基金实行(    )，为每个参加企业年金的职工建立(    )账户，按照国家有关规定投资运营","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2b00cc5fbeab473f81afdef2be929b0b","sort":1,"code":"A","content":"完全积累；个人"},{"id":"9afce32f3f77465d9609afe5a1753be1","sort":2,"code":"B","content":"部分积累；个人"},{"id":"d0a70c4107fc4b84833e6d569b1cfb55","sort":3,"code":"C","content":"完全积累；统筹"},{"id":"470088804e84487cacee7b3dba040eff","sort":4,"code":"D","content":"部分积累；统筹"}],"keywords":"null"},{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"37617262af704c8a9268a3f473b5ba53","sort":1,"code":"A","content":"个人自主申报"},{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":2,"code":"B","content":"业内公正评价"},{"id":"f021e857a2dc490caeb862efdbe11e28","sort":3,"code":"C","content":"单位择优使用"},{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":4,"code":"D","content":"政府依法认定"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a7ae703580c542398303612d32f10288","sort":1,"code":"A","content":"上一年度全省城镇居民人均可支配收入"},{"id":"da0164df20a6444ea9c06df863038525","sort":2,"code":"B","content":"上一年度全国居民人均可支配收入"},{"id":"659b0e46772647ffb997df394f735d00","sort":3,"code":"C","content":"上一年度全国城镇居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":4,"code":"D","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"}],"keywords":"null"},{"id":"68586","type":"001007","level":"003001","content":"《职业年金基金管理暂行办法》规定，(    )是指接受受托人委托投资管理职业年金基金财产的专业机构。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fcb82e17cf9d4a1ca637084fdf3224ce","sort":1,"code":"A","content":"代理人"},{"id":"b14de9c6fd2d4d4287d3ecfb43a24b0f","sort":2,"code":"B","content":"受托人"},{"id":"ba109ee6879246269a64d7ec24a58c46","sort":3,"code":"C","content":"托管人"},{"id":"f91cd557c0454e90807926a4ac38a909","sort":4,"code":"D","content":"投资管理人"}],"keywords":"null"},{"id":"68560","type":"001007","level":"003001","content":"（    ）参加劳动预备制培训的，可以享受一定标准的生活费补贴。","answer":"A,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c9efc2fba21f4e0d8ab0f96d8fa16667","sort":1,"code":"A","content":"农村学员"},{"id":"2050b405c33d4e62882bb572311fc967","sort":2,"code":"B","content":"困难家庭学员"},{"id":"0336f625724641558e729178184964c5","sort":3,"code":"C","content":"应届初高中毕业生"},{"id":"6f9319af9c2c4dbbac85f623eb4cd331","sort":4,"code":"D","content":"城市低保家庭学员"}],"keywords":"null"},{"id":"68614","type":"001007","level":"003001","content":"企业裁减人员时，依法应当优先留用（    ）。","answer":"A,B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"77f2089cced8489a8c83c2ef45b7d43c","sort":1,"code":"A","content":"与本单位订立8年期限劳动合同的人员"},{"id":"8742eccd8e41413688b3941288fc3c41","sort":2,"code":"B","content":"与本单位订立无固定期限劳动合同的人员"},{"id":"23b4206865ef40298f20596679a00de0","sort":3,"code":"C","content":"掌握企业核心技术、对企业发展至关重要的人员"},{"id":"1fd8155b7ba64462ab9c9bd68a31a9ab","sort":4,"code":"D","content":"家庭有需要扶养的老人"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"0a552d4343a044648aa59cb70df04f39","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68629","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位的隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3f3bb9efec414414930731eea2e812a1","sort":1,"code":"A","content":"正确"},{"id":"bc4688d2e71b4c7cb641d78bd9022cbb","sort":2,"code":"B","content":"错误"}],"keywords":"null"}],"code":"SUCCESS"}

json_0627_test3 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"305967ca85db49f5ab2468c7e6d32966","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599190,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68722","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对&amp;2526lt;/span&amp;2526gt;2020年3月至12月，领取失业保险金期满仍未就业的失业人员、不符合领取失业保险金条件的参保失业人员，发放（ &nbsp;&nbsp;）个月的失业补助金，标准不高于当地失业保险金的（ &nbsp;&nbsp;&nbsp;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b49f0e5f79a8463cbb91d053a19a69cc","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"7383c2af02604820b6882b632b404923","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c2c76fcab56746099f6e0020afb20110","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"d8243054793d442c9577daac5446188a","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"583b9bc056c641ffa095ef97015a8380","sort":1,"code":"A","content":"常住地；出生地"},{"id":"5a22297e9c5e42588338374f2db13853","sort":2,"code":"B","content":"出生地；户籍地"},{"id":"c663276dfd0b4d2c93e4177521a14071","sort":3,"code":"C","content":"原单位注册地；常住地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":4,"code":"D","content":"常住地；常住地"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":1,"code":"A","content":"在注册地参加社会保险"},{"id":"a1b641859d98482e920a476122b69775","sort":2,"code":"B","content":"可以参加职工基本养老保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":3,"code":"C","content":"可以参加职工基本医疗保险"},{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":4,"code":"D","content":"在居住地参加社会保险"}],"keywords":"null"},{"id":"68597","type":"001007","level":"003001","content":"属于高校毕业生基层服务项目的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a3d35ea01e424f67ac8b84525f318ca7","sort":1,"code":"A","content":"“三支一扶”计划"},{"id":"1c1f46c89b06468eb1497d0825bd0658","sort":2,"code":"B","content":"志愿服务西部计划"},{"id":"b8f6e68bbba84a7ba269bfaefaefe9c3","sort":3,"code":"C","content":"“凤凰飞翔”计划"},{"id":"a9983ec2a62b48e9915eb0112bc48a3c","sort":4,"code":"D","content":"公益就业行动计划"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"da0164df20a6444ea9c06df863038525","sort":1,"code":"A","content":"上一年度全国居民人均可支配收入"},{"id":"a7ae703580c542398303612d32f10288","sort":2,"code":"B","content":"上一年度全省城镇居民人均可支配收入"},{"id":"659b0e46772647ffb997df394f735d00","sort":3,"code":"C","content":"上一年度全国城镇居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":4,"code":"D","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":1,"code":"A","content":"10"},{"id":"8e5fd62e7b12443db02196646c2f3315","sort":2,"code":"B","content":"5"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":3,"code":"C","content":"8"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":4,"code":"D","content":"12"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5bf34b901e04adeb4129feb04f01116","sort":1,"code":"A","content":"195"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":3,"code":"C","content":"145"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":4,"code":"D","content":"139"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"16f20c281c794a91a6c95a3b39906a17","sort":1,"code":"A","content":"30000元"},{"id":"f507bc94dcde431cb1b0717eef448115","sort":2,"code":"B","content":"40000元"},{"id":"25f07a9858854902a7f5513177500991","sort":3,"code":"C","content":"60000元"},{"id":"f741138316654c55b9c78bf21488a952","sort":4,"code":"D","content":"10000元"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1e922892adfa4cc291ccc8e08086313f","sort":1,"code":"A","content":"6000元"},{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":2,"code":"B","content":"4000元"},{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":3,"code":"C","content":"8000元"},{"id":"1045b445dbf340f992680615412a2c36","sort":4,"code":"D","content":"10000元"}],"keywords":"null"},{"id":"68565","type":"001007","level":"003001","content":"企业职工基本养老保险中央调剂基金由各省份养老保险基金上解的资金构成。按照各省份职工平均工资的(    )和在职应参保人数作为计算上解额的基数，上解比例从(    )起步，逐步提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6cce8cd0ef46464fac76fea4b3041cff","sort":1,"code":"A","content":"90%；3.5%"},{"id":"43ddec4cd71e4923a09e3b8898825e74","sort":2,"code":"B","content":"80%；3.5%"},{"id":"eda8f0ab8ad4412db86793bebc83f28d","sort":3,"code":"C","content":"80%；3%"},{"id":"79e7d517e5c14955af8ca6803e8d180a","sort":4,"code":"D","content":"90%；3%"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":1,"code":"A","content":"7个"},{"id":"88f1f34a065f44dea656d7797a9edc11","sort":2,"code":"B","content":"5个"},{"id":"8df6381555cb4de9883763e7239ed809","sort":3,"code":"C","content":"6个"},{"id":"713eaa07fb8042eea09409619ff0f619","sort":4,"code":"D","content":"8个"}],"keywords":"null"},{"id":"68567","type":"001007","level":"003001","content":"按照现行企业年金制度，某企业当年年度工资总额为500万元，该企业当年度缴纳企业年金的额度，不符合规定的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d6da7cd4c58e4d47966177125dc00cf6","sort":1,"code":"A","content":"80万元"},{"id":"e1171cc6d05742a18d04fb02b1fcfcc8","sort":2,"code":"B","content":"20万元"},{"id":"f0c637e8214e4881b3a497b10801045a","sort":3,"code":"C","content":"40万元"},{"id":"62ff517715bf4207a464dfc56e981f84","sort":4,"code":"D","content":"100万元"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f6cf14fd2b249109922524a550c021b","sort":1,"code":"A","content":"个人自带"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":2,"code":"B","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":3,"code":"C","content":"可直接从学校转递到企业"},{"id":"3ae4a91f95a049629966229077ae4831","sort":4,"code":"D","content":"可以弃档不管"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":1,"code":"A","content":"60000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":2,"code":"B","content":"96000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":3,"code":"C","content":"84000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":4,"code":"D","content":"108000元"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"55180558f6bc48c5bebed340833a779f","sort":1,"code":"A","content":"天津"},{"id":"b2b033f986284933a47b14d742bfa453","sort":2,"code":"B","content":"北京"},{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":3,"code":"C","content":"职工户籍所在地"},{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":4,"code":"D","content":"山东"}],"keywords":"null"},{"id":"68585","type":"001007","level":"003001","content":"企业年金养老金产品投资管理人应当接受份额持有人和(    )的监督。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0ba7f9932f4d49dbbc769575c5a16bf8","sort":1,"code":"A","content":"托管人"},{"id":"31ce5c02f25c48a282d1bd33c108d29f","sort":2,"code":"B","content":"账管人"},{"id":"e734ff275d68469ebc3463c80771c3a8","sort":3,"code":"C","content":"代理人"},{"id":"6ba5033a73fb44bf85c943bf3d2f3520","sort":4,"code":"D","content":"受托人"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c344b8652c604917b8df2f26adf68344","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8ada3e4200ed486aa248102ccddecad0","sort":1,"code":"A","content":"2022"},{"id":"d393b9f42b594346bacf7e7db5375709","sort":2,"code":"B","content":"2020"},{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":3,"code":"C","content":"2021"},{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":4,"code":"D","content":"2023"}],"keywords":"null"},{"id":"68582","type":"001007","level":"003001","content":"老王因工伤生活不能自理，现停工留薪期需要护理。老王的（   ）可以从工伤保险基金支出。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ad60dee7c6a1413b9b8ee7555bd84922","sort":1,"code":"A","content":"伙食补助费"},{"id":"5a143c14dde44889bb20d45be1c5adf5","sort":2,"code":"B","content":"生活护理费"},{"id":"bd8a68d0a39b4dd8bb431ded378294b9","sort":3,"code":"C","content":"赴统筹地区以外就医所需交通、食宿费"},{"id":"66b9b5278b7d4a428a4e2f9f6d307925","sort":4,"code":"D","content":"工伤医疗待遇"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":1,"code":"A","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":2,"code":"B","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"377c82a0fae341139629ddee8f6a400e","sort":3,"code":"C","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":4,"code":"D","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":1,"code":"A","content":"经人力资源社会保障部门授权的单位"},{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":2,"code":"B","content":"省级公共就业和人才服务机构"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":3,"code":"C","content":"县级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":4,"code":"D","content":"流动人员本人"}],"keywords":"null"},{"id":"68577","type":"001007","level":"003001","content":"社会保险行政部门应当自工伤认定决定作出之日起(    )日内，将《认定工伤决定书》或者《不予认定工伤决定书》送达受伤害职工（或者其近亲属）和用人单位。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8d58775a231d418183c6215ee073f126","sort":1,"code":"A","content":"10"},{"id":"f4022fc1650c4d3097978fa1790d1b67","sort":2,"code":"B","content":"20"},{"id":"b98281b1df4c496a8e51e77baad9b1ba","sort":3,"code":"C","content":"30"},{"id":"6a08fed453aa4474ac518f54fa380e30","sort":4,"code":"D","content":"60"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":1,"code":"A","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":2,"code":"B","content":"按照小李的要求为其办理转正定级手续"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":3,"code":"C","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":4,"code":"D","content":"与档案接收机构协商，想办法为小李办理。"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"01107e15e02e4d2f96538f9313d5170f","sort":1,"code":"A","content":"重点情况说明"},{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":2,"code":"B","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":3,"code":"C","content":"备案函"},{"id":"97366b5104d6412895f3f301041881f1","sort":4,"code":"D","content":"职工（代表）大会决议"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e3125d07cd0446a89213ec98e18812ab","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bcbfd8add87943f0ace414c4194d3546","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":1,"code":"A","content":"贫困家庭子女"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":2,"code":"B","content":"农村转移就业劳动者"},{"id":"5d3526a8261343468d01869caa805ef4","sort":3,"code":"C","content":"毕业年度高校毕业生"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":4,"code":"D","content":"城镇登记失业人员"}],"keywords":"null"},{"id":"68611","type":"001007","level":"003001","content":"用人单位有下列（    ）情形的，劳动者可以解除劳动合同。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"dc6c86086ec541daa0696055a59ed2b1","sort":1,"code":"A","content":"未按照劳动合同约定提供劳动保护的"},{"id":"650abb015d27483490fe7e4888278af8","sort":2,"code":"B","content":"未依法为劳动者购买意外伤害险的"},{"id":"80e05fb12f1344fbba2f0776f4d6831c","sort":3,"code":"C","content":"未及时足额支付劳动者工资的"},{"id":"c34ef1a7fe764b34bc462de3915eef12","sort":4,"code":"D","content":"根据经营需要，与劳动者协商加班的"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e39693a21869498da8aa63f62ffaaa91","sort":1,"code":"A","content":"三至五"},{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":2,"code":"B","content":"四至六"},{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":3,"code":"C","content":"五至七"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":4,"code":"D","content":"六至八"}],"keywords":"null"},{"id":"68586","type":"001007","level":"003001","content":"《职业年金基金管理暂行办法》规定，(    )是指接受受托人委托投资管理职业年金基金财产的专业机构。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ba109ee6879246269a64d7ec24a58c46","sort":1,"code":"A","content":"托管人"},{"id":"fcb82e17cf9d4a1ca637084fdf3224ce","sort":2,"code":"B","content":"代理人"},{"id":"b14de9c6fd2d4d4287d3ecfb43a24b0f","sort":3,"code":"C","content":"受托人"},{"id":"f91cd557c0454e90807926a4ac38a909","sort":4,"code":"D","content":"投资管理人"}],"keywords":"null"},{"id":"68566","type":"001007","level":"003001","content":"在我国就业的外国人领取养老保险待遇的年龄，原则上执行(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a59921796e884cf9a15f6a87c6beb649","sort":1,"code":"A","content":"我国退休年龄政策，如果属于与我国签订社会保险缴费双边或多边协议的国家，则执行该国退休年龄政策"},{"id":"06e499fbbc6c467d85fcd66f8ec81222","sort":2,"code":"B","content":"我国退休年龄政策"},{"id":"c201c3f515044f70abba35079d08948a","sort":3,"code":"C","content":"外国人国籍国退休年龄政策"},{"id":"660287329b444b84b0c26d2dc1fd909e","sort":4,"code":"D","content":"我国退休年龄政策，如果外国人国籍国退休年龄晚于我国退休年龄，则执行外国人国籍国退休年龄政策"}],"keywords":"null"},{"id":"68563","type":"001007","level":"003001","content":"职业年金个人账户记账利率根据(    )确定。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7601119a7b14918a6fa15e399479565","sort":1,"code":"A","content":"银行定期存款利率"},{"id":"5f597299fca34798b1bfe485a0b33c00","sort":2,"code":"B","content":"上年M1增幅"},{"id":"a0906be902af4316aeda40b6cc0cfddb","sort":3,"code":"C","content":"上年CPI增幅"},{"id":"78114bd83b2f484d9b214d2aec4c9940","sort":4,"code":"D","content":"实账积累部分的投资收益率"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"438022975c334265a21c2fffb7f465de","sort":1,"code":"A","content":"4"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":2,"code":"B","content":"6"},{"id":"a082cb3fdd534991930f4cb8693b9894","sort":3,"code":"C","content":"5"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":4,"code":"D","content":"7"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"0a552d4343a044648aa59cb70df04f39","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3413d86553634b5c958740b3ec761da0","sort":1,"code":"A","content":"制定企业年金基金战略资产配置策略"},{"id":"5f415af62962421ebe130734f5103ae3","sort":2,"code":"B","content":"安全保管企业年金基金财产"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":3,"code":"C","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":4,"code":"D","content":"及时办理清算、交割事宜"}],"keywords":"null"},{"id":"68600","type":"001007","level":"003001","content":"按照现行规定，面向个人发放的创业担保贷款期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cfb5ba55490b49fd91dd7d7e0a82de7d","sort":1,"code":"A","content":"1"},{"id":"414a064395064954a551f10efd6a73d9","sort":2,"code":"B","content":"3"},{"id":"24092da8dfdf4c9e910f8421d51e885c","sort":3,"code":"C","content":"2"},{"id":"d7d57727a08f4884950a0f667f43caf4","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68589","type":"001007","level":"003001","content":"参加职工基本养老保险的个人达到法定退休年龄时，累计缴费年限不足15年的，其养老待遇可以（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2dd32079db4a4387ba3623c41bbce584","sort":1,"code":"A","content":"可以申请转入户籍所在地城乡居民社会养老保险，享受相应的养老保险待遇"},{"id":"0930b9bb44fe49869d2d4e15045f9652","sort":2,"code":"B","content":"一次性趸缴至15年"},{"id":"28c4610eff3742c58279b142d12d75d0","sort":3,"code":"C","content":"个人可以书面申请终止职工基本养老保险关系。社保机构按照程序，经本人书面确认后，终止其职工养老保险关系，并将个人账户储存额一次性支付给本人"},{"id":"8dfbb022285d4dcf943839c49fe9c1a1","sort":4,"code":"D","content":"延长缴费至满15年，然后按月领取基本养老金（其中社会保险法实施前参保，延长缴费5年后仍不足15年的，延长缴费至满15年）"}],"keywords":"null"},{"id":"68618","type":"001007","level":"003001","content":"甲公司介绍三名13周岁未成年人到乙公司工作。甲公司应被罚款(    )元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f8fee2535baa4419bb4bf460573f232a","sort":1,"code":"A","content":"8000"},{"id":"91dd009201e2490a924cab882346306d","sort":2,"code":"B","content":"4000"},{"id":"fc2a44ec470d4c389cd50befa6053a2a","sort":3,"code":"C","content":"10000"},{"id":"d40b2572feab4410b822d497ee817674","sort":4,"code":"D","content":"15000"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":1,"code":"A","content":"正常运营3个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":2,"code":"B","content":"正常运营1个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":3,"code":"C","content":"正常运营5个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":4,"code":"D","content":"正常运营7个月"}],"keywords":"null"},{"id":"68723","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对于消杀防疫、保洁环卫等临时性公益岗位，根据工作任务和工作时间，给予一定的岗位补贴和社会保险补贴，补贴期限最长不超过（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）个月。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"72cd2c8aac9e49fa94bc5fc4f351682f","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"},{"id":"9f9527074b2f45a68a54fecfb938b402","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"},{"id":"0c0e8fb4121b4399832df59d6534cb05","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"},{"id":"838276c3b20e40b592f138faded1ffab","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;7&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f1a18478c3554009833aa2d6993ded3a","sort":1,"code":"A","content":"不属于本仲裁委员会管辖"},{"id":"adfa6de440ea42a588db9548679b987a","sort":2,"code":"B","content":"不属于仲裁委员会受理争议范围"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":3,"code":"C","content":"不属于本仲裁委员会管辖"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":4,"code":"D","content":"超出规定的仲裁审查申请期间的"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":1,"code":"A","content":"2"},{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":2,"code":"B","content":"4"},{"id":"394106514712430bad66fd4bf853deb1","sort":3,"code":"C","content":"3"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":1,"code":"A","content":"职工一方协商代表资格是否符合国家有关规定"},{"id":"d76d9d824b1348c190e381f06a178776","sort":2,"code":"B","content":"协商程序是否履行《集体合同规定》所规定的具体程序"},{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":3,"code":"C","content":"集体合同约定的工资增幅是否合理"},{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":4,"code":"D","content":"补充保险和福利约定是否符合国家有关规"}],"keywords":"null"},{"id":"68615","type":"001007","level":"003001","content":"关于女职工生育享受假期，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b2c58eb097ae4d81819fd9be7a8c39a5","sort":1,"code":"A","content":"女职工生育享受98天产假，其中产前只能休假10天"},{"id":"07f14be1e48f4ed6af0ba069010a9a12","sort":2,"code":"B","content":"女职工怀孕未满4个月流产的，享受15天产假"},{"id":"b05792b7d339491a8ae07be2266e7248","sort":3,"code":"C","content":"难产的，应增加产假15天；生育多胞胎的，每多生育1个婴儿，可增加产假10天"},{"id":"f49b1e597dfe4db58af159ca8f0a2d4e","sort":4,"code":"D","content":"怀孕满4个月流产的，享受48天产假"}],"keywords":"null"},{"id":"68624","type":"001007","level":"003001","content":"根据《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》，严重失信、失范行为包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b4b68d4fccf44ed484f8a7922ea94cd5","sort":1,"code":"A","content":"社保服务机构违反服务协议的"},{"id":"42e37dfb02bf4ffcb42f2a8c48234005","sort":2,"code":"B","content":"非法获取社保个人权益数据的"},{"id":"c937f322d72945d6be8d65d0d3edc7e4","sort":3,"code":"C","content":"应缴纳社会保险费却拒不缴纳的"},{"id":"14af74be5a8c4080ae67f4d0a37e7dc0","sort":4,"code":"D","content":"隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"38ac1534bac04628b824eee9c740e6ed","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"57d05cea438c42ceabf4ec28047254c3","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68556","type":"001007","level":"003001","content":"A省人才中心实行了档案接收告知承诺制，其在接收某企业员工小张的档案时，发现缺少核定小张学历学位的材料。该人才中心正确做法是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"7c3dba49ff6f4b128d475f7192c7fe73","sort":1,"code":"A","content":"与原单位协商退回并补充材料"},{"id":"cbbf941b0d784fa991ed21d2c952eb10","sort":2,"code":"B","content":"一次性告知所缺材料及其可能造成的影响，经本人作出书面知情说明、承诺补充材料后予以接收"},{"id":"bfd6c9e1fa7e406bb2942347175c6f48","sort":3,"code":"C","content":"一次性告知所缺材料及其可能造成的影响后，采取先存后补方式予以接收"},{"id":"3927d7aff6fa4c848316890cccf2f613","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":1,"code":"A","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":2,"code":"B","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":3,"code":"C","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":4,"code":"D","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68625","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照人社部财政部文件规定，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府投资开发的公益性岗位，只限安排符合岗位要求的就业困难人员。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"465813873edf45c891af7acde9fd4be3","sort":1,"code":"A","content":"正确"},{"id":"5e4791de7b8f4db8bb06008e5013ece6","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68630","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对违反劳动保障法律的行为，如发生在&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;年内&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，劳动保障行政部门应当依法受理。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2196c3eed8be4a8d84e88434598eb1e5","sort":1,"code":"A","content":"正确"},{"id":"123bdc965cb2468cb26bd23a7d2f42b3","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68632","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者依法享受探亲假、婚丧假、节育手术假等国家规定的假期间&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，视为正常劳动，但带薪年休假假期除外。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"24626dda34f14a6e9f995a0013ac89ff","sort":1,"code":"A","content":"正确"},{"id":"4e8385dc8c2842628b6006f8fecbe7c7","sort":2,"code":"B","content":"错误"}],"keywords":"null"}]}]},"code":"SUCCESS"}
json_0627_answer3 = {"httpStatus":"OK","status":0,"message":"成功","data":[{"id":"68625","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照人社部财政部文件规定，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府投资开发的公益性岗位，只限安排符合岗位要求的就业困难人员。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"465813873edf45c891af7acde9fd4be3","sort":1,"code":"A","content":"正确"},{"id":"5e4791de7b8f4db8bb06008e5013ece6","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68565","type":"001007","level":"003001","content":"企业职工基本养老保险中央调剂基金由各省份养老保险基金上解的资金构成。按照各省份职工平均工资的(    )和在职应参保人数作为计算上解额的基数，上解比例从(    )起步，逐步提高。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"eda8f0ab8ad4412db86793bebc83f28d","sort":1,"code":"A","content":"80%；3%"},{"id":"6cce8cd0ef46464fac76fea4b3041cff","sort":2,"code":"B","content":"90%；3.5%"},{"id":"43ddec4cd71e4923a09e3b8898825e74","sort":3,"code":"C","content":"80%；3.5%"},{"id":"79e7d517e5c14955af8ca6803e8d180a","sort":4,"code":"D","content":"90%；3%"}],"keywords":"null"},{"id":"68585","type":"001007","level":"003001","content":"企业年金养老金产品投资管理人应当接受份额持有人和(    )的监督。","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0ba7f9932f4d49dbbc769575c5a16bf8","sort":1,"code":"A","content":"托管人"},{"id":"31ce5c02f25c48a282d1bd33c108d29f","sort":2,"code":"B","content":"账管人"},{"id":"e734ff275d68469ebc3463c80771c3a8","sort":3,"code":"C","content":"代理人"},{"id":"6ba5033a73fb44bf85c943bf3d2f3520","sort":4,"code":"D","content":"受托人"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d393b9f42b594346bacf7e7db5375709","sort":1,"code":"A","content":"2020"},{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":2,"code":"B","content":"2021"},{"id":"8ada3e4200ed486aa248102ccddecad0","sort":3,"code":"C","content":"2022"},{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":4,"code":"D","content":"2023"}],"keywords":"null"},{"id":"68577","type":"001007","level":"003001","content":"社会保险行政部门应当自工伤认定决定作出之日起(    )日内，将《认定工伤决定书》或者《不予认定工伤决定书》送达受伤害职工（或者其近亲属）和用人单位。","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8d58775a231d418183c6215ee073f126","sort":1,"code":"A","content":"10"},{"id":"f4022fc1650c4d3097978fa1790d1b67","sort":2,"code":"B","content":"20"},{"id":"b98281b1df4c496a8e51e77baad9b1ba","sort":3,"code":"C","content":"30"},{"id":"6a08fed453aa4474ac518f54fa380e30","sort":4,"code":"D","content":"60"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":1,"code":"A","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":2,"code":"B","content":"备案函"},{"id":"01107e15e02e4d2f96538f9313d5170f","sort":3,"code":"C","content":"重点情况说明"},{"id":"97366b5104d6412895f3f301041881f1","sort":4,"code":"D","content":"职工（代表）大会决议"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"A,B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":1,"code":"A","content":"贫困家庭子女"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":2,"code":"B","content":"农村转移就业劳动者"},{"id":"5d3526a8261343468d01869caa805ef4","sort":3,"code":"C","content":"毕业年度高校毕业生"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":4,"code":"D","content":"城镇登记失业人员"}],"keywords":"null"},{"id":"68611","type":"001007","level":"003001","content":"用人单位有下列（    ）情形的，劳动者可以解除劳动合同。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"650abb015d27483490fe7e4888278af8","sort":1,"code":"A","content":"未依法为劳动者购买意外伤害险的"},{"id":"80e05fb12f1344fbba2f0776f4d6831c","sort":2,"code":"B","content":"未及时足额支付劳动者工资的"},{"id":"dc6c86086ec541daa0696055a59ed2b1","sort":3,"code":"C","content":"未按照劳动合同约定提供劳动保护的"},{"id":"c34ef1a7fe764b34bc462de3915eef12","sort":4,"code":"D","content":"根据经营需要，与劳动者协商加班的"}],"keywords":"null"},{"id":"68566","type":"001007","level":"003001","content":"在我国就业的外国人领取养老保险待遇的年龄，原则上执行(    )。","answer":"A","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"06e499fbbc6c467d85fcd66f8ec81222","sort":1,"code":"A","content":"我国退休年龄政策"},{"id":"a59921796e884cf9a15f6a87c6beb649","sort":2,"code":"B","content":"我国退休年龄政策，如果属于与我国签订社会保险缴费双边或多边协议的国家，则执行该国退休年龄政策"},{"id":"c201c3f515044f70abba35079d08948a","sort":3,"code":"C","content":"外国人国籍国退休年龄政策"},{"id":"660287329b444b84b0c26d2dc1fd909e","sort":4,"code":"D","content":"我国退休年龄政策，如果外国人国籍国退休年龄晚于我国退休年龄，则执行外国人国籍国退休年龄政策"}],"keywords":"null"},{"id":"68632","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者依法享受探亲假、婚丧假、节育手术假等国家规定的假期间&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，视为正常劳动，但带薪年休假假期除外。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"24626dda34f14a6e9f995a0013ac89ff","sort":1,"code":"A","content":"正确"},{"id":"4e8385dc8c2842628b6006f8fecbe7c7","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68563","type":"001007","level":"003001","content":"职业年金个人账户记账利率根据(    )确定。","answer":"D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7601119a7b14918a6fa15e399479565","sort":1,"code":"A","content":"银行定期存款利率"},{"id":"a0906be902af4316aeda40b6cc0cfddb","sort":2,"code":"B","content":"上年CPI增幅"},{"id":"5f597299fca34798b1bfe485a0b33c00","sort":3,"code":"C","content":"上年M1增幅"},{"id":"78114bd83b2f484d9b214d2aec4c9940","sort":4,"code":"D","content":"实账积累部分的投资收益率"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"B,C,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"438022975c334265a21c2fffb7f465de","sort":1,"code":"A","content":"4"},{"id":"a082cb3fdd534991930f4cb8693b9894","sort":2,"code":"B","content":"5"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":3,"code":"C","content":"6"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":4,"code":"D","content":"7"}],"keywords":"null"},{"id":"68589","type":"001007","level":"003001","content":"参加职工基本养老保险的个人达到法定退休年龄时，累计缴费年限不足15年的，其养老待遇可以（    ）。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0930b9bb44fe49869d2d4e15045f9652","sort":1,"code":"A","content":"一次性趸缴至15年"},{"id":"2dd32079db4a4387ba3623c41bbce584","sort":2,"code":"B","content":"可以申请转入户籍所在地城乡居民社会养老保险，享受相应的养老保险待遇"},{"id":"28c4610eff3742c58279b142d12d75d0","sort":3,"code":"C","content":"个人可以书面申请终止职工基本养老保险关系。社保机构按照程序，经本人书面确认后，终止其职工养老保险关系，并将个人账户储存额一次性支付给本人"},{"id":"8dfbb022285d4dcf943839c49fe9c1a1","sort":4,"code":"D","content":"延长缴费至满15年，然后按月领取基本养老金（其中社会保险法实施前参保，延长缴费5年后仍不足15年的，延长缴费至满15年）"}],"keywords":"null"},{"id":"68615","type":"001007","level":"003001","content":"关于女职工生育享受假期，错误的是（    ）。","answer":"A,B,D","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b2c58eb097ae4d81819fd9be7a8c39a5","sort":1,"code":"A","content":"女职工生育享受98天产假，其中产前只能休假10天"},{"id":"b05792b7d339491a8ae07be2266e7248","sort":2,"code":"B","content":"难产的，应增加产假15天；生育多胞胎的，每多生育1个婴儿，可增加产假10天"},{"id":"07f14be1e48f4ed6af0ba069010a9a12","sort":3,"code":"C","content":"女职工怀孕未满4个月流产的，享受15天产假"},{"id":"f49b1e597dfe4db58af159ca8f0a2d4e","sort":4,"code":"D","content":"怀孕满4个月流产的，享受48天产假"}],"keywords":"null"}],"code":"SUCCESS"}

json_0627_test4 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"8a20f8727a824f44bae7f9cdc79e8294","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599860,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f1a18478c3554009833aa2d6993ded3a","sort":1,"code":"A","content":"不属于本仲裁委员会管辖"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":2,"code":"B","content":"超出规定的仲裁审查申请期间的"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":3,"code":"C","content":"不属于本仲裁委员会管辖"},{"id":"adfa6de440ea42a588db9548679b987a","sort":4,"code":"D","content":"不属于仲裁委员会受理争议范围"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d393b9f42b594346bacf7e7db5375709","sort":1,"code":"A","content":"2020"},{"id":"8ada3e4200ed486aa248102ccddecad0","sort":2,"code":"B","content":"2022"},{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":3,"code":"C","content":"2021"},{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":4,"code":"D","content":"2023"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":1,"code":"A","content":"50"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":2,"code":"B","content":"40"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":3,"code":"C","content":"5"},{"id":"03b1512043044934a2d266cff87749f7","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68596","type":"001007","level":"003001","content":"对公益性岗位安置就业困难人员给予（    ）补贴，补贴标准参照当地最低工资标准执行。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fffaae54e22b4080a0cdd4b54084847f","sort":1,"code":"A","content":"交通"},{"id":"24867d24ce5a467e9d86aa5e02d16624","sort":2,"code":"B","content":"救济"},{"id":"75cff79c4fa4442984d5b9b8cd41f29c","sort":3,"code":"C","content":"生活"},{"id":"fd638b2f28974d8bb2e636ba9c6cabff","sort":4,"code":"D","content":"岗位"}],"keywords":"null"},{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":1,"code":"A","content":"一次性工亡补助金"},{"id":"5041b2322d4e46ecb88c5ee258187797","sort":2,"code":"B","content":"伤残津贴"},{"id":"1161f371d32547158ebc4d0779992cde","sort":3,"code":"C","content":"6个月本人工资的丧葬补助金"},{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":4,"code":"D","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":1,"code":"A","content":"高寒、高海拔安置区"},{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":2,"code":"B","content":"“三区三州”等深度贫困地区安置区"},{"id":"846e95aa078f4798b9f2adda36932a45","sort":3,"code":"C","content":"人口规模1000人以上大型安置区"},{"id":"973b9a79351146a4acac647acc0331ff","sort":4,"code":"D","content":"地市级城市安置区"}],"keywords":"null"},{"id":"68566","type":"001007","level":"003001","content":"在我国就业的外国人领取养老保险待遇的年龄，原则上执行(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a59921796e884cf9a15f6a87c6beb649","sort":1,"code":"A","content":"我国退休年龄政策，如果属于与我国签订社会保险缴费双边或多边协议的国家，则执行该国退休年龄政策"},{"id":"06e499fbbc6c467d85fcd66f8ec81222","sort":2,"code":"B","content":"我国退休年龄政策"},{"id":"c201c3f515044f70abba35079d08948a","sort":3,"code":"C","content":"外国人国籍国退休年龄政策"},{"id":"660287329b444b84b0c26d2dc1fd909e","sort":4,"code":"D","content":"我国退休年龄政策，如果外国人国籍国退休年龄晚于我国退休年龄，则执行外国人国籍国退休年龄政策"}],"keywords":"null"},{"id":"68579","type":"001007","level":"003001","content":"某企业职工因工死亡，其生前本人月工资8000元，所在统筹地区上年度职工月平均工资为6000元，其配偶应从工伤保险基金领取丧葬补助金和供养亲属抚恤金分别是多少？","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"80a5607757e44876831d096ec23aba1c","sort":1,"code":"A","content":"36000元，每月3200元"},{"id":"666213be31564dfa99c40513598556d9","sort":2,"code":"B","content":"72000元，每月3200元"},{"id":"e185334e3b1d47c98455a6aeb54404f2","sort":3,"code":"C","content":"72000元，每月4000元"},{"id":"89329886b18d48d0944f15c8b0888539","sort":4,"code":"D","content":"36000元，每月4000元"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a6937611ca064abfb27cba90c8064169","sort":1,"code":"A","content":"入境权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":2,"code":"B","content":"民事权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":3,"code":"C","content":"定居权"},{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":4,"code":"D","content":"工作权"}],"keywords":"null"},{"id":"68568","type":"001007","level":"003001","content":"企业年金基金实行(    )，为每个参加企业年金的职工建立(    )账户，按照国家有关规定投资运营","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d0a70c4107fc4b84833e6d569b1cfb55","sort":1,"code":"A","content":"完全积累；统筹"},{"id":"9afce32f3f77465d9609afe5a1753be1","sort":2,"code":"B","content":"部分积累；个人"},{"id":"2b00cc5fbeab473f81afdef2be929b0b","sort":3,"code":"C","content":"完全积累；个人"},{"id":"470088804e84487cacee7b3dba040eff","sort":4,"code":"D","content":"部分积累；统筹"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":1,"code":"A","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":2,"code":"B","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":3,"code":"C","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":4,"code":"D","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d4c856b634ba4590b329500c0fd45234","sort":1,"code":"A","content":"罚款金额最高不得超过5万元"},{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":2,"code":"B","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"},{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":3,"code":"C","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"},{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":4,"code":"D","content":"罚款金额为违法所得的50%至200%"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"84f5476d5068448f8d760b6187a1bb35","sort":1,"code":"A","content":"5"},{"id":"6a937d1dcae9447cac94ce236451b132","sort":2,"code":"B","content":"4"},{"id":"40e7e2db81604a22aa8cab33cc970533","sort":3,"code":"C","content":"3"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":4,"code":"D","content":"6"}],"keywords":"null"},{"id":"68571","type":"001007","level":"003001","content":"出现下列情形(    )，企业年金方案应当终止。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ed43688093e94ded8d612a41db90cc01","sort":1,"code":"A","content":"某企业依法宣告破产，企业年金方案已无法履行"},{"id":"038bd80e1eb2484cba5f2c5c60af07ea","sort":2,"code":"B","content":"因不可抗力等原因导致企业年金方案无法履行的"},{"id":"ac4b6712dda9473f9b10431ef8d6c79b","sort":3,"code":"C","content":"某企业年金集合计划基金财产连续2个月低于500万人民币"},{"id":"526cca00c93346df844b9b82bcb021c0","sort":4,"code":"D","content":"某企业建立企业年金后，因自身短期内经营不善，当前不能继续缴费"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":1,"code":"A","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":2,"code":"B","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":3,"code":"C","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":4,"code":"D","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"}],"keywords":"null"},{"id":"68577","type":"001007","level":"003001","content":"社会保险行政部门应当自工伤认定决定作出之日起(    )日内，将《认定工伤决定书》或者《不予认定工伤决定书》送达受伤害职工（或者其近亲属）和用人单位。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8d58775a231d418183c6215ee073f126","sort":1,"code":"A","content":"10"},{"id":"f4022fc1650c4d3097978fa1790d1b67","sort":2,"code":"B","content":"20"},{"id":"b98281b1df4c496a8e51e77baad9b1ba","sort":3,"code":"C","content":"30"},{"id":"6a08fed453aa4474ac518f54fa380e30","sort":4,"code":"D","content":"60"}],"keywords":"null"},{"id":"68618","type":"001007","level":"003001","content":"甲公司介绍三名13周岁未成年人到乙公司工作。甲公司应被罚款(    )元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f8fee2535baa4419bb4bf460573f232a","sort":1,"code":"A","content":"8000"},{"id":"fc2a44ec470d4c389cd50befa6053a2a","sort":2,"code":"B","content":"10000"},{"id":"d40b2572feab4410b822d497ee817674","sort":3,"code":"C","content":"15000"},{"id":"91dd009201e2490a924cab882346306d","sort":4,"code":"D","content":"4000"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":1,"code":"A","content":"按照小李的要求为其办理转正定级手续"},{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":2,"code":"B","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":3,"code":"C","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":4,"code":"D","content":"与档案接收机构协商，想办法为小李办理。"}],"keywords":"null"},{"id":"68723","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对于消杀防疫、保洁环卫等临时性公益岗位，根据工作任务和工作时间，给予一定的岗位补贴和社会保险补贴，补贴期限最长不超过（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）个月。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0c0e8fb4121b4399832df59d6534cb05","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"},{"id":"838276c3b20e40b592f138faded1ffab","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;7&amp;2526lt;/p&amp;2526gt;"},{"id":"72cd2c8aac9e49fa94bc5fc4f351682f","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"},{"id":"9f9527074b2f45a68a54fecfb938b402","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":1,"code":"A","content":"按照本人工资的60%支付伤残津贴"},{"id":"2c3304f118214840a8944ef614188916","sort":2,"code":"B","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"},{"id":"4f9b228b803e481b9aed1047772b5845","sort":3,"code":"C","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":4,"code":"D","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"01107e15e02e4d2f96538f9313d5170f","sort":1,"code":"A","content":"重点情况说明"},{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":2,"code":"B","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":3,"code":"C","content":"备案函"},{"id":"97366b5104d6412895f3f301041881f1","sort":4,"code":"D","content":"职工（代表）大会决议"}],"keywords":"null"},{"id":"68586","type":"001007","level":"003001","content":"《职业年金基金管理暂行办法》规定，(    )是指接受受托人委托投资管理职业年金基金财产的专业机构。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b14de9c6fd2d4d4287d3ecfb43a24b0f","sort":1,"code":"A","content":"受托人"},{"id":"ba109ee6879246269a64d7ec24a58c46","sort":2,"code":"B","content":"托管人"},{"id":"fcb82e17cf9d4a1ca637084fdf3224ce","sort":3,"code":"C","content":"代理人"},{"id":"f91cd557c0454e90807926a4ac38a909","sort":4,"code":"D","content":"投资管理人"}],"keywords":"null"},{"id":"68565","type":"001007","level":"003001","content":"企业职工基本养老保险中央调剂基金由各省份养老保险基金上解的资金构成。按照各省份职工平均工资的(    )和在职应参保人数作为计算上解额的基数，上解比例从(    )起步，逐步提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6cce8cd0ef46464fac76fea4b3041cff","sort":1,"code":"A","content":"90%；3.5%"},{"id":"43ddec4cd71e4923a09e3b8898825e74","sort":2,"code":"B","content":"80%；3.5%"},{"id":"eda8f0ab8ad4412db86793bebc83f28d","sort":3,"code":"C","content":"80%；3%"},{"id":"79e7d517e5c14955af8ca6803e8d180a","sort":4,"code":"D","content":"90%；3%"}],"keywords":"null"},{"id":"68589","type":"001007","level":"003001","content":"参加职工基本养老保险的个人达到法定退休年龄时，累计缴费年限不足15年的，其养老待遇可以（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"28c4610eff3742c58279b142d12d75d0","sort":1,"code":"A","content":"个人可以书面申请终止职工基本养老保险关系。社保机构按照程序，经本人书面确认后，终止其职工养老保险关系，并将个人账户储存额一次性支付给本人"},{"id":"0930b9bb44fe49869d2d4e15045f9652","sort":2,"code":"B","content":"一次性趸缴至15年"},{"id":"2dd32079db4a4387ba3623c41bbce584","sort":3,"code":"C","content":"可以申请转入户籍所在地城乡居民社会养老保险，享受相应的养老保险待遇"},{"id":"8dfbb022285d4dcf943839c49fe9c1a1","sort":4,"code":"D","content":"延长缴费至满15年，然后按月领取基本养老金（其中社会保险法实施前参保，延长缴费5年后仍不足15年的，延长缴费至满15年）"}],"keywords":"null"},{"id":"68608","type":"001007","level":"003001","content":"博士后设站单位可以将在站博士后予以退站的情形包括（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b6a870373e994075884b5516965e7050","sort":1,"code":"A","content":"出国逾期不归超过15日的"},{"id":"cf8aa510cd684d9a932ef0d10284a4a9","sort":2,"code":"B","content":"因患病等原因难以完成工作的"},{"id":"fe600c99ad2f409396e87e26c02b01e0","sort":3,"code":"C","content":"提供虚假材料获得进站资格的"},{"id":"0bc09acfdb2742a1952906a39c23afd7","sort":4,"code":"D","content":"进站一年仍未取得国家承认的博士学位证书的"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5bf34b901e04adeb4129feb04f01116","sort":1,"code":"A","content":"195"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":3,"code":"C","content":"145"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":4,"code":"D","content":"139"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"438022975c334265a21c2fffb7f465de","sort":1,"code":"A","content":"4"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":2,"code":"B","content":"6"},{"id":"a082cb3fdd534991930f4cb8693b9894","sort":3,"code":"C","content":"5"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":4,"code":"D","content":"7"}],"keywords":"null"},{"id":"68593","type":"001007","level":"003001","content":"无法进行失业登记的人员包括(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"097dc10304544df2ac34a71a406871e5","sort":1,"code":"A","content":"刑满释放人员"},{"id":"d3f9679e86b348109957df6809b90dd5","sort":2,"code":"B","content":"个体工商户业主或私营企业业主停业、破产停止经营的"},{"id":"abc9ac31fc81493a87535e02f62700c2","sort":3,"code":"C","content":"退出现役军人"},{"id":"709fbe517f27498a837fd51f6e23730f","sort":4,"code":"D","content":"年满16周岁，从各类学校毕业、肄业的"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"377c82a0fae341139629ddee8f6a400e","sort":1,"code":"A","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":2,"code":"B","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":3,"code":"C","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":4,"code":"D","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":1,"code":"A","content":"四至六"},{"id":"e39693a21869498da8aa63f62ffaaa91","sort":2,"code":"B","content":"三至五"},{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":3,"code":"C","content":"五至七"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":4,"code":"D","content":"六至八"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f507bc94dcde431cb1b0717eef448115","sort":1,"code":"A","content":"40000元"},{"id":"16f20c281c794a91a6c95a3b39906a17","sort":2,"code":"B","content":"30000元"},{"id":"25f07a9858854902a7f5513177500991","sort":3,"code":"C","content":"60000元"},{"id":"f741138316654c55b9c78bf21488a952","sort":4,"code":"D","content":"10000元"}],"keywords":"null"},{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":1,"code":"A","content":"政府依法认定"},{"id":"f021e857a2dc490caeb862efdbe11e28","sort":2,"code":"B","content":"单位择优使用"},{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":3,"code":"C","content":"业内公正评价"},{"id":"37617262af704c8a9268a3f473b5ba53","sort":4,"code":"D","content":"个人自主申报"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":1,"code":"A","content":"96000元"},{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":2,"code":"B","content":"60000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":3,"code":"C","content":"84000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":4,"code":"D","content":"108000元"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0a552d4343a044648aa59cb70df04f39","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":1,"code":"A","content":"应当为安置人员购买意外伤害商业保险"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":2,"code":"B","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":3,"code":"C","content":"补贴标准根据乡村生活费用确定"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":4,"code":"D","content":"可以签订劳动合同也可以签订劳务协议"}],"keywords":"null"},{"id":"68616","type":"001007","level":"003001","content":"关于非全日制用工的描述，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cedd50b25f9f4bfebf14a08411411a8a","sort":1,"code":"A","content":"不得约定试用期"},{"id":"4403042a372a4012a06c24f2c30d0f91","sort":2,"code":"B","content":"劳动者可与一个或一个以上用人单位订立劳动合同"},{"id":"95cc3dcbef024d729a17d23ac8c371ab","sort":3,"code":"C","content":"劳动者在同一用人单位每周工作时间累计不超过20小时"},{"id":"3f32cdc64b2845f8af57d9884e182b23","sort":4,"code":"D","content":"劳动者在同一用人单位一般平均每天工作不超过4小时"}],"keywords":"null"},{"id":"68726","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年政府工作报告指出，今年有关目标为：城镇新增就业（&nbsp;&nbsp;&nbsp; ）人以上，城镇调查失业率（&nbsp;&nbsp;&nbsp; ）左右，城镇登记失业率（&nbsp;&nbsp;&nbsp; ）左右。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9c5807f503084d8daaec7e16c3fc6772","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6.5%；5.5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"106ca254439f4238a1a51f9b28628025","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6.5%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fd0cd6f2d8714db2a00254d9bfb292a5","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6%；5.5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"a25ef3d52bf14b9eb77f995697c9c17c","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68585","type":"001007","level":"003001","content":"企业年金养老金产品投资管理人应当接受份额持有人和(    )的监督。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"31ce5c02f25c48a282d1bd33c108d29f","sort":1,"code":"A","content":"账管人"},{"id":"e734ff275d68469ebc3463c80771c3a8","sort":2,"code":"B","content":"代理人"},{"id":"0ba7f9932f4d49dbbc769575c5a16bf8","sort":3,"code":"C","content":"托管人"},{"id":"6ba5033a73fb44bf85c943bf3d2f3520","sort":4,"code":"D","content":"受托人"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bcbfd8add87943f0ace414c4194d3546","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e3125d07cd0446a89213ec98e18812ab","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5d3526a8261343468d01869caa805ef4","sort":1,"code":"A","content":"毕业年度高校毕业生"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":2,"code":"B","content":"农村转移就业劳动者"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":3,"code":"C","content":"城镇登记失业人员"},{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":4,"code":"D","content":"贫困家庭子女"}],"keywords":"null"},{"id":"68576","type":"001007","level":"003001","content":"以建设项目为单位参保的建筑企业，可以按照(    )的一定比例计算缴纳工伤保险费。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bbe9b096e1b54c6a92643641bca1f5f6","sort":1,"code":"A","content":"项目工程总造价"},{"id":"1517719a0cda40b0ab282c74e67368d8","sort":2,"code":"B","content":"工资总额"},{"id":"e9aadb1f63024e34a14885585a223fa9","sort":3,"code":"C","content":"当地平均工资"},{"id":"af3b6737393c465599080524c7cce70d","sort":4,"code":"D","content":"以上皆可"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":1,"code":"A","content":"9；2；3"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":2,"code":"B","content":"10；5；6"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":3,"code":"C","content":"10；4；5"},{"id":"b34b2d30e563409e9615ece5765d7739","sort":4,"code":"D","content":"9；3；4"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c344b8652c604917b8df2f26adf68344","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":1,"code":"A","content":"在注册地参加社会保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":2,"code":"B","content":"可以参加职工基本医疗保险"},{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":3,"code":"C","content":"在居住地参加社会保险"},{"id":"a1b641859d98482e920a476122b69775","sort":4,"code":"D","content":"可以参加职工基本养老保险"}],"keywords":"null"},{"id":"68614","type":"001007","level":"003001","content":"企业裁减人员时，依法应当优先留用（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8742eccd8e41413688b3941288fc3c41","sort":1,"code":"A","content":"与本单位订立无固定期限劳动合同的人员"},{"id":"1fd8155b7ba64462ab9c9bd68a31a9ab","sort":2,"code":"B","content":"家庭有需要扶养的老人"},{"id":"23b4206865ef40298f20596679a00de0","sort":3,"code":"C","content":"掌握企业核心技术、对企业发展至关重要的人员"},{"id":"77f2089cced8489a8c83c2ef45b7d43c","sort":4,"code":"D","content":"与本单位订立8年期限劳动合同的人员"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f1fb45ece27943f1b08b0390638b8438","sort":1,"code":"A","content":"城乡劳动力"},{"id":"20775075cd5b451b827342aa85304fc7","sort":2,"code":"B","content":"城镇劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":3,"code":"C","content":"高校劳动力"},{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":4,"code":"D","content":"农村劳动力"}],"keywords":"null"},{"id":"68574","type":"001007","level":"003001","content":"老王在领取失业保险金期间因达到退休年龄办理了退休手续，并开始领取养老金。那么(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"51829768776847d1995a7bf0331eedc6","sort":1,"code":"A","content":"他可以继续领取剩余的失业保险金"},{"id":"73f7985a40e6455786c037381bf05164","sort":2,"code":"B","content":"他不可以继续领失业保险金"},{"id":"5c9fb3c9a8704de88fd7be3be4cab922","sort":3,"code":"C","content":"他可以再领取一个月的失业保险金"},{"id":"0dc709dd74274fedbb89a08feb023003","sort":4,"code":"D","content":"他不可以继续领失业保险金，但可以享受其他失业保险待遇"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68625","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;按照人社部财政部文件规定，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;政府投资开发的公益性岗位，只限安排符合岗位要求的就业困难人员。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5e4791de7b8f4db8bb06008e5013ece6","sort":1,"code":"A","content":"错误"},{"id":"465813873edf45c891af7acde9fd4be3","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68629","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位的隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bc4688d2e71b4c7cb641d78bd9022cbb","sort":1,"code":"A","content":"错误"},{"id":"3f3bb9efec414414930731eea2e812a1","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68627","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce4efa5b214748c78c355df38da717a2","sort":1,"code":"A","content":"错误"},{"id":"1be729e13a1945bab354d0faf4c3492c","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]}]},"code":"SUCCESS"}
json_0627_answer4 = {"httpStatus":"OK","status":0,"message":"成功","data":[{"id":"68579","type":"001007","level":"003001","content":"某企业职工因工死亡，其生前本人月工资8000元，所在统筹地区上年度职工月平均工资为6000元，其配偶应从工伤保险基金领取丧葬补助金和供养亲属抚恤金分别是多少？","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"666213be31564dfa99c40513598556d9","sort":1,"code":"A","content":"72000元，每月3200元"},{"id":"e185334e3b1d47c98455a6aeb54404f2","sort":2,"code":"B","content":"72000元，每月4000元"},{"id":"80a5607757e44876831d096ec23aba1c","sort":3,"code":"C","content":"36000元，每月3200元"},{"id":"89329886b18d48d0944f15c8b0888539","sort":4,"code":"D","content":"36000元，每月4000元"}],"keywords":"null"},{"id":"68571","type":"001007","level":"003001","content":"出现下列情形(    )，企业年金方案应当终止。","answer":"B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ac4b6712dda9473f9b10431ef8d6c79b","sort":1,"code":"A","content":"某企业年金集合计划基金财产连续2个月低于500万人民币"},{"id":"ed43688093e94ded8d612a41db90cc01","sort":2,"code":"B","content":"某企业依法宣告破产，企业年金方案已无法履行"},{"id":"038bd80e1eb2484cba5f2c5c60af07ea","sort":3,"code":"C","content":"因不可抗力等原因导致企业年金方案无法履行的"},{"id":"526cca00c93346df844b9b82bcb021c0","sort":4,"code":"D","content":"某企业建立企业年金后，因自身短期内经营不善，当前不能继续缴费"}],"keywords":"null"},{"id":"68616","type":"001007","level":"003001","content":"关于非全日制用工的描述，错误的是(    )","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3f32cdc64b2845f8af57d9884e182b23","sort":1,"code":"A","content":"劳动者在同一用人单位一般平均每天工作不超过4小时"},{"id":"95cc3dcbef024d729a17d23ac8c371ab","sort":2,"code":"B","content":"劳动者在同一用人单位每周工作时间累计不超过20小时"},{"id":"cedd50b25f9f4bfebf14a08411411a8a","sort":3,"code":"C","content":"不得约定试用期"},{"id":"4403042a372a4012a06c24f2c30d0f91","sort":4,"code":"D","content":"劳动者可与一个或一个以上用人单位订立劳动合同"}],"keywords":"null"}],"code":"SUCCESS"}

json_0627_test5 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"05b610b384524992913888161f8762d0","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599325,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cd44e594750548e8a9b814d8744f4121","sort":1,"code":"A","content":"需要经常出差，男士优先"},{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":2,"code":"B","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"},{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":3,"code":"C","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"},{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":4,"code":"D","content":"具有互联网工作经验优先"}],"keywords":"null"},{"id":"68566","type":"001007","level":"003001","content":"在我国就业的外国人领取养老保险待遇的年龄，原则上执行(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"660287329b444b84b0c26d2dc1fd909e","sort":1,"code":"A","content":"我国退休年龄政策，如果外国人国籍国退休年龄晚于我国退休年龄，则执行外国人国籍国退休年龄政策"},{"id":"06e499fbbc6c467d85fcd66f8ec81222","sort":2,"code":"B","content":"我国退休年龄政策"},{"id":"c201c3f515044f70abba35079d08948a","sort":3,"code":"C","content":"外国人国籍国退休年龄政策"},{"id":"a59921796e884cf9a15f6a87c6beb649","sort":4,"code":"D","content":"我国退休年龄政策，如果属于与我国签订社会保险缴费双边或多边协议的国家，则执行该国退休年龄政策"}],"keywords":"null"},{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5041b2322d4e46ecb88c5ee258187797","sort":1,"code":"A","content":"伤残津贴"},{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":2,"code":"B","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"},{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":3,"code":"C","content":"一次性工亡补助金"},{"id":"1161f371d32547158ebc4d0779992cde","sort":4,"code":"D","content":"6个月本人工资的丧葬补助金"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":1,"code":"A","content":"职工一方协商代表资格是否符合国家有关规定"},{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":2,"code":"B","content":"集体合同约定的工资增幅是否合理"},{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":3,"code":"C","content":"补充保险和福利约定是否符合国家有关规"},{"id":"d76d9d824b1348c190e381f06a178776","sort":4,"code":"D","content":"协商程序是否履行《集体合同规定》所规定的具体程序"}],"keywords":"null"},{"id":"68585","type":"001007","level":"003001","content":"企业年金养老金产品投资管理人应当接受份额持有人和(    )的监督。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6ba5033a73fb44bf85c943bf3d2f3520","sort":1,"code":"A","content":"受托人"},{"id":"e734ff275d68469ebc3463c80771c3a8","sort":2,"code":"B","content":"代理人"},{"id":"0ba7f9932f4d49dbbc769575c5a16bf8","sort":3,"code":"C","content":"托管人"},{"id":"31ce5c02f25c48a282d1bd33c108d29f","sort":4,"code":"D","content":"账管人"}],"keywords":"null"},{"id":"68577","type":"001007","level":"003001","content":"社会保险行政部门应当自工伤认定决定作出之日起(    )日内，将《认定工伤决定书》或者《不予认定工伤决定书》送达受伤害职工（或者其近亲属）和用人单位。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8d58775a231d418183c6215ee073f126","sort":1,"code":"A","content":"10"},{"id":"b98281b1df4c496a8e51e77baad9b1ba","sort":2,"code":"B","content":"30"},{"id":"6a08fed453aa4474ac518f54fa380e30","sort":3,"code":"C","content":"60"},{"id":"f4022fc1650c4d3097978fa1790d1b67","sort":4,"code":"D","content":"20"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":1,"code":"A","content":"累计参保缴费满三年"},{"id":"df3ec29881de4e89a74191f1b922cccb","sort":2,"code":"B","content":"累计参保缴费满一年"},{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":3,"code":"C","content":"不设参保年限"},{"id":"84fdcd3629f2496597b7906039f6acaf","sort":4,"code":"D","content":"累计参保缴费满二年"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"57d05cea438c42ceabf4ec28047254c3","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"38ac1534bac04628b824eee9c740e6ed","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"defeb3d10031449d86eaf10f6271a331","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":1,"code":"A","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":2,"code":"B","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":3,"code":"C","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":4,"code":"D","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0a552d4343a044648aa59cb70df04f39","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"97366b5104d6412895f3f301041881f1","sort":1,"code":"A","content":"职工（代表）大会决议"},{"id":"01107e15e02e4d2f96538f9313d5170f","sort":2,"code":"B","content":"重点情况说明"},{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":3,"code":"C","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":4,"code":"D","content":"备案函"}],"keywords":"null"},{"id":"68576","type":"001007","level":"003001","content":"以建设项目为单位参保的建筑企业，可以按照(    )的一定比例计算缴纳工伤保险费。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1517719a0cda40b0ab282c74e67368d8","sort":1,"code":"A","content":"工资总额"},{"id":"af3b6737393c465599080524c7cce70d","sort":2,"code":"B","content":"以上皆可"},{"id":"e9aadb1f63024e34a14885585a223fa9","sort":3,"code":"C","content":"当地平均工资"},{"id":"bbe9b096e1b54c6a92643641bca1f5f6","sort":4,"code":"D","content":"项目工程总造价"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"faed1327f3e646e5be24adc94103c3d7","sort":1,"code":"A","content":"正常运营5个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":2,"code":"B","content":"正常运营7个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":3,"code":"C","content":"正常运营1个月"},{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":4,"code":"D","content":"正常运营3个月"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":1,"code":"A","content":"108000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":2,"code":"B","content":"96000元"},{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":3,"code":"C","content":"60000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":4,"code":"D","content":"84000元"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":1,"code":"A","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":2,"code":"B","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":3,"code":"C","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":4,"code":"D","content":"王某与公司续订为期3年的劳动合同，未约定试用期"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"659b0e46772647ffb997df394f735d00","sort":1,"code":"A","content":"上一年度全国城镇居民人均可支配收入"},{"id":"a7ae703580c542398303612d32f10288","sort":2,"code":"B","content":"上一年度全省城镇居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":3,"code":"C","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"},{"id":"da0164df20a6444ea9c06df863038525","sort":4,"code":"D","content":"上一年度全国居民人均可支配收入"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"55180558f6bc48c5bebed340833a779f","sort":1,"code":"A","content":"天津"},{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":2,"code":"B","content":"山东"},{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":3,"code":"C","content":"职工户籍所在地"},{"id":"b2b033f986284933a47b14d742bfa453","sort":4,"code":"D","content":"北京"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68722","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对&amp;2526lt;/span&amp;2526gt;2020年3月至12月，领取失业保险金期满仍未就业的失业人员、不符合领取失业保险金条件的参保失业人员，发放（ &nbsp;&nbsp;）个月的失业补助金，标准不高于当地失业保险金的（ &nbsp;&nbsp;&nbsp;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b49f0e5f79a8463cbb91d053a19a69cc","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"7383c2af02604820b6882b632b404923","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"d8243054793d442c9577daac5446188a","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c2c76fcab56746099f6e0020afb20110","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5f415af62962421ebe130734f5103ae3","sort":1,"code":"A","content":"安全保管企业年金基金财产"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":2,"code":"B","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":3,"code":"C","content":"及时办理清算、交割事宜"},{"id":"3413d86553634b5c958740b3ec761da0","sort":4,"code":"D","content":"制定企业年金基金战略资产配置策略"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":1,"code":"A","content":"常住地；常住地"},{"id":"5a22297e9c5e42588338374f2db13853","sort":2,"code":"B","content":"出生地；户籍地"},{"id":"583b9bc056c641ffa095ef97015a8380","sort":3,"code":"C","content":"常住地；出生地"},{"id":"c663276dfd0b4d2c93e4177521a14071","sort":4,"code":"D","content":"原单位注册地；常住地"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b34b2d30e563409e9615ece5765d7739","sort":1,"code":"A","content":"9；3；4"},{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":2,"code":"B","content":"9；2；3"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":3,"code":"C","content":"10；4；5"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":4,"code":"D","content":"10；5；6"}],"keywords":"null"},{"id":"68597","type":"001007","level":"003001","content":"属于高校毕业生基层服务项目的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1c1f46c89b06468eb1497d0825bd0658","sort":1,"code":"A","content":"志愿服务西部计划"},{"id":"a9983ec2a62b48e9915eb0112bc48a3c","sort":2,"code":"B","content":"公益就业行动计划"},{"id":"b8f6e68bbba84a7ba269bfaefaefe9c3","sort":3,"code":"C","content":"“凤凰飞翔”计划"},{"id":"a3d35ea01e424f67ac8b84525f318ca7","sort":4,"code":"D","content":"“三支一扶”计划"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":1,"code":"A","content":"50"},{"id":"03b1512043044934a2d266cff87749f7","sort":2,"code":"B","content":"4"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":3,"code":"C","content":"5"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":4,"code":"D","content":"40"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":1,"code":"A","content":"罚款金额为违法所得的50%至200%"},{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":2,"code":"B","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"},{"id":"d4c856b634ba4590b329500c0fd45234","sort":3,"code":"C","content":"罚款金额最高不得超过5万元"},{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":4,"code":"D","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":1,"code":"A","content":"省级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":2,"code":"B","content":"流动人员本人"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":3,"code":"C","content":"县级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":4,"code":"D","content":"经人力资源社会保障部门授权的单位"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a1b641859d98482e920a476122b69775","sort":1,"code":"A","content":"可以参加职工基本养老保险"},{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":2,"code":"B","content":"在注册地参加社会保险"},{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":3,"code":"C","content":"在居住地参加社会保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":4,"code":"D","content":"可以参加职工基本医疗保险"}],"keywords":"null"},{"id":"68568","type":"001007","level":"003001","content":"企业年金基金实行(    )，为每个参加企业年金的职工建立(    )账户，按照国家有关规定投资运营","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d0a70c4107fc4b84833e6d569b1cfb55","sort":1,"code":"A","content":"完全积累；统筹"},{"id":"470088804e84487cacee7b3dba040eff","sort":2,"code":"B","content":"部分积累；统筹"},{"id":"2b00cc5fbeab473f81afdef2be929b0b","sort":3,"code":"C","content":"完全积累；个人"},{"id":"9afce32f3f77465d9609afe5a1753be1","sort":4,"code":"D","content":"部分积累；个人"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":1,"code":"A","content":"2023"},{"id":"8ada3e4200ed486aa248102ccddecad0","sort":2,"code":"B","content":"2022"},{"id":"d393b9f42b594346bacf7e7db5375709","sort":3,"code":"C","content":"2020"},{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":4,"code":"D","content":"2021"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"88f1f34a065f44dea656d7797a9edc11","sort":1,"code":"A","content":"5个"},{"id":"713eaa07fb8042eea09409619ff0f619","sort":2,"code":"B","content":"8个"},{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":3,"code":"C","content":"7个"},{"id":"8df6381555cb4de9883763e7239ed809","sort":4,"code":"D","content":"6个"}],"keywords":"null"},{"id":"68620","type":"001007","level":"003001","content":"在办理机关事业单位职业年金转移接续时，无需转移的基金项目包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f7c56f8bb62f4a2eae54ee2e7da8edff","sort":1,"code":"A","content":"补记的职业年金"},{"id":"cc0fe7a8998f46a4b1392c42b28a687a","sort":2,"code":"B","content":"缴费形成的职业年金"},{"id":"83c5e0f5fd124299b2aadccc4da44c6e","sort":3,"code":"C","content":"原转入的企业年金"},{"id":"4038e407cd32415e941dc64bc86f7969","sort":4,"code":"D","content":"个人缴费本息"}],"keywords":"null"},{"id":"68624","type":"001007","level":"003001","content":"根据《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》，严重失信、失范行为包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c937f322d72945d6be8d65d0d3edc7e4","sort":1,"code":"A","content":"应缴纳社会保险费却拒不缴纳的"},{"id":"42e37dfb02bf4ffcb42f2a8c48234005","sort":2,"code":"B","content":"非法获取社保个人权益数据的"},{"id":"14af74be5a8c4080ae67f4d0a37e7dc0","sort":3,"code":"C","content":"隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的"},{"id":"b4b68d4fccf44ed484f8a7922ea94cd5","sort":4,"code":"D","content":"社保服务机构违反服务协议的"}],"keywords":"null"},{"id":"68592","type":"001007","level":"003001","content":"属于行政审批项目的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"94a8395b864240348475edc5c522c30e","sort":1,"code":"A","content":"标准工时制度"},{"id":"64660271849e44af98a09ce7791f55dc","sort":2,"code":"B","content":"劳务派遣经营"},{"id":"a51751a0bd244b29b28eedbe23089ba7","sort":3,"code":"C","content":"民办职业培训机构变更审批"},{"id":"6d0991298d834283ace6da359767410e","sort":4,"code":"D","content":"职业技能考核鉴定机构设立审批"}],"keywords":"null"},{"id":"68600","type":"001007","level":"003001","content":"按照现行规定，面向个人发放的创业担保贷款期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"414a064395064954a551f10efd6a73d9","sort":1,"code":"A","content":"3"},{"id":"d7d57727a08f4884950a0f667f43caf4","sort":2,"code":"B","content":"4"},{"id":"cfb5ba55490b49fd91dd7d7e0a82de7d","sort":3,"code":"C","content":"1"},{"id":"24092da8dfdf4c9e910f8421d51e885c","sort":4,"code":"D","content":"2"}],"keywords":"null"},{"id":"68614","type":"001007","level":"003001","content":"企业裁减人员时，依法应当优先留用（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"23b4206865ef40298f20596679a00de0","sort":1,"code":"A","content":"掌握企业核心技术、对企业发展至关重要的人员"},{"id":"1fd8155b7ba64462ab9c9bd68a31a9ab","sort":2,"code":"B","content":"家庭有需要扶养的老人"},{"id":"77f2089cced8489a8c83c2ef45b7d43c","sort":3,"code":"C","content":"与本单位订立8年期限劳动合同的人员"},{"id":"8742eccd8e41413688b3941288fc3c41","sort":4,"code":"D","content":"与本单位订立无固定期限劳动合同的人员"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f741138316654c55b9c78bf21488a952","sort":1,"code":"A","content":"10000元"},{"id":"16f20c281c794a91a6c95a3b39906a17","sort":2,"code":"B","content":"30000元"},{"id":"25f07a9858854902a7f5513177500991","sort":3,"code":"C","content":"60000元"},{"id":"f507bc94dcde431cb1b0717eef448115","sort":4,"code":"D","content":"40000元"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":1,"code":"A","content":"139"},{"id":"c5bf34b901e04adeb4129feb04f01116","sort":2,"code":"B","content":"195"},{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":3,"code":"C","content":"145"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":4,"code":"D","content":"170"}],"keywords":"null"},{"id":"68560","type":"001007","level":"003001","content":"（    ）参加劳动预备制培训的，可以享受一定标准的生活费补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c9efc2fba21f4e0d8ab0f96d8fa16667","sort":1,"code":"A","content":"农村学员"},{"id":"0336f625724641558e729178184964c5","sort":2,"code":"B","content":"应届初高中毕业生"},{"id":"6f9319af9c2c4dbbac85f623eb4cd331","sort":3,"code":"C","content":"城市低保家庭学员"},{"id":"2050b405c33d4e62882bb572311fc967","sort":4,"code":"D","content":"困难家庭学员"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8fc87ce4be7544959362d8195ee69b27","sort":1,"code":"A","content":"六至八"},{"id":"e39693a21869498da8aa63f62ffaaa91","sort":2,"code":"B","content":"三至五"},{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":3,"code":"C","content":"五至七"},{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":4,"code":"D","content":"四至六"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":1,"code":"A","content":"应当为安置人员购买意外伤害商业保险"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":2,"code":"B","content":"可以签订劳动合同也可以签订劳务协议"},{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":3,"code":"C","content":"补贴标准根据乡村生活费用确定"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":4,"code":"D","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"20775075cd5b451b827342aa85304fc7","sort":1,"code":"A","content":"城镇劳动力"},{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":2,"code":"B","content":"农村劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":3,"code":"C","content":"高校劳动力"},{"id":"f1fb45ece27943f1b08b0390638b8438","sort":4,"code":"D","content":"城乡劳动力"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f6cf14fd2b249109922524a550c021b","sort":1,"code":"A","content":"个人自带"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":2,"code":"B","content":"可直接从学校转递到企业"},{"id":"3ae4a91f95a049629966229077ae4831","sort":3,"code":"C","content":"可以弃档不管"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":4,"code":"D","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5d3526a8261343468d01869caa805ef4","sort":1,"code":"A","content":"毕业年度高校毕业生"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":2,"code":"B","content":"城镇登记失业人员"},{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":3,"code":"C","content":"贫困家庭子女"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":4,"code":"D","content":"农村转移就业劳动者"}],"keywords":"null"},{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":1,"code":"A","content":"政府依法认定"},{"id":"37617262af704c8a9268a3f473b5ba53","sort":2,"code":"B","content":"个人自主申报"},{"id":"f021e857a2dc490caeb862efdbe11e28","sort":3,"code":"C","content":"单位择优使用"},{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":4,"code":"D","content":"业内公正评价"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"438022975c334265a21c2fffb7f465de","sort":1,"code":"A","content":"4"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":2,"code":"B","content":"6"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":3,"code":"C","content":"7"},{"id":"a082cb3fdd534991930f4cb8693b9894","sort":4,"code":"D","content":"5"}],"keywords":"null"},{"id":"68725","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年5月至12月，对2019年1月1日之后参保不满( &nbsp;&nbsp;)的失业农民工，参照参保地城市低保标准，按月发放不超过( &nbsp;&nbsp;)个月的临时生活补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"97071a22bb11498384baf737fd2d7635","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"c16cbd2548cd4f78b46e6a212158fa32","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9bcba69d0e274fd4ade1bb6e44238fd8","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e6643bbfec93471f888bb4891304f525","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68631","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;中央直属企业实行不定时工作制和综合计算工时工作制等其他工作和休息办法的，需经国务院行业主管部门审核，报国务院劳动行政部门批准。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e678ea16f06c467891a594d7260ec56c","sort":1,"code":"A","content":"错误"},{"id":"d18af3bfb0174ffd80a125be025d97bd","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68630","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对违反劳动保障法律的行为，如发生在&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;3&amp;2526lt;span&amp;2526gt;年内&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，劳动保障行政部门应当依法受理。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"123bdc965cb2468cb26bd23a7d2f42b3","sort":1,"code":"A","content":"错误"},{"id":"2196c3eed8be4a8d84e88434598eb1e5","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68629","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位的隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bc4688d2e71b4c7cb641d78bd9022cbb","sort":1,"code":"A","content":"错误"},{"id":"3f3bb9efec414414930731eea2e812a1","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]}]},"code":"SUCCESS"}
# json_0627_answer5 =

json_0627_test6 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"6218c118841f41b4a0ca662df73a4a59","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599649,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":1,"code":"A","content":"业内公正评价"},{"id":"37617262af704c8a9268a3f473b5ba53","sort":2,"code":"B","content":"个人自主申报"},{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":3,"code":"C","content":"政府依法认定"},{"id":"f021e857a2dc490caeb862efdbe11e28","sort":4,"code":"D","content":"单位择优使用"}],"keywords":"null"},{"id":"68568","type":"001007","level":"003001","content":"企业年金基金实行(    )，为每个参加企业年金的职工建立(    )账户，按照国家有关规定投资运营","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"470088804e84487cacee7b3dba040eff","sort":1,"code":"A","content":"部分积累；统筹"},{"id":"9afce32f3f77465d9609afe5a1753be1","sort":2,"code":"B","content":"部分积累；个人"},{"id":"2b00cc5fbeab473f81afdef2be929b0b","sort":3,"code":"C","content":"完全积累；个人"},{"id":"d0a70c4107fc4b84833e6d569b1cfb55","sort":4,"code":"D","content":"完全积累；统筹"}],"keywords":"null"},{"id":"68556","type":"001007","level":"003001","content":"A省人才中心实行了档案接收告知承诺制，其在接收某企业员工小张的档案时，发现缺少核定小张学历学位的材料。该人才中心正确做法是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cbbf941b0d784fa991ed21d2c952eb10","sort":1,"code":"A","content":"一次性告知所缺材料及其可能造成的影响，经本人作出书面知情说明、承诺补充材料后予以接收"},{"id":"bfd6c9e1fa7e406bb2942347175c6f48","sort":2,"code":"B","content":"一次性告知所缺材料及其可能造成的影响后，采取先存后补方式予以接收"},{"id":"7c3dba49ff6f4b128d475f7192c7fe73","sort":3,"code":"C","content":"与原单位协商退回并补充材料"},{"id":"3927d7aff6fa4c848316890cccf2f613","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":1,"code":"A","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":2,"code":"B","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":3,"code":"C","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":4,"code":"D","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":1,"code":"A","content":"职工户籍所在地"},{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":2,"code":"B","content":"山东"},{"id":"b2b033f986284933a47b14d742bfa453","sort":3,"code":"C","content":"北京"},{"id":"55180558f6bc48c5bebed340833a779f","sort":4,"code":"D","content":"天津"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":1,"code":"A","content":"可以参加职工基本医疗保险"},{"id":"a1b641859d98482e920a476122b69775","sort":2,"code":"B","content":"可以参加职工基本养老保险"},{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":3,"code":"C","content":"在居住地参加社会保险"},{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":4,"code":"D","content":"在注册地参加社会保险"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":1,"code":"A","content":"工作权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":2,"code":"B","content":"定居权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":3,"code":"C","content":"民事权"},{"id":"a6937611ca064abfb27cba90c8064169","sort":4,"code":"D","content":"入境权"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":1,"code":"A","content":"2021"},{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":2,"code":"B","content":"2023"},{"id":"d393b9f42b594346bacf7e7db5375709","sort":3,"code":"C","content":"2020"},{"id":"8ada3e4200ed486aa248102ccddecad0","sort":4,"code":"D","content":"2022"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":1,"code":"A","content":"贫困家庭子女"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":2,"code":"B","content":"城镇登记失业人员"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":3,"code":"C","content":"农村转移就业劳动者"},{"id":"5d3526a8261343468d01869caa805ef4","sort":4,"code":"D","content":"毕业年度高校毕业生"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"defeb3d10031449d86eaf10f6271a331","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":2,"code":"B","content":"2"},{"id":"394106514712430bad66fd4bf853deb1","sort":3,"code":"C","content":"3"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68615","type":"001007","level":"003001","content":"关于女职工生育享受假期，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f49b1e597dfe4db58af159ca8f0a2d4e","sort":1,"code":"A","content":"怀孕满4个月流产的，享受48天产假"},{"id":"b2c58eb097ae4d81819fd9be7a8c39a5","sort":2,"code":"B","content":"女职工生育享受98天产假，其中产前只能休假10天"},{"id":"b05792b7d339491a8ae07be2266e7248","sort":3,"code":"C","content":"难产的，应增加产假15天；生育多胞胎的，每多生育1个婴儿，可增加产假10天"},{"id":"07f14be1e48f4ed6af0ba069010a9a12","sort":4,"code":"D","content":"女职工怀孕未满4个月流产的，享受15天产假"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f6cf14fd2b249109922524a550c021b","sort":1,"code":"A","content":"个人自带"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":2,"code":"B","content":"可直接从学校转递到企业"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":3,"code":"C","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"3ae4a91f95a049629966229077ae4831","sort":4,"code":"D","content":"可以弃档不管"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bcbfd8add87943f0ace414c4194d3546","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e3125d07cd0446a89213ec98e18812ab","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8e5fd62e7b12443db02196646c2f3315","sort":1,"code":"A","content":"5"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":2,"code":"B","content":"12"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":3,"code":"C","content":"8"},{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":4,"code":"D","content":"10"}],"keywords":"null"},{"id":"68596","type":"001007","level":"003001","content":"对公益性岗位安置就业困难人员给予（    ）补贴，补贴标准参照当地最低工资标准执行。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fd638b2f28974d8bb2e636ba9c6cabff","sort":1,"code":"A","content":"岗位"},{"id":"24867d24ce5a467e9d86aa5e02d16624","sort":2,"code":"B","content":"救济"},{"id":"fffaae54e22b4080a0cdd4b54084847f","sort":3,"code":"C","content":"交通"},{"id":"75cff79c4fa4442984d5b9b8cd41f29c","sort":4,"code":"D","content":"生活"}],"keywords":"null"},{"id":"68585","type":"001007","level":"003001","content":"企业年金养老金产品投资管理人应当接受份额持有人和(    )的监督。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0ba7f9932f4d49dbbc769575c5a16bf8","sort":1,"code":"A","content":"托管人"},{"id":"6ba5033a73fb44bf85c943bf3d2f3520","sort":2,"code":"B","content":"受托人"},{"id":"31ce5c02f25c48a282d1bd33c108d29f","sort":3,"code":"C","content":"账管人"},{"id":"e734ff275d68469ebc3463c80771c3a8","sort":4,"code":"D","content":"代理人"}],"keywords":"null"},{"id":"68612","type":"001007","level":"003001","content":"劳动争议仲裁时效中断的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c0aa12a2e1a04eee8762906faa99857d","sort":1,"code":"A","content":"针对用人单位拖欠的工资报酬，张某想了几个月，觉得耗时耗力，最终放弃了"},{"id":"493382fe56de47f3aa0a3f28d36a5556","sort":2,"code":"B","content":"张某向调解组织申请，希望调解组织组织调解用人单位与其个人的劳动纠纷"},{"id":"e07bc7a86d4a4dd194dc7c45a90a3d6b","sort":3,"code":"C","content":"张某主动要求用人单位支付加班工资，用人单位否认拖欠工资报酬"},{"id":"3c73b4e2e0f94b6ca1ded207e503dc61","sort":4,"code":"D","content":"用人单位书面承诺，3个月内向劳动者支付拖欠的劳动报酬"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"35fc4638f35144bc968e525af74b0899","sort":1,"code":"A","content":"正常运营7个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":2,"code":"B","content":"正常运营1个月"},{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":3,"code":"C","content":"正常运营3个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":4,"code":"D","content":"正常运营5个月"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":1,"code":"A","content":"108000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":2,"code":"B","content":"84000元"},{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":3,"code":"C","content":"60000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":4,"code":"D","content":"96000元"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6491ca747d40446b9851d75b5d998c5f","sort":1,"code":"A","content":"10；5；6"},{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":2,"code":"B","content":"9；2；3"},{"id":"b34b2d30e563409e9615ece5765d7739","sort":3,"code":"C","content":"9；3；4"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":4,"code":"D","content":"10；4；5"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":1,"code":"A","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"},{"id":"2c3304f118214840a8944ef614188916","sort":2,"code":"B","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"},{"id":"4f9b228b803e481b9aed1047772b5845","sort":3,"code":"C","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":4,"code":"D","content":"按照本人工资的60%支付伤残津贴"}],"keywords":"null"},{"id":"68723","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对于消杀防疫、保洁环卫等临时性公益岗位，根据工作任务和工作时间，给予一定的岗位补贴和社会保险补贴，补贴期限最长不超过（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）个月。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"838276c3b20e40b592f138faded1ffab","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;7&amp;2526lt;/p&amp;2526gt;"},{"id":"72cd2c8aac9e49fa94bc5fc4f351682f","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;6&amp;2526lt;/p&amp;2526gt;"},{"id":"9f9527074b2f45a68a54fecfb938b402","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;4&amp;2526lt;/p&amp;2526gt;"},{"id":"0c0e8fb4121b4399832df59d6534cb05","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;5&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5a22297e9c5e42588338374f2db13853","sort":1,"code":"A","content":"出生地；户籍地"},{"id":"c663276dfd0b4d2c93e4177521a14071","sort":2,"code":"B","content":"原单位注册地；常住地"},{"id":"583b9bc056c641ffa095ef97015a8380","sort":3,"code":"C","content":"常住地；出生地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":4,"code":"D","content":"常住地；常住地"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":1,"code":"A","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"},{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":2,"code":"B","content":"罚款金额为违法所得的50%至200%"},{"id":"d4c856b634ba4590b329500c0fd45234","sort":3,"code":"C","content":"罚款金额最高不得超过5万元"},{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":4,"code":"D","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"}],"keywords":"null"},{"id":"68624","type":"001007","level":"003001","content":"根据《关于对社会保险领域严重失信企业及其有关人员实施联合惩戒的合作备忘录》，严重失信、失范行为包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b4b68d4fccf44ed484f8a7922ea94cd5","sort":1,"code":"A","content":"社保服务机构违反服务协议的"},{"id":"42e37dfb02bf4ffcb42f2a8c48234005","sort":2,"code":"B","content":"非法获取社保个人权益数据的"},{"id":"14af74be5a8c4080ae67f4d0a37e7dc0","sort":3,"code":"C","content":"隐匿、转移、侵占、挪用社会保险费款、基金或者违规投资运营的"},{"id":"c937f322d72945d6be8d65d0d3edc7e4","sort":4,"code":"D","content":"应缴纳社会保险费却拒不缴纳的"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a7ae703580c542398303612d32f10288","sort":1,"code":"A","content":"上一年度全省城镇居民人均可支配收入"},{"id":"da0164df20a6444ea9c06df863038525","sort":2,"code":"B","content":"上一年度全国居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":3,"code":"C","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"},{"id":"659b0e46772647ffb997df394f735d00","sort":4,"code":"D","content":"上一年度全国城镇居民人均可支配收入"}],"keywords":"null"},{"id":"68616","type":"001007","level":"003001","content":"关于非全日制用工的描述，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4403042a372a4012a06c24f2c30d0f91","sort":1,"code":"A","content":"劳动者可与一个或一个以上用人单位订立劳动合同"},{"id":"95cc3dcbef024d729a17d23ac8c371ab","sort":2,"code":"B","content":"劳动者在同一用人单位每周工作时间累计不超过20小时"},{"id":"3f32cdc64b2845f8af57d9884e182b23","sort":3,"code":"C","content":"劳动者在同一用人单位一般平均每天工作不超过4小时"},{"id":"cedd50b25f9f4bfebf14a08411411a8a","sort":4,"code":"D","content":"不得约定试用期"}],"keywords":"null"},{"id":"68619","type":"001007","level":"003001","content":"《领取社会保险待遇资格确认经办规程（暂行）》规定，属于丧失领取养老保险待遇资格的人员包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2425ab1a2e5e4efbbb517cb94f9745bb","sort":1,"code":"A","content":"人力资源社会保障服务平台确认及上报的死亡人员"},{"id":"ffe16158fb314d6885bb622fbdf0e9d4","sort":2,"code":"B","content":"家属反映其父母仍然健在的人员"},{"id":"484dea31f666461bac6a785a1438af2e","sort":3,"code":"C","content":"全民参保登记数据库标识为健在但服刑的人员"},{"id":"10707a5ed75745b89d87077d51a0d5bd","sort":4,"code":"D","content":"国家人口库中标识为死亡、有高铁出行记录的人员"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":1,"code":"A","content":"省级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":2,"code":"B","content":"经人力资源社会保障部门授权的单位"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":3,"code":"C","content":"县级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":4,"code":"D","content":"流动人员本人"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":1,"code":"A","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":2,"code":"B","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":3,"code":"C","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"},{"id":"377c82a0fae341139629ddee8f6a400e","sort":4,"code":"D","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":1,"code":"A","content":"超出规定的仲裁审查申请期间的"},{"id":"adfa6de440ea42a588db9548679b987a","sort":2,"code":"B","content":"不属于仲裁委员会受理争议范围"},{"id":"f1a18478c3554009833aa2d6993ded3a","sort":3,"code":"C","content":"不属于本仲裁委员会管辖"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":4,"code":"D","content":"不属于本仲裁委员会管辖"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":1,"code":"A","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":2,"code":"B","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"},{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":3,"code":"C","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":4,"code":"D","content":"约定王某工资为1000元/月，试用期工资为700元/月"}],"keywords":"null"},{"id":"68574","type":"001007","level":"003001","content":"老王在领取失业保险金期间因达到退休年龄办理了退休手续，并开始领取养老金。那么(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0dc709dd74274fedbb89a08feb023003","sort":1,"code":"A","content":"他不可以继续领失业保险金，但可以享受其他失业保险待遇"},{"id":"51829768776847d1995a7bf0331eedc6","sort":2,"code":"B","content":"他可以继续领取剩余的失业保险金"},{"id":"5c9fb3c9a8704de88fd7be3be4cab922","sort":3,"code":"C","content":"他可以再领取一个月的失业保险金"},{"id":"73f7985a40e6455786c037381bf05164","sort":4,"code":"D","content":"他不可以继续领失业保险金"}],"keywords":"null"},{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":1,"code":"A","content":"具有互联网工作经验优先"},{"id":"cd44e594750548e8a9b814d8744f4121","sort":2,"code":"B","content":"需要经常出差，男士优先"},{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":3,"code":"C","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"},{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":4,"code":"D","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"}],"keywords":"null"},{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1161f371d32547158ebc4d0779992cde","sort":1,"code":"A","content":"6个月本人工资的丧葬补助金"},{"id":"5041b2322d4e46ecb88c5ee258187797","sort":2,"code":"B","content":"伤残津贴"},{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":3,"code":"C","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"},{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":4,"code":"D","content":"一次性工亡补助金"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"97366b5104d6412895f3f301041881f1","sort":1,"code":"A","content":"职工（代表）大会决议"},{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":2,"code":"B","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":3,"code":"C","content":"备案函"},{"id":"01107e15e02e4d2f96538f9313d5170f","sort":4,"code":"D","content":"重点情况说明"}],"keywords":"null"},{"id":"68579","type":"001007","level":"003001","content":"某企业职工因工死亡，其生前本人月工资8000元，所在统筹地区上年度职工月平均工资为6000元，其配偶应从工伤保险基金领取丧葬补助金和供养亲属抚恤金分别是多少？","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e185334e3b1d47c98455a6aeb54404f2","sort":1,"code":"A","content":"72000元，每月4000元"},{"id":"89329886b18d48d0944f15c8b0888539","sort":2,"code":"B","content":"36000元，每月4000元"},{"id":"666213be31564dfa99c40513598556d9","sort":3,"code":"C","content":"72000元，每月3200元"},{"id":"80a5607757e44876831d096ec23aba1c","sort":4,"code":"D","content":"36000元，每月3200元"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a082cb3fdd534991930f4cb8693b9894","sort":1,"code":"A","content":"5"},{"id":"438022975c334265a21c2fffb7f465de","sort":2,"code":"B","content":"4"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":3,"code":"C","content":"6"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":4,"code":"D","content":"7"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2fd776cc724e464e9d4fd529d781815f","sort":1,"code":"A","content":"可以签订劳动合同也可以签订劳务协议"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":2,"code":"B","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":3,"code":"C","content":"补贴标准根据乡村生活费用确定"},{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":4,"code":"D","content":"应当为安置人员购买意外伤害商业保险"}],"keywords":"null"},{"id":"68563","type":"001007","level":"003001","content":"职业年金个人账户记账利率根据(    )确定。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7601119a7b14918a6fa15e399479565","sort":1,"code":"A","content":"银行定期存款利率"},{"id":"78114bd83b2f484d9b214d2aec4c9940","sort":2,"code":"B","content":"实账积累部分的投资收益率"},{"id":"a0906be902af4316aeda40b6cc0cfddb","sort":3,"code":"C","content":"上年CPI增幅"},{"id":"5f597299fca34798b1bfe485a0b33c00","sort":4,"code":"D","content":"上年M1增幅"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c5bf34b901e04adeb4129feb04f01116","sort":1,"code":"A","content":"195"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":3,"code":"C","content":"139"},{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":4,"code":"D","content":"145"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"38ac1534bac04628b824eee9c740e6ed","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"57d05cea438c42ceabf4ec28047254c3","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":1,"code":"A","content":"40"},{"id":"03b1512043044934a2d266cff87749f7","sort":2,"code":"B","content":"4"},{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":3,"code":"C","content":"50"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":4,"code":"D","content":"5"}],"keywords":"null"},{"id":"68571","type":"001007","level":"003001","content":"出现下列情形(    )，企业年金方案应当终止。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ac4b6712dda9473f9b10431ef8d6c79b","sort":1,"code":"A","content":"某企业年金集合计划基金财产连续2个月低于500万人民币"},{"id":"526cca00c93346df844b9b82bcb021c0","sort":2,"code":"B","content":"某企业建立企业年金后，因自身短期内经营不善，当前不能继续缴费"},{"id":"ed43688093e94ded8d612a41db90cc01","sort":3,"code":"C","content":"某企业依法宣告破产，企业年金方案已无法履行"},{"id":"038bd80e1eb2484cba5f2c5c60af07ea","sort":4,"code":"D","content":"因不可抗力等原因导致企业年金方案无法履行的"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6a937d1dcae9447cac94ce236451b132","sort":1,"code":"A","content":"4"},{"id":"84f5476d5068448f8d760b6187a1bb35","sort":2,"code":"B","content":"5"},{"id":"40e7e2db81604a22aa8cab33cc970533","sort":3,"code":"C","content":"3"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":4,"code":"D","content":"6"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"973b9a79351146a4acac647acc0331ff","sort":1,"code":"A","content":"地市级城市安置区"},{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":2,"code":"B","content":"高寒、高海拔安置区"},{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":3,"code":"C","content":"“三区三州”等深度贫困地区安置区"},{"id":"846e95aa078f4798b9f2adda36932a45","sort":4,"code":"D","content":"人口规模1000人以上大型安置区"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68632","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者依法享受探亲假、婚丧假、节育手术假等国家规定的假期间&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，视为正常劳动，但带薪年休假假期除外。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"24626dda34f14a6e9f995a0013ac89ff","sort":1,"code":"A","content":"正确"},{"id":"4e8385dc8c2842628b6006f8fecbe7c7","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68629","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;在确定事业单位专业技术高级、中级、初级岗位内部不同等级岗位之间的结构比例时，事业单位的隶属关系是考量因素之一。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3f3bb9efec414414930731eea2e812a1","sort":1,"code":"A","content":"正确"},{"id":"bc4688d2e71b4c7cb641d78bd9022cbb","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68628","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;行政处罚的执法决定信息要在执法决定作出之日起&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;10&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个工作日内公开。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"046bf5236b13491099ac1a0a9bf3e53e","sort":1,"code":"A","content":"正确"},{"id":"25003e89e9124301a0b6bb36c7c465e4","sort":2,"code":"B","content":"错误"}],"keywords":"null"}]}]},"code":"SUCCESS"}
json_0627_answer6 = {"httpStatus":"OK","status":0,"message":"成功","data":[{"id":"68612","type":"001007","level":"003001","content":"劳动争议仲裁时效中断的情形包括（    ）。","answer":"A,B,C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e07bc7a86d4a4dd194dc7c45a90a3d6b","sort":1,"code":"A","content":"张某主动要求用人单位支付加班工资，用人单位否认拖欠工资报酬"},{"id":"493382fe56de47f3aa0a3f28d36a5556","sort":2,"code":"B","content":"张某向调解组织申请，希望调解组织组织调解用人单位与其个人的劳动纠纷"},{"id":"3c73b4e2e0f94b6ca1ded207e503dc61","sort":3,"code":"C","content":"用人单位书面承诺，3个月内向劳动者支付拖欠的劳动报酬"},{"id":"c0aa12a2e1a04eee8762906faa99857d","sort":4,"code":"D","content":"针对用人单位拖欠的工资报酬，张某想了几个月，觉得耗时耗力，最终放弃了"}],"keywords":"null"},{"id":"68580","type":"001007","level":"003001","content":"《工伤保险条例》规定，一次性工亡补助金标准是(    )的20倍","answer":"C","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a7ae703580c542398303612d32f10288","sort":1,"code":"A","content":"上一年度全省城镇居民人均可支配收入"},{"id":"da0164df20a6444ea9c06df863038525","sort":2,"code":"B","content":"上一年度全国居民人均可支配收入"},{"id":"659b0e46772647ffb997df394f735d00","sort":3,"code":"C","content":"上一年度全国城镇居民人均可支配收入"},{"id":"70c54210b28b4fc2bb39190d8dcb803a","sort":4,"code":"D","content":"本年度工伤保险统筹区内城镇居民人均可支配收入"}],"keywords":"null"},{"id":"68628","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;行政处罚的执法决定信息要在执法决定作出之日起&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;10&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;个工作日内公开。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"B","analysis":"","score":"null","userAnswer":"null","blanksNumber":"null","signed":"null","checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"046bf5236b13491099ac1a0a9bf3e53e","sort":1,"code":"A","content":"正确"},{"id":"25003e89e9124301a0b6bb36c7c465e4","sort":2,"code":"B","content":"错误"}],"keywords":"null"}],"code":"SUCCESS"}

json_0627_test7 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"88fec56155cd44cca618253f1ed848ab","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599340,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68623","type":"001007","level":"003001","content":"伤残职工停工留薪期满内因工伤导致死亡，其近亲属依法可以享受的待遇是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5041b2322d4e46ecb88c5ee258187797","sort":1,"code":"A","content":"伤残津贴"},{"id":"9004ce2a302143a49ff9e42d44e492ad","sort":2,"code":"B","content":"一次性工亡补助金"},{"id":"e4559b46ad9a40fdb5ff2dafa8751180","sort":3,"code":"C","content":"按照统筹地区月平均工资一定比例的供养亲属抚恤金"},{"id":"1161f371d32547158ebc4d0779992cde","sort":4,"code":"D","content":"6个月本人工资的丧葬补助金"}],"keywords":"null"},{"id":"68614","type":"001007","level":"003001","content":"企业裁减人员时，依法应当优先留用（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"77f2089cced8489a8c83c2ef45b7d43c","sort":1,"code":"A","content":"与本单位订立8年期限劳动合同的人员"},{"id":"1fd8155b7ba64462ab9c9bd68a31a9ab","sort":2,"code":"B","content":"家庭有需要扶养的老人"},{"id":"23b4206865ef40298f20596679a00de0","sort":3,"code":"C","content":"掌握企业核心技术、对企业发展至关重要的人员"},{"id":"8742eccd8e41413688b3941288fc3c41","sort":4,"code":"D","content":"与本单位订立无固定期限劳动合同的人员"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":1,"code":"A","content":"省级公共就业和人才服务机构"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":2,"code":"B","content":"县级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":3,"code":"C","content":"流动人员本人"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":4,"code":"D","content":"经人力资源社会保障部门授权的单位"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"defeb3d10031449d86eaf10f6271a331","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":2,"code":"B","content":"1"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":3,"code":"C","content":"2"},{"id":"394106514712430bad66fd4bf853deb1","sort":4,"code":"D","content":"3"}],"keywords":"null"},{"id":"68618","type":"001007","level":"003001","content":"甲公司介绍三名13周岁未成年人到乙公司工作。甲公司应被罚款(    )元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d40b2572feab4410b822d497ee817674","sort":1,"code":"A","content":"15000"},{"id":"91dd009201e2490a924cab882346306d","sort":2,"code":"B","content":"4000"},{"id":"fc2a44ec470d4c389cd50befa6053a2a","sort":3,"code":"C","content":"10000"},{"id":"f8fee2535baa4419bb4bf460573f232a","sort":4,"code":"D","content":"8000"}],"keywords":"null"},{"id":"68611","type":"001007","level":"003001","content":"用人单位有下列（    ）情形的，劳动者可以解除劳动合同。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"650abb015d27483490fe7e4888278af8","sort":1,"code":"A","content":"未依法为劳动者购买意外伤害险的"},{"id":"dc6c86086ec541daa0696055a59ed2b1","sort":2,"code":"B","content":"未按照劳动合同约定提供劳动保护的"},{"id":"c34ef1a7fe764b34bc462de3915eef12","sort":3,"code":"C","content":"根据经营需要，与劳动者协商加班的"},{"id":"80e05fb12f1344fbba2f0776f4d6831c","sort":4,"code":"D","content":"未及时足额支付劳动者工资的"}],"keywords":"null"},{"id":"68576","type":"001007","level":"003001","content":"以建设项目为单位参保的建筑企业，可以按照(    )的一定比例计算缴纳工伤保险费。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1517719a0cda40b0ab282c74e67368d8","sort":1,"code":"A","content":"工资总额"},{"id":"e9aadb1f63024e34a14885585a223fa9","sort":2,"code":"B","content":"当地平均工资"},{"id":"af3b6737393c465599080524c7cce70d","sort":3,"code":"C","content":"以上皆可"},{"id":"bbe9b096e1b54c6a92643641bca1f5f6","sort":4,"code":"D","content":"项目工程总造价"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":1,"code":"A","content":"96000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":2,"code":"B","content":"108000元"},{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":3,"code":"C","content":"60000元"},{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":4,"code":"D","content":"84000元"}],"keywords":"null"},{"id":"68561","type":"001007","level":"003001","content":"王某在某县直属事业单位工作，其当地上年度在岗职工平均工资是30000元，王某个人上年度工资是100000元，（    ）不计入王某个人缴费工资基数。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"25f07a9858854902a7f5513177500991","sort":1,"code":"A","content":"60000元"},{"id":"16f20c281c794a91a6c95a3b39906a17","sort":2,"code":"B","content":"30000元"},{"id":"f741138316654c55b9c78bf21488a952","sort":3,"code":"C","content":"10000元"},{"id":"f507bc94dcde431cb1b0717eef448115","sort":4,"code":"D","content":"40000元"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":1,"code":"A","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":2,"code":"B","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":3,"code":"C","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":4,"code":"D","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"}],"keywords":"null"},{"id":"68596","type":"001007","level":"003001","content":"对公益性岗位安置就业困难人员给予（    ）补贴，补贴标准参照当地最低工资标准执行。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"75cff79c4fa4442984d5b9b8cd41f29c","sort":1,"code":"A","content":"生活"},{"id":"24867d24ce5a467e9d86aa5e02d16624","sort":2,"code":"B","content":"救济"},{"id":"fd638b2f28974d8bb2e636ba9c6cabff","sort":3,"code":"C","content":"岗位"},{"id":"fffaae54e22b4080a0cdd4b54084847f","sort":4,"code":"D","content":"交通"}],"keywords":"null"},{"id":"68621","type":"001007","level":"003001","content":"关于从事个体工商经营的香港居民在内地参加社会保险，错误的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c1c2d1e02e8a4cd98419cdfaa2f13e49","sort":1,"code":"A","content":"在居住地参加社会保险"},{"id":"a1b641859d98482e920a476122b69775","sort":2,"code":"B","content":"可以参加职工基本养老保险"},{"id":"c5d09d6c990a4f0da234d26811d2ce60","sort":3,"code":"C","content":"在注册地参加社会保险"},{"id":"63d3b5c78c35424abe387d1e1b9eaaab","sort":4,"code":"D","content":"可以参加职工基本医疗保险"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bcbfd8add87943f0ace414c4194d3546","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e3125d07cd0446a89213ec98e18812ab","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":1,"code":"A","content":"50"},{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":2,"code":"B","content":"5"},{"id":"03b1512043044934a2d266cff87749f7","sort":3,"code":"C","content":"4"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":4,"code":"D","content":"40"}],"keywords":"null"},{"id":"68565","type":"001007","level":"003001","content":"企业职工基本养老保险中央调剂基金由各省份养老保险基金上解的资金构成。按照各省份职工平均工资的(    )和在职应参保人数作为计算上解额的基数，上解比例从(    )起步，逐步提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"eda8f0ab8ad4412db86793bebc83f28d","sort":1,"code":"A","content":"80%；3%"},{"id":"43ddec4cd71e4923a09e3b8898825e74","sort":2,"code":"B","content":"80%；3.5%"},{"id":"79e7d517e5c14955af8ca6803e8d180a","sort":3,"code":"C","content":"90%；3%"},{"id":"6cce8cd0ef46464fac76fea4b3041cff","sort":4,"code":"D","content":"90%；3.5%"}],"keywords":"null"},{"id":"68575","type":"001007","level":"003001","content":"A企业注册地在北京，生产经营地在天津，一部分职工被派出在山东工作，原则上应在(    )为这些职工参加工伤保险。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2b9720ced3c6473ba842256c0f4c0bcb","sort":1,"code":"A","content":"山东"},{"id":"47b3e97dd66e45658017ebf1cea64c51","sort":2,"code":"B","content":"职工户籍所在地"},{"id":"55180558f6bc48c5bebed340833a779f","sort":3,"code":"C","content":"天津"},{"id":"b2b033f986284933a47b14d742bfa453","sort":4,"code":"D","content":"北京"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"adfa6de440ea42a588db9548679b987a","sort":1,"code":"A","content":"不属于仲裁委员会受理争议范围"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":2,"code":"B","content":"超出规定的仲裁审查申请期间的"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":3,"code":"C","content":"不属于本仲裁委员会管辖"},{"id":"f1a18478c3554009833aa2d6993ded3a","sort":4,"code":"D","content":"不属于本仲裁委员会管辖"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":1,"code":"A","content":"正常运营1个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":2,"code":"B","content":"正常运营5个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":3,"code":"C","content":"正常运营7个月"},{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":4,"code":"D","content":"正常运营3个月"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ae4a91f95a049629966229077ae4831","sort":1,"code":"A","content":"可以弃档不管"},{"id":"623bf52e22c84515b275a537283e7b8e","sort":2,"code":"B","content":"可直接从学校转递到企业"},{"id":"4f6cf14fd2b249109922524a550c021b","sort":3,"code":"C","content":"个人自带"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":4,"code":"D","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":1,"code":"A","content":"10"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":2,"code":"B","content":"12"},{"id":"8e5fd62e7b12443db02196646c2f3315","sort":3,"code":"C","content":"5"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":4,"code":"D","content":"8"}],"keywords":"null"},{"id":"68570","type":"001007","level":"003001","content":"下属单位加入集团公司企业年金计划备案时所需材料包括 (    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"97366b5104d6412895f3f301041881f1","sort":1,"code":"A","content":"职工（代表）大会决议"},{"id":"01107e15e02e4d2f96538f9313d5170f","sort":2,"code":"B","content":"重点情况说明"},{"id":"b2a1d32efcae4c74adc86caabf107a89","sort":3,"code":"C","content":"企业年金方案"},{"id":"dc3f51ee6cd2444a8482ef9413cf60fc","sort":4,"code":"D","content":"备案函"}],"keywords":"null"},{"id":"68571","type":"001007","level":"003001","content":"出现下列情形(    )，企业年金方案应当终止。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"526cca00c93346df844b9b82bcb021c0","sort":1,"code":"A","content":"某企业建立企业年金后，因自身短期内经营不善，当前不能继续缴费"},{"id":"ac4b6712dda9473f9b10431ef8d6c79b","sort":2,"code":"B","content":"某企业年金集合计划基金财产连续2个月低于500万人民币"},{"id":"038bd80e1eb2484cba5f2c5c60af07ea","sort":3,"code":"C","content":"因不可抗力等原因导致企业年金方案无法履行的"},{"id":"ed43688093e94ded8d612a41db90cc01","sort":4,"code":"D","content":"某企业依法宣告破产，企业年金方案已无法履行"}],"keywords":"null"},{"id":"68612","type":"001007","level":"003001","content":"劳动争议仲裁时效中断的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3c73b4e2e0f94b6ca1ded207e503dc61","sort":1,"code":"A","content":"用人单位书面承诺，3个月内向劳动者支付拖欠的劳动报酬"},{"id":"c0aa12a2e1a04eee8762906faa99857d","sort":2,"code":"B","content":"针对用人单位拖欠的工资报酬，张某想了几个月，觉得耗时耗力，最终放弃了"},{"id":"e07bc7a86d4a4dd194dc7c45a90a3d6b","sort":3,"code":"C","content":"张某主动要求用人单位支付加班工资，用人单位否认拖欠工资报酬"},{"id":"493382fe56de47f3aa0a3f28d36a5556","sort":4,"code":"D","content":"张某向调解组织申请，希望调解组织组织调解用人单位与其个人的劳动纠纷"}],"keywords":"null"},{"id":"68609","type":"001007","level":"003001","content":"为满足非公有制经济组织、社会组织以及新兴业态职称评价需求，要建立完善（    ）的社会化评审机制。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e8835a3ba4fa4f6a9934a906067793e7","sort":1,"code":"A","content":"政府依法认定"},{"id":"37617262af704c8a9268a3f473b5ba53","sort":2,"code":"B","content":"个人自主申报"},{"id":"f021e857a2dc490caeb862efdbe11e28","sort":3,"code":"C","content":"单位择优使用"},{"id":"c061856c1ecf4628b7a9c1a92c252465","sort":4,"code":"D","content":"业内公正评价"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"20775075cd5b451b827342aa85304fc7","sort":1,"code":"A","content":"城镇劳动力"},{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":2,"code":"B","content":"农村劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":3,"code":"C","content":"高校劳动力"},{"id":"f1fb45ece27943f1b08b0390638b8438","sort":4,"code":"D","content":"城乡劳动力"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":1,"code":"A","content":"工作权"},{"id":"a6937611ca064abfb27cba90c8064169","sort":2,"code":"B","content":"入境权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":3,"code":"C","content":"民事权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":4,"code":"D","content":"定居权"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":1,"code":"A","content":"补贴标准根据乡村生活费用确定"},{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":2,"code":"B","content":"应当为安置人员购买意外伤害商业保险"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":3,"code":"C","content":"可以签订劳动合同也可以签订劳务协议"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":4,"code":"D","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d65251be089d41c4b34b375a5c4e130c","sort":1,"code":"A","content":"与档案接收机构协商，想办法为小李办理。"},{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":2,"code":"B","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":3,"code":"C","content":"按照小李的要求为其办理转正定级手续"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":4,"code":"D","content":"拒绝小李的要求，并为小李讲解相关政策规定"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b34b2d30e563409e9615ece5765d7739","sort":1,"code":"A","content":"9；3；4"},{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":2,"code":"B","content":"9；2；3"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":3,"code":"C","content":"10；4；5"},{"id":"6491ca747d40446b9851d75b5d998c5f","sort":4,"code":"D","content":"10；5；6"}],"keywords":"null"},{"id":"68560","type":"001007","level":"003001","content":"（    ）参加劳动预备制培训的，可以享受一定标准的生活费补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6f9319af9c2c4dbbac85f623eb4cd331","sort":1,"code":"A","content":"城市低保家庭学员"},{"id":"c9efc2fba21f4e0d8ab0f96d8fa16667","sort":2,"code":"B","content":"农村学员"},{"id":"0336f625724641558e729178184964c5","sort":3,"code":"C","content":"应届初高中毕业生"},{"id":"2050b405c33d4e62882bb572311fc967","sort":4,"code":"D","content":"困难家庭学员"}],"keywords":"null"},{"id":"68564","type":"001007","level":"003001","content":"王大姐今年42岁，自2009年开始从事高温工种，可以（   ）年退休。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"99918d07c41a4cb7bb0d6926af2a5e4f","sort":1,"code":"A","content":"2023"},{"id":"d393b9f42b594346bacf7e7db5375709","sort":2,"code":"B","content":"2020"},{"id":"8ada3e4200ed486aa248102ccddecad0","sort":3,"code":"C","content":"2022"},{"id":"993532115f804f0b9d90b796fb5c5e0e","sort":4,"code":"D","content":"2021"}],"keywords":"null"},{"id":"68591","type":"001007","level":"003001","content":"用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"741b8f627d864ab3999fe4d9cea6ae87","sort":1,"code":"A","content":"按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同"},{"id":"3372645120c247f4b83b3120312dbd92","sort":2,"code":"B","content":"员工承诺，在本公司工作期间遵守规章制度"},{"id":"107b86939e514a7f8f50b7d96b2507a1","sort":3,"code":"C","content":"员工自愿承诺，在本公司工作期间不结婚"},{"id":"96175f4056be4936b13f9307e2eb2ae0","sort":4,"code":"D","content":"公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":1,"code":"A","content":"8000元"},{"id":"1045b445dbf340f992680615412a2c36","sort":2,"code":"B","content":"10000元"},{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":3,"code":"C","content":"4000元"},{"id":"1e922892adfa4cc291ccc8e08086313f","sort":4,"code":"D","content":"6000元"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"377c82a0fae341139629ddee8f6a400e","sort":1,"code":"A","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":2,"code":"B","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":3,"code":"C","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"},{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":4,"code":"D","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"}],"keywords":"null"},{"id":"68550","type":"001007","level":"003001","content":"小王今年大学毕业，如果他（    ），可享受职业技能鉴定补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e730086b1f9a4387ac46ce90770dbbf7","sort":1,"code":"A","content":"参加了职业技能培训"},{"id":"2e0d1eb028404a68a8eb7893cc8eee3b","sort":2,"code":"B","content":"取得了人社部门颁发的培训合格证书"},{"id":"dcc59cb8751848e89c4c606206e50387","sort":3,"code":"C","content":"通过了初次职业技能鉴定并取得职业资格证书"},{"id":"83d0ef84425e48aba2eba8f0081b74de","sort":4,"code":"D","content":"取得了职业资格证书"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5f415af62962421ebe130734f5103ae3","sort":1,"code":"A","content":"安全保管企业年金基金财产"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":2,"code":"B","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":3,"code":"C","content":"及时办理清算、交割事宜"},{"id":"3413d86553634b5c958740b3ec761da0","sort":4,"code":"D","content":"制定企业年金基金战略资产配置策略"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"40e7e2db81604a22aa8cab33cc970533","sort":1,"code":"A","content":"3"},{"id":"84f5476d5068448f8d760b6187a1bb35","sort":2,"code":"B","content":"5"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":3,"code":"C","content":"6"},{"id":"6a937d1dcae9447cac94ce236451b132","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68595","type":"001007","level":"003001","content":"享受职业培训补贴的人员包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6fa8d4329e7e4a749f2632af18a07daf","sort":1,"code":"A","content":"贫困家庭子女"},{"id":"5d3526a8261343468d01869caa805ef4","sort":2,"code":"B","content":"毕业年度高校毕业生"},{"id":"9d5f8bdd6bf549c7aa906d279599b717","sort":3,"code":"C","content":"城镇登记失业人员"},{"id":"2570b08e054849a0b5cb090ee49278aa","sort":4,"code":"D","content":"农村转移就业劳动者"}],"keywords":"null"},{"id":"68566","type":"001007","level":"003001","content":"在我国就业的外国人领取养老保险待遇的年龄，原则上执行(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"06e499fbbc6c467d85fcd66f8ec81222","sort":1,"code":"A","content":"我国退休年龄政策"},{"id":"c201c3f515044f70abba35079d08948a","sort":2,"code":"B","content":"外国人国籍国退休年龄政策"},{"id":"660287329b444b84b0c26d2dc1fd909e","sort":3,"code":"C","content":"我国退休年龄政策，如果外国人国籍国退休年龄晚于我国退休年龄，则执行外国人国籍国退休年龄政策"},{"id":"a59921796e884cf9a15f6a87c6beb649","sort":4,"code":"D","content":"我国退休年龄政策，如果属于与我国签订社会保险缴费双边或多边协议的国家，则执行该国退休年龄政策"}],"keywords":"null"},{"id":"68574","type":"001007","level":"003001","content":"老王在领取失业保险金期间因达到退休年龄办理了退休手续，并开始领取养老金。那么(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"73f7985a40e6455786c037381bf05164","sort":1,"code":"A","content":"他不可以继续领失业保险金"},{"id":"0dc709dd74274fedbb89a08feb023003","sort":2,"code":"B","content":"他不可以继续领失业保险金，但可以享受其他失业保险待遇"},{"id":"51829768776847d1995a7bf0331eedc6","sort":3,"code":"C","content":"他可以继续领取剩余的失业保险金"},{"id":"5c9fb3c9a8704de88fd7be3be4cab922","sort":4,"code":"D","content":"他可以再领取一个月的失业保险金"}],"keywords":"null"},{"id":"68552","type":"001007","level":"003001","content":"企业今年有10名见习生，见习期满留用（  ）人的，该企业享受的见习补贴标准可以适当提高。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"438022975c334265a21c2fffb7f465de","sort":1,"code":"A","content":"4"},{"id":"842cc2116bc944d293f05fd38d4458f7","sort":2,"code":"B","content":"7"},{"id":"9ba686b6c35941f6acefabbb3bf7cb38","sort":3,"code":"C","content":"6"},{"id":"a082cb3fdd534991930f4cb8693b9894","sort":4,"code":"D","content":"5"}],"keywords":"null"},{"id":"68725","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年5月至12月，对2019年1月1日之后参保不满( &nbsp;&nbsp;)的失业农民工，参照参保地城市低保标准，按月发放不超过( &nbsp;&nbsp;)个月的临时生活补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c16cbd2548cd4f78b46e6a212158fa32","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e6643bbfec93471f888bb4891304f525","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9bcba69d0e274fd4ade1bb6e44238fd8","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"97071a22bb11498384baf737fd2d7635","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68602","type":"001007","level":"003001","content":"关于企业未经许可擅自从事职业中介的罚款规定，错误的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a4e0360a5ff543899c86ba90848e07b4","sort":1,"code":"A","content":"行政机关作出较大数额罚款决定之前，应当告知当事人有要求举行听证的权利"},{"id":"d4c856b634ba4590b329500c0fd45234","sort":2,"code":"B","content":"罚款金额最高不得超过5万元"},{"id":"0b77c0cf7abf4a258cdc71413f127925","sort":3,"code":"C","content":"罚款金额为违法所得的50%至200%"},{"id":"42bc24a6a7014377bb9cc2fadc893ba4","sort":4,"code":"D","content":"只有符合行政机关依法责令改正和企业拒不改正两个前提条件下，才能处以罚款"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"583b9bc056c641ffa095ef97015a8380","sort":1,"code":"A","content":"常住地；出生地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":2,"code":"B","content":"常住地；常住地"},{"id":"5a22297e9c5e42588338374f2db13853","sort":3,"code":"C","content":"出生地；户籍地"},{"id":"c663276dfd0b4d2c93e4177521a14071","sort":4,"code":"D","content":"原单位注册地；常住地"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":1,"code":"A","content":"不设参保年限"},{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":2,"code":"B","content":"累计参保缴费满三年"},{"id":"df3ec29881de4e89a74191f1b922cccb","sort":3,"code":"C","content":"累计参保缴费满一年"},{"id":"84fdcd3629f2496597b7906039f6acaf","sort":4,"code":"D","content":"累计参保缴费满二年"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68633","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;生效了的专项集体合同，应当自生效之日起由协商代表及时以适当的方式向本方全体人员公布。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"591f2e658eea491e936cb7ef47084f89","sort":1,"code":"A","content":"错误"},{"id":"590f278ac32a4a979247de53953c62f3","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68632","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;劳动者依法享受探亲假、婚丧假、节育手术假等国家规定的假期间&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;，视为正常劳动，但带薪年休假假期除外。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4e8385dc8c2842628b6006f8fecbe7c7","sort":1,"code":"A","content":"错误"},{"id":"24626dda34f14a6e9f995a0013ac89ff","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68626","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;地方各级人民政府和有关部门、公共就业服务机构举办的招聘会，不得向劳动者和用人单位收取费用。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3721c379c2234614901770842b2364d8","sort":1,"code":"A","content":"错误"},{"id":"e45d789984ba4d87b23af1578f8d6635","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]}]},"code":"SUCCESS"}

json_0627_test8 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"a756ae910e81499e97adef4985b9b42a","conclusions":"感谢您的参与！","description":"null","name":"6月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599809,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":94.0,"totalNumbers":47,"description":"不定项选择题，可能有一个或多个正确答案","questions":[{"id":"68600","type":"001007","level":"003001","content":"按照现行规定，面向个人发放的创业担保贷款期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"24092da8dfdf4c9e910f8421d51e885c","sort":1,"code":"A","content":"2"},{"id":"414a064395064954a551f10efd6a73d9","sort":2,"code":"B","content":"3"},{"id":"d7d57727a08f4884950a0f667f43caf4","sort":3,"code":"C","content":"4"},{"id":"cfb5ba55490b49fd91dd7d7e0a82de7d","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68558","type":"001007","level":"003001","content":"北京市某职业学校和当地某企业开展合作，该企业接收实习生，合作期限可以是(    )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6a937d1dcae9447cac94ce236451b132","sort":1,"code":"A","content":"4"},{"id":"84f5476d5068448f8d760b6187a1bb35","sort":2,"code":"B","content":"5"},{"id":"40e7e2db81604a22aa8cab33cc970533","sort":3,"code":"C","content":"3"},{"id":"e5e6a7663e724028bcb5b54ad7eaa5b4","sort":4,"code":"D","content":"6"}],"keywords":"null"},{"id":"68581","type":"001007","level":"003001","content":"如果工亡职工的供养亲属生活有困难，可以预支上一年度全国城镇居民人均可支配收入（    ）倍的一次性工亡补助金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8e5fd62e7b12443db02196646c2f3315","sort":1,"code":"A","content":"5"},{"id":"adada23fbc60449aac5da4f3ce86f7d2","sort":2,"code":"B","content":"8"},{"id":"fa2eff2332db480bb943d82d5905e4b9","sort":3,"code":"C","content":"10"},{"id":"6e5af75f37464cc2afab5317fedd1a04","sort":4,"code":"D","content":"12"}],"keywords":"null"},{"id":"68590","type":"001007","level":"003001","content":"不属于对劳动者就业歧视的情形包括(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8d7baa1d923e4039b16bd89c5f30bf07","sort":1,"code":"A","content":"本岗位需要值夜班，怀孕8个月以上的女性不予考虑"},{"id":"976202c2e2514ebf914a08a51c5b5ea6","sort":2,"code":"B","content":"具有互联网工作经验优先"},{"id":"cd44e594750548e8a9b814d8744f4121","sort":3,"code":"C","content":"需要经常出差，男士优先"},{"id":"865b11cc23da4230ae5ffbc55f88239d","sort":4,"code":"D","content":"本职位需要经常加班，如身体欠佳、属传染病病原携带者的求职者不予考虑"}],"keywords":"null"},{"id":"68562","type":"001007","level":"003001","content":"张某（女，55周岁）于2020年1月份在某事业单位到龄退休，其个人账户养老金的计发月数为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d7e1664c6c9444eaadb98e1b10d62512","sort":1,"code":"A","content":"145"},{"id":"e28f6910c6534787be27eabf8916e0f1","sort":2,"code":"B","content":"170"},{"id":"c5bf34b901e04adeb4129feb04f01116","sort":3,"code":"C","content":"195"},{"id":"c91ba5d4b2f14ca58bd7c8793ed7d838","sort":4,"code":"D","content":"139"}],"keywords":"null"},{"id":"68722","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对&amp;2526lt;/span&amp;2526gt;2020年3月至12月，领取失业保险金期满仍未就业的失业人员、不符合领取失业保险金条件的参保失业人员，发放（ &nbsp;&nbsp;）个月的失业补助金，标准不高于当地失业保险金的（ &nbsp;&nbsp;&nbsp;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c2c76fcab56746099f6e0020afb20110","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"d8243054793d442c9577daac5446188a","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;8；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"7383c2af02604820b6882b632b404923","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"b49f0e5f79a8463cbb91d053a19a69cc","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6；60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68553","type":"001007","level":"003001","content":"小微企业吸纳高校毕业生就业的社保补贴范围，扩大到离校（    ）年内未就业高校毕业生","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3fb2591e80644d728e5537f6ad9ca999","sort":1,"code":"A","content":"4"},{"id":"1ac5dc9603cd42f3a0e80b18dc36db25","sort":2,"code":"B","content":"2"},{"id":"394106514712430bad66fd4bf853deb1","sort":3,"code":"C","content":"3"},{"id":"15453e5dc27b4ca296c6bc449fb8cb51","sort":4,"code":"D","content":"1"}],"keywords":"null"},{"id":"68583","type":"001007","level":"003001","content":"城乡居民基本养老保险最高缴费档次标准原则上不超过当地(    )参加职工基本养老保险的年缴费额。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"69e21d5c8f1744b189967826d3bda008","sort":1,"code":"A","content":"社会组织人员"},{"id":"d57337d54ad1408bac0f4626029888d4","sort":2,"code":"B","content":"灵活就业人员"},{"id":"e389eef064b8405488a2e37fcd58d4ea","sort":3,"code":"C","content":"企业职工"},{"id":"5373234878474becb562233802a15c39","sort":4,"code":"D","content":"机关事业单位人员"}],"keywords":"null"},{"id":"68607","type":"001007","level":"003001","content":"在易地扶贫搬迁就业帮扶工作中，安置的重点区域包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"846e95aa078f4798b9f2adda36932a45","sort":1,"code":"A","content":"人口规模1000人以上大型安置区"},{"id":"fbd8cc1839b14f7daeb35d60b81e5d33","sort":2,"code":"B","content":"高寒、高海拔安置区"},{"id":"1d230b60712b4339ad7947a8c4ed8b59","sort":3,"code":"C","content":"“三区三州”等深度贫困地区安置区"},{"id":"973b9a79351146a4acac647acc0331ff","sort":4,"code":"D","content":"地市级城市安置区"}],"keywords":"null"},{"id":"68567","type":"001007","level":"003001","content":"按照现行企业年金制度，某企业当年年度工资总额为500万元，该企业当年度缴纳企业年金的额度，不符合规定的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e1171cc6d05742a18d04fb02b1fcfcc8","sort":1,"code":"A","content":"20万元"},{"id":"f0c637e8214e4881b3a497b10801045a","sort":2,"code":"B","content":"40万元"},{"id":"d6da7cd4c58e4d47966177125dc00cf6","sort":3,"code":"C","content":"80万元"},{"id":"62ff517715bf4207a464dfc56e981f84","sort":4,"code":"D","content":"100万元"}],"keywords":"null"},{"id":"68597","type":"001007","level":"003001","content":"属于高校毕业生基层服务项目的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a3d35ea01e424f67ac8b84525f318ca7","sort":1,"code":"A","content":"“三支一扶”计划"},{"id":"b8f6e68bbba84a7ba269bfaefaefe9c3","sort":2,"code":"B","content":"“凤凰飞翔”计划"},{"id":"1c1f46c89b06468eb1497d0825bd0658","sort":3,"code":"C","content":"志愿服务西部计划"},{"id":"a9983ec2a62b48e9915eb0112bc48a3c","sort":4,"code":"D","content":"公益就业行动计划"}],"keywords":"null"},{"id":"68572","type":"001007","level":"003001","content":"某参保企业坚持不裁员，上年度实际缴纳社保费100万元（含失业保险费10万元），根据《关于失业保险支持企业稳定就业岗位的通知》，可向企业支付稳岗返还补贴（    ）万元。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b126c54fa6ef4010a40e5f116fa1a418","sort":1,"code":"A","content":"5"},{"id":"e3e7d48f078640eeab81eb21a3a4f021","sort":2,"code":"B","content":"40"},{"id":"c3b22e9e45464c2b8c3b922c7d84c918","sort":3,"code":"C","content":"50"},{"id":"03b1512043044934a2d266cff87749f7","sort":4,"code":"D","content":"4"}],"keywords":"null"},{"id":"68598","type":"001007","level":"003001","content":"为推动（    ）有序外出就业，对市场主体开展有组织劳务输出的，给予就业创业服务补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"20775075cd5b451b827342aa85304fc7","sort":1,"code":"A","content":"城镇劳动力"},{"id":"6bc327dbcc0d466f9427fe024638ef2a","sort":2,"code":"B","content":"农村劳动力"},{"id":"f1fb45ece27943f1b08b0390638b8438","sort":3,"code":"C","content":"城乡劳动力"},{"id":"35be41b5c1e049f6b7656ee6f7652fa2","sort":4,"code":"D","content":"高校劳动力"}],"keywords":"null"},{"id":"68582","type":"001007","level":"003001","content":"老王因工伤生活不能自理，现停工留薪期需要护理。老王的（   ）可以从工伤保险基金支出。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5a143c14dde44889bb20d45be1c5adf5","sort":1,"code":"A","content":"生活护理费"},{"id":"ad60dee7c6a1413b9b8ee7555bd84922","sort":2,"code":"B","content":"伙食补助费"},{"id":"bd8a68d0a39b4dd8bb431ded378294b9","sort":3,"code":"C","content":"赴统筹地区以外就医所需交通、食宿费"},{"id":"66b9b5278b7d4a428a4e2f9f6d307925","sort":4,"code":"D","content":"工伤医疗待遇"}],"keywords":"null"},{"id":"68620","type":"001007","level":"003001","content":"在办理机关事业单位职业年金转移接续时，无需转移的基金项目包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"83c5e0f5fd124299b2aadccc4da44c6e","sort":1,"code":"A","content":"原转入的企业年金"},{"id":"4038e407cd32415e941dc64bc86f7969","sort":2,"code":"B","content":"个人缴费本息"},{"id":"f7c56f8bb62f4a2eae54ee2e7da8edff","sort":3,"code":"C","content":"补记的职业年金"},{"id":"cc0fe7a8998f46a4b1392c42b28a687a","sort":4,"code":"D","content":"缴费形成的职业年金"}],"keywords":"null"},{"id":"68725","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年5月至12月，对2019年1月1日之后参保不满( &nbsp;&nbsp;)的失业农民工，参照参保地城市低保标准，按月发放不超过( &nbsp;&nbsp;)个月的临时生活补助。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c16cbd2548cd4f78b46e6a212158fa32","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e6643bbfec93471f888bb4891304f525","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;12个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"97071a22bb11498384baf737fd2d7635","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；6个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9bcba69d0e274fd4ade1bb6e44238fd8","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;6个月；3个月&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68587","type":"001007","level":"003001","content":"老王2019年9月因工外出发生事故，从（  ）月起(    )个月内照发工资，从第(    )个月起停发工资，由工伤保险基金向其供养亲属按月支付供养亲属抚恤金。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6491ca747d40446b9851d75b5d998c5f","sort":1,"code":"A","content":"10；5；6"},{"id":"0c66b96fc51741c4896a685321e4b225","sort":2,"code":"B","content":"10；4；5"},{"id":"6618a17aa86c4677a3d6666b65ec01a2","sort":3,"code":"C","content":"9；2；3"},{"id":"b34b2d30e563409e9615ece5765d7739","sort":4,"code":"D","content":"9；3；4"}],"keywords":"null"},{"id":"68613","type":"001007","level":"003001","content":"属于人社行政部门审查集体合同合法性的事项包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b498d2c3899b4e34af9c44d6b8fd8c00","sort":1,"code":"A","content":"补充保险和福利约定是否符合国家有关规"},{"id":"d5b143b8f7de423da117509b15fcb6ed","sort":2,"code":"B","content":"集体合同约定的工资增幅是否合理"},{"id":"d76d9d824b1348c190e381f06a178776","sort":3,"code":"C","content":"协商程序是否履行《集体合同规定》所规定的具体程序"},{"id":"93cc751f4650480e8ba4cb651a1fba72","sort":4,"code":"D","content":"职工一方协商代表资格是否符合国家有关规定"}],"keywords":"null"},{"id":"68603","type":"001007","level":"003001","content":"《人力资源市场暂行条例》规定，未按规定提交经营情况年度报告，且拒不改正的，罚款金额可以是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1045b445dbf340f992680615412a2c36","sort":1,"code":"A","content":"10000元"},{"id":"688c684404bc4abf9cc5118cf1ca95f4","sort":2,"code":"B","content":"8000元"},{"id":"1e922892adfa4cc291ccc8e08086313f","sort":3,"code":"C","content":"6000元"},{"id":"89b43c6832e344b5bb706ba95c02cbfe","sort":4,"code":"D","content":"4000元"}],"keywords":"null"},{"id":"68724","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》&amp;2526lt;span&amp;2526gt;要求&amp;2526lt;/span&amp;2526gt;，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"defeb3d10031449d86eaf10f6271a331","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具失业登记证&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"942c5d93b45c4065a6f08f5ca50f33c9","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;经办机构认定失业人员失业状态时，应通过内部经办信息系统比对及信息共享来核实，不得要求失业人员出具证明材料。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"fb8dea0023f644d4a13635d66b73287e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时可以凭社会保障卡或身份证件到现场申请&amp;2526lt;/span&amp;2526gt;,也可以网上申请&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"2539e4e3d75540bab9328a219bd8e25b","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;申请失业金时需要出具与单位解除劳动关系的相关证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68721","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《国务院办公厅关于应对新冠肺炎疫情影响&amp;2526lt;/span&amp;2526gt; &amp;2526lt;span&amp;2526gt;强化稳就业举措的实施意见》，对不裁员或少裁员的中小微企业，返还标准最高可提至企业及其职工上年度缴纳失业保险费的（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"589fa50f624f45a8a4aa033d4b702f54","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;90%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"0a552d4343a044648aa59cb70df04f39","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;100%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"3fbcbf1e9757456e93d15e58bd728dac","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;80%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"bc91fbba5ea2464bb9d4f8c29c9b47f1","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;60%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68554","type":"001007","level":"003001","content":"可以保管流动人员人事档案的是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3ffa074212c04e4399dadc3193ae64d4","sort":1,"code":"A","content":"省级公共就业和人才服务机构"},{"id":"a8c6ec098c8e4dcf9fd6ec8f584a052a","sort":2,"code":"B","content":"经人力资源社会保障部门授权的单位"},{"id":"1218cb6efe284f6c8956e734857815fe","sort":3,"code":"C","content":"县级公共就业和人才服务机构"},{"id":"648f6280ed78408a955bb9d932535e11","sort":4,"code":"D","content":"流动人员本人"}],"keywords":"null"},{"id":"68617","type":"001007","level":"003001","content":"关于试用期，错误的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3cb788ca81ac441aaba6a76808cf683e","sort":1,"code":"A","content":"王某进入某事业单位工作，签订为期2年的聘用合用，必须约定12个月试用期"},{"id":"f7ebcd072642428e98e8dc84a6e7d61c","sort":2,"code":"B","content":"约定王某工资为1000元/月，试用期工资为700元/月"},{"id":"cec3dda1073d43faa1d696e0f0621e6f","sort":3,"code":"C","content":"王某与公司续订为期3年的劳动合同，未约定试用期"},{"id":"ce548f3ee1414c2993c3978a00373d9d","sort":4,"code":"D","content":"王某与公司签订2年的劳动合同，约定1个月的试用期"}],"keywords":"null"},{"id":"68551","type":"001007","level":"003001","content":"户口在四川老家的老张和老刘长期在深圳务工，今年工厂倒闭，俩人都失业了，老刘还是残疾人。他俩可在(    )公共就业服务机构办理失业登记，老刘可在(    )申请认定为就业困难人员，享受就业援助。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c663276dfd0b4d2c93e4177521a14071","sort":1,"code":"A","content":"原单位注册地；常住地"},{"id":"5a22297e9c5e42588338374f2db13853","sort":2,"code":"B","content":"出生地；户籍地"},{"id":"583b9bc056c641ffa095ef97015a8380","sort":3,"code":"C","content":"常住地；出生地"},{"id":"20f338c14a3d4169a382d5eda4ef0417","sort":4,"code":"D","content":"常住地；常住地"}],"keywords":"null"},{"id":"68606","type":"001007","level":"003001","content":"关于乡村公益性岗位，正确的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5e088a7beb324ba090cafda91d08b8e9","sort":1,"code":"A","content":"应当为安置人员购买意外伤害商业保险"},{"id":"234c8fe65aee4e9a8a605b7661f29cbe","sort":2,"code":"B","content":"补贴标准根据乡村生活费用确定"},{"id":"0debda5158ba4959ae81084c7d59f009","sort":3,"code":"C","content":"补贴原则上不低于当地城镇公益性岗位补贴水平"},{"id":"2fd776cc724e464e9d4fd529d781815f","sort":4,"code":"D","content":"可以签订劳动合同也可以签订劳务协议"}],"keywords":"null"},{"id":"68591","type":"001007","level":"003001","content":"用人单位与女职工签订的劳动合同，其约定内容违反国家法律规定的是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"741b8f627d864ab3999fe4d9cea6ae87","sort":1,"code":"A","content":"按照公司绩效考核规定，员工不能胜任工作要求时，公司有权解除劳动合同"},{"id":"96175f4056be4936b13f9307e2eb2ae0","sort":2,"code":"B","content":"公司不提倡员工间谈恋爱；若被公司发现，根据规章制度视情况进行处理"},{"id":"3372645120c247f4b83b3120312dbd92","sort":3,"code":"C","content":"员工承诺，在本公司工作期间遵守规章制度"},{"id":"107b86939e514a7f8f50b7d96b2507a1","sort":4,"code":"D","content":"员工自愿承诺，在本公司工作期间不结婚"}],"keywords":"null"},{"id":"68727","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于&amp;2526lt;/span&amp;2526gt;2020年调整退休人员基本养老金的通知》规定，全国总体调整比例按照2019年退休人员月人均基本养老金的（&nbsp;&nbsp;&nbsp; ）确定。各省以全国总体调整比例为（&nbsp;&nbsp;&nbsp; ）确定本省调整比例。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bcbfd8add87943f0ace414c4194d3546","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；高&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"50ffeae5acd74980801e6a5c3b009e43","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；高限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e316209cd95a47bb855a5caaaf9844f5","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%左右；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"e3125d07cd0446a89213ec98e18812ab","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;5%；下限&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68594","type":"001007","level":"003001","content":"外国人在中国就业是指，没有取得(    )的外国人在中国境内依法从事社会劳动并获取劳动报酬的行为。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a6937611ca064abfb27cba90c8064169","sort":1,"code":"A","content":"入境权"},{"id":"21bdbd0d3a3a4760b2aafff86493f39b","sort":2,"code":"B","content":"工作权"},{"id":"809b77556b434574856b00e3ab37dbeb","sort":3,"code":"C","content":"定居权"},{"id":"01c6716d57234e98960251fb42e1d28e","sort":4,"code":"D","content":"民事权"}],"keywords":"null"},{"id":"68555","type":"001007","level":"003001","content":"2017年小李大学毕业后在某民企工作，其人事档案存到了工作单位所在地的公共就业和人才服务机构，后来小李换工作后需将档案转出，此时小李要求存档机构为其补办转正定级手续，面对这种情况，存档机构正确的做法应是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8f5710d5453c488da8a7fa5af56c08e9","sort":1,"code":"A","content":"拒绝小李的要求，直接按商调函将其档案转出"},{"id":"ac67b80e989f45cc910efb3e44b5433c","sort":2,"code":"B","content":"拒绝小李的要求，并为小李讲解相关政策规定"},{"id":"775f2e4b2bd144aaa1f85aa9f91e8a71","sort":3,"code":"C","content":"按照小李的要求为其办理转正定级手续"},{"id":"d65251be089d41c4b34b375a5c4e130c","sort":4,"code":"D","content":"与档案接收机构协商，想办法为小李办理。"}],"keywords":"null"},{"id":"68557","type":"001007","level":"003001","content":"天津的南开大学某应届毕业生应聘到北京某具有人事档案管理权限的国有企业工作，其办理入职手续后，应如何转递档案？(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"623bf52e22c84515b275a537283e7b8e","sort":1,"code":"A","content":"可直接从学校转递到企业"},{"id":"4f6cf14fd2b249109922524a550c021b","sort":2,"code":"B","content":"个人自带"},{"id":"72a63716ed094293b8cc957c118cb13e","sort":3,"code":"C","content":"应当先转至天津市人才公共服务机构，然后在天津市和北京市的人才公共服务机构之间转递"},{"id":"3ae4a91f95a049629966229077ae4831","sort":4,"code":"D","content":"可以弃档不管"}],"keywords":"null"},{"id":"68622","type":"001007","level":"003001","content":"职工因工致残被鉴定为六级伤残的，其劳动关系可按（    ）方式处理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4f9b228b803e481b9aed1047772b5845","sort":1,"code":"A","content":"经工伤职工本人提出，可以与用人单位终止劳动关系"},{"id":"d163139486ec4918bbbf2e5b1ad46667","sort":2,"code":"B","content":"按照本人工资的60%支付伤残津贴"},{"id":"2c3304f118214840a8944ef614188916","sort":3,"code":"C","content":"经工伤职工本人提出，可以与用人单位解除劳动关系，由用人单位支付一次性工伤医疗补助金，由工伤保险基金支付一次性伤残就业补助金"},{"id":"e8f0e160d23f4ba2832ede6da8d24f67","sort":4,"code":"D","content":"经工伤职工本人提出，可以与用人单位解除劳动关系"}],"keywords":"null"},{"id":"68578","type":"001007","level":"003001","content":"职工老赵因工致残被鉴定为五级伤残，其月工资6000元，应享受的一次性伤残补助金为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a6ca3a1308f04903b1367e9ec2acc0ae","sort":1,"code":"A","content":"84000元"},{"id":"93ffc4b79b1a40d0bd15eebcbde9faea","sort":2,"code":"B","content":"60000元"},{"id":"a2a86113c6544b8782b76e05f86bb2b7","sort":3,"code":"C","content":"96000元"},{"id":"40f1494212f24cad92c1714fd7d6edf4","sort":4,"code":"D","content":"108000元"}],"keywords":"null"},{"id":"68619","type":"001007","level":"003001","content":"《领取社会保险待遇资格确认经办规程（暂行）》规定，属于丧失领取养老保险待遇资格的人员包括（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"484dea31f666461bac6a785a1438af2e","sort":1,"code":"A","content":"全民参保登记数据库标识为健在但服刑的人员"},{"id":"10707a5ed75745b89d87077d51a0d5bd","sort":2,"code":"B","content":"国家人口库中标识为死亡、有高铁出行记录的人员"},{"id":"2425ab1a2e5e4efbbb517cb94f9745bb","sort":3,"code":"C","content":"人力资源社会保障服务平台确认及上报的死亡人员"},{"id":"ffe16158fb314d6885bb622fbdf0e9d4","sort":4,"code":"D","content":"家属反映其父母仍然健在的人员"}],"keywords":"null"},{"id":"68573","type":"001007","level":"003001","content":"《关于使用失业保险基金支持脱贫攻坚的通知》规定，深度贫困地区参加失业保险的企业职工申领技能提升补贴，参保年限可以放宽为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"84fdcd3629f2496597b7906039f6acaf","sort":1,"code":"A","content":"累计参保缴费满二年"},{"id":"52efa1d781e343d7bf5f466286ca5b8b","sort":2,"code":"B","content":"累计参保缴费满三年"},{"id":"df3ec29881de4e89a74191f1b922cccb","sort":3,"code":"C","content":"累计参保缴费满一年"},{"id":"f4cead46a20b4e88980b6029095bf3fd","sort":4,"code":"D","content":"不设参保年限"}],"keywords":"null"},{"id":"68588","type":"001007","level":"003001","content":"机关事业单位工作人员可以领取职业年金的情形不包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64019ed1efdb483a987b3ca8019c6afe","sort":1,"code":"A","content":"老赵退休后出国（境）定居，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2cdd00b1b1424d5380f3a6da18b2cf1a","sort":2,"code":"B","content":"老张办理退休手续后，本人选择按月领取职业年金待遇"},{"id":"377c82a0fae341139629ddee8f6a400e","sort":3,"code":"C","content":"老刘未到退休年龄，辞职离开原单位，要求一次性将职业年金个人账户资金支付给本人"},{"id":"2e5bd09d8f1344408d754eda3e6480ed","sort":4,"code":"D","content":"老胡在职期间因病去世，其职业年金个人账户余额可以由其直系亲属继承"}],"keywords":"null"},{"id":"68592","type":"001007","level":"003001","content":"属于行政审批项目的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"64660271849e44af98a09ce7791f55dc","sort":1,"code":"A","content":"劳务派遣经营"},{"id":"a51751a0bd244b29b28eedbe23089ba7","sort":2,"code":"B","content":"民办职业培训机构变更审批"},{"id":"6d0991298d834283ace6da359767410e","sort":3,"code":"C","content":"职业技能考核鉴定机构设立审批"},{"id":"94a8395b864240348475edc5c522c30e","sort":4,"code":"D","content":"标准工时制度"}],"keywords":"null"},{"id":"68599","type":"001007","level":"003001","content":"某农民工首次从事个体经营且自工商登记注册之日起正常运营，其可以享受一次性创业补贴的情形是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"70c4f61f2fd14222bae5a9ff04ad0a28","sort":1,"code":"A","content":"正常运营3个月"},{"id":"faed1327f3e646e5be24adc94103c3d7","sort":2,"code":"B","content":"正常运营5个月"},{"id":"2e9e4430cf074fdb9904fdcd90aa6f23","sort":3,"code":"C","content":"正常运营1个月"},{"id":"35fc4638f35144bc968e525af74b0899","sort":4,"code":"D","content":"正常运营7个月"}],"keywords":"null"},{"id":"68726","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;2020年政府工作报告指出，今年有关目标为：城镇新增就业（&nbsp;&nbsp;&nbsp; ）人以上，城镇调查失业率（&nbsp;&nbsp;&nbsp; ）左右，城镇登记失业率（&nbsp;&nbsp;&nbsp; ）左右。正确的选项是：&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"fd0cd6f2d8714db2a00254d9bfb292a5","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6%；5.5&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"9c5807f503084d8daaec7e16c3fc6772","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6.5%；5.5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"106ca254439f4238a1a51f9b28628025","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;900万；6.5%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"a25ef3d52bf14b9eb77f995697c9c17c","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;1000万；6%；5%&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68610","type":"001007","level":"003001","content":"对当事人提出的仲裁审查申请，仲裁委员会应作出不予受理的情形包括（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f1a18478c3554009833aa2d6993ded3a","sort":1,"code":"A","content":"不属于本仲裁委员会管辖"},{"id":"72bbb3f13b3443eb8b59adc60ee231f5","sort":2,"code":"B","content":"不属于本仲裁委员会管辖"},{"id":"5ea4dfbace3544c6bce8b58c23ae88cb","sort":3,"code":"C","content":"超出规定的仲裁审查申请期间的"},{"id":"adfa6de440ea42a588db9548679b987a","sort":4,"code":"D","content":"不属于仲裁委员会受理争议范围"}],"keywords":"null"},{"id":"68559","type":"001007","level":"003001","content":"技工院校教师副高级职称对应的专业技术岗位(    )级。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c7a835707be24df68a1f4fa24a6c7029","sort":1,"code":"A","content":"五至七"},{"id":"d21929faf68e416eb0cf2dbe8dd0f11f","sort":2,"code":"B","content":"四至六"},{"id":"e39693a21869498da8aa63f62ffaaa91","sort":3,"code":"C","content":"三至五"},{"id":"8fc87ce4be7544959362d8195ee69b27","sort":4,"code":"D","content":"六至八"}],"keywords":"null"},{"id":"68720","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;根据《&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;关于进一步推进失业保险金&amp;2526lt;/span&amp;2526gt;“畅通领、安全办”的通知》，&amp;2526lt;/span&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;符合要求的是（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"57d05cea438c42ceabf4ec28047254c3","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老刘申领失业金时，经办人员通过数据共享发现其之前有&amp;2526lt;/span&amp;2526gt;5年视同缴费缴费年限，并据此向老刘发放了失业金。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"f76d78cdeb2146edbb4e33b519e01b10","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老李是在北京参保的外地户籍人员，申领失业金时，工作人员告诉老李将档案转移至北京后即可领取&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"98c01957a8b24e6fbb6f1718e9868bee","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老赵通过网上办理成功申领了失业金，且人社部门通过手机短信告知其成功领取失业金的情况已同步记录到其档案，以便老赵今后办理相关业务时无需再出具证明&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"38ac1534bac04628b824eee9c740e6ed","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;老张申领失业金，但已超过&amp;2526lt;/span&amp;2526gt;60天申领期限，工作人员告诉老张，超过期限视为放弃当次申领，其未享受的失业金予以封存&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68605","type":"001007","level":"003001","content":"针对疫情防控期间一线医务人员，可采取的保障措施有（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2ed5b1e3f6274b788f56a29c32fca75f","sort":1,"code":"A","content":"根据工作情况，疫情防控一线医务人员可以享受临时性工作补助"},{"id":"1f8e7cd205ae45d293187ad6632855f0","sort":2,"code":"B","content":"医务人员在疫情防控期间的表现，可以作为职称评审医德医风考核的重要内容"},{"id":"dc03bb86c9e04be78edfea1582d66990","sort":3,"code":"C","content":"一次性绩效工资总量应向一线医院及其医护人员、疫情防控人员倾斜"},{"id":"04d281ceb37f4cab8860043e9a36af3e","sort":4,"code":"D","content":"医疗卫生机构可通过简化招聘程序紧急补充疫情防控工作人员"}],"keywords":"null"},{"id":"68604","type":"001007","level":"003001","content":"职称评审委员会评审专家应当具备的条件是（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"81cf1c608d3c4bdc93132ae6628e52ac","sort":1,"code":"A","content":"本职称系列或者专业相应层级的职称"},{"id":"f8ec40175498465794628d3e215aafc9","sort":2,"code":"B","content":"从事本领域专业技术工作"},{"id":"da2f030fb71e4d2da7b4c5b08e522d9f","sort":3,"code":"C","content":"年龄不超过65周"},{"id":"9a5838e7b40042d995e4fe69cb34086a","sort":4,"code":"D","content":"良好的职业道德"}],"keywords":"null"},{"id":"68584","type":"001007","level":"003001","content":"下列职责属于企业年金基金托管人应当履行的是(    )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5f415af62962421ebe130734f5103ae3","sort":1,"code":"A","content":"安全保管企业年金基金财产"},{"id":"3413d86553634b5c958740b3ec761da0","sort":2,"code":"B","content":"制定企业年金基金战略资产配置策略"},{"id":"ad0ac71a0e1b4c2d809febf8fd171a11","sort":3,"code":"C","content":"对所托管的不同企业年金基金财产分别设置账户，确保基金财产的完整和独立"},{"id":"c2cbe48837f643f1b565c3632ec1a301","sort":4,"code":"D","content":"及时办理清算、交割事宜"}],"keywords":"null"},{"id":"68569","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;目前，职工个人企业年金缴费税前扣除比例不超过( &nbsp; &nbsp;)。&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6aef8f55c0bf415c9870efaecde68eff","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6%&amp;2526lt;/p&amp;2526gt;"},{"id":"c344b8652c604917b8df2f26adf68344","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;5%&amp;2526lt;/p&amp;2526gt;"},{"id":"587a45c2df13456797e2ffadaf7b5f0e","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;4%&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;"},{"id":"972f54f556b444cab3ce8cbd122d5b4f","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;8%&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68556","type":"001007","level":"003001","content":"A省人才中心实行了档案接收告知承诺制，其在接收某企业员工小张的档案时，发现缺少核定小张学历学位的材料。该人才中心正确做法是(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bfd6c9e1fa7e406bb2942347175c6f48","sort":1,"code":"A","content":"一次性告知所缺材料及其可能造成的影响后，采取先存后补方式予以接收"},{"id":"cbbf941b0d784fa991ed21d2c952eb10","sort":2,"code":"B","content":"一次性告知所缺材料及其可能造成的影响，经本人作出书面知情说明、承诺补充材料后予以接收"},{"id":"7c3dba49ff6f4b128d475f7192c7fe73","sort":3,"code":"C","content":"与原单位协商退回并补充材料"},{"id":"3927d7aff6fa4c848316890cccf2f613","sort":4,"code":"D","content":"拒绝接收"}],"keywords":"null"},{"id":"68601","type":"001007","level":"003001","content":"劳动者办理失业登记时，各地可采取劳动者书面承诺的方式，在（    ）工作日内办结失业登记，以适当方式主动反馈办理结果。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"713eaa07fb8042eea09409619ff0f619","sort":1,"code":"A","content":"8个"},{"id":"8df6381555cb4de9883763e7239ed809","sort":2,"code":"B","content":"6个"},{"id":"b39b0f251b584b7eaeb5e48093f5c949","sort":3,"code":"C","content":"7个"},{"id":"88f1f34a065f44dea656d7797a9edc11","sort":4,"code":"D","content":"5个"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":6.0,"totalNumbers":3,"description":"判断题，请选择正确或错误","questions":[{"id":"68633","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;生效了的专项集体合同，应当自生效之日起由协商代表及时以适当的方式向本方全体人员公布。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"591f2e658eea491e936cb7ef47084f89","sort":1,"code":"A","content":"错误"},{"id":"590f278ac32a4a979247de53953c62f3","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68626","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;地方各级人民政府和有关部门、公共就业服务机构举办的招聘会，不得向劳动者和用人单位收取费用。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"3721c379c2234614901770842b2364d8","sort":1,"code":"A","content":"错误"},{"id":"e45d789984ba4d87b23af1578f8d6635","sort":2,"code":"B","content":"正确"}],"keywords":"null"},{"id":"68627","type":"001003","level":"003001","content":"&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;对县级以上地方各级人民政府工作部门的具体行政行为不服的，由申请人选择，可以向该部门的本级人民政府申请行政复议，也可以向上一级主管部门申请行政复议。&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"ce4efa5b214748c78c355df38da717a2","sort":1,"code":"A","content":"错误"},{"id":"1be729e13a1945bab354d0faf4c3492c","sort":2,"code":"B","content":"正确"}],"keywords":"null"}]}]},"code":"SUCCESS"}

json_0926 = {"httpStatus":"OK","status":0,"message":"成功","data":{"recordId":"0d248ba08a1d4ffa9774329824daf912","conclusions":"谢谢","description":"&amp;2526lt;p&amp;2526gt;9月份月月比考试&amp;2526lt;/p&amp;2526gt;","name":"9月份月月比考试","totalScore":100.0,"passScore":60.0,"duration":10,"remainingTime":599612,"questionTypeSummaries":[{"type":"001007","score":2.0,"totalScores":90.0,"totalNumbers":45,"description":"null","questions":[{"id":"68876","type":"001007","level":"003001","content":"下列情形中，做法正确的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"296fbbc1032741c383a5ef7a3a01fa97","sort":1,"code":"A","content":"受劳动保障行政部门委托，劳动保障监察支队可以自己名义对用人单位给予行政处罚"},{"id":"e2c4589094564816b7443e73227a5001","sort":2,"code":"B","content":"县人社局处以警告的，由于违法情节轻微，可以不再听取用人单位陈述申辩"},{"id":"ce368c62548144e7be1cbd13905132d8","sort":3,"code":"C","content":"县人社局处以罚款的，应当听取用人单位陈述申辩"},{"id":"73f6fae327de4200b1b8cf659c2fb613","sort":4,"code":"D","content":"《劳动保障监察行政处罚决定书》应当在宣告后当场交付当事人；当事人不在场的，应当在10日内送达当事人"}],"keywords":"null"},{"id":"68859","type":"001007","level":"003001","content":"老王参加工作11年，2019年7月1日从A公司跳槽到B公司。老王在A公司休年休假2天，他在B公司可以休(     )天年休假。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6d334542d7d34407878afa5fd26f6605","sort":1,"code":"A","content":"6"},{"id":"b1438c75bb254796bb2091d65774b451","sort":2,"code":"B","content":"7"},{"id":"70c3c4bcd827478aa29fce28a6e5f9eb","sort":3,"code":"C","content":"8"},{"id":"87bc377b47f04515903170f7671b94ae","sort":4,"code":"D","content":"5"}],"keywords":"null"},{"id":"68871","type":"001007","level":"003001","content":"取得博士学位的海外留学人员可以到国内博士后科研流动站、（   ）做博士后。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b40b1023118c4b1cb9581e953b35a232","sort":1,"code":"A","content":"留学人员创业园"},{"id":"e75f9f41a9934b6988cb95ffc0a44664","sort":2,"code":"B","content":"博士后科研创新站"},{"id":"8645c2252b334ebc8bc8efa479062480","sort":3,"code":"C","content":"博士后科研交流站"},{"id":"40bb931440d34b2ca77c0ed37440d9f1","sort":4,"code":"D","content":"博士后科研工作站"}],"keywords":"null"},{"id":"68858","type":"001007","level":"003001","content":"某企业职工老乔因工致残被鉴定为三级伤残，老乔享受的待遇有（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9be7bb4ec284444c944d384cf6d733da","sort":1,"code":"A","content":"从工伤保险基金按月支付伤残津贴，标准为其工资的80%"},{"id":"4b9258cd0e75476a962788ab5b15813f","sort":2,"code":"B","content":"达到退休年龄并办理退休手续后，停发伤残津贴，按照国家有关规定享受基本养老保险待遇"},{"id":"bfb25f4412ca4e2cb06f9d2d4b019797","sort":3,"code":"C","content":"从工伤保险基金支付一次性伤残补助金，标准为其25个月的工资"},{"id":"f5a5f8efbaac4c7f88fb78450252acfe","sort":4,"code":"D","content":"由用人单位和职工个人以本人工资为基数，缴纳基本医疗保险费"}],"keywords":"null"},{"id":"68825","type":"001007","level":"003001","content":"王某在2014年受了工伤并经鉴定为8级伤残，2016年再次受伤经鉴定为9级伤残，2018年12月王某与单位解除劳动合同，可以享受（    ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b69e499a42c24c48bf85490d78cb4c96","sort":1,"code":"A","content":"一次性伤残补助金，按照8级与9级的差额进行补足"},{"id":"47eba46d3da449fcbc293c99405757e2","sort":2,"code":"B","content":"按照8级工伤享受一次性伤残补助金"},{"id":"7bfbf983623e422b97676d685dba2d27","sort":3,"code":"C","content":"按照9级工伤享受一次性工伤医疗补助金"},{"id":"1017f18943ed4065864a9a70c2c6a00c","sort":4,"code":"D","content":"按照9级工伤享受一次性伤残就业补助金"}],"keywords":"null"},{"id":"68843","type":"001007","level":"003001","content":"关于非全日制用工的说法，正确的是（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"7a6f00c2cbdc47eca8bb80eda97c3892","sort":1,"code":"A","content":"劳动者在同一用人单位每周工作时间累计不超过24小时"},{"id":"3add1116db9a48dea311d0099ec04a52","sort":2,"code":"B","content":"劳动者在同一用人单位一般平均每天工作不超过4小时"},{"id":"89d719823c464b01bbe03193bae3bbdf","sort":3,"code":"C","content":"经劳动者本人同意，用人单位可以与其约定试用期"},{"id":"cbda6146245948faaabe164709cbf675","sort":4,"code":"D","content":"劳动者可与一个或一个以上用人单位订立劳动合同"}],"keywords":"null"},{"id":"68842","type":"001007","level":"003001","content":"某返乡创业企业在当地（       ）的，按规定给予社会保险补贴。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"b743d641e54c4def9126acdc83285ae0","sort":1,"code":"A","content":"招聘了10名就业困难人员"},{"id":"80c09a2b6352458297e91007682da709","sort":2,"code":"B","content":"招聘了5名应届职业培训院校毕业生"},{"id":"f93c9f569472403eb4fcd5e28fe41660","sort":3,"code":"C","content":"招聘了5名复员转业退役军人"},{"id":"53387e6918dc4986be0a74550465d87e","sort":4,"code":"D","content":"招聘了11名农村建档立卡贫困人员"}],"keywords":"null"},{"id":"68835","type":"001007","level":"003001","content":"《企业劳动争议协商调解规定》，调解员聘期可以为(      )年。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e2dfef90c0884f5a8ac8720d71c7e29c","sort":1,"code":"A","content":"1年"},{"id":"cb1d909008014ff98d3851eaabbf65a9","sort":2,"code":"B","content":"2年"},{"id":"9984b788fe834a049af796c1b79fc118","sort":3,"code":"C","content":"3年"},{"id":"058b2f803f7841cf813eb23fe8a665f6","sort":4,"code":"D","content":"4年"}],"keywords":"null"},{"id":"68887","type":"001007","level":"003001","content":"关于企业职工带薪年休假，说法正确的是（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"764e4f96b6704852af0bb3f21af7a31c","sort":1,"code":"A","content":"年休假期间享受与正常工作期间相同的工资收入"},{"id":"0cc099f38ab041b19d39c9fc0a9b4173","sort":2,"code":"B","content":"因工伤停工留薪期间不计入年休假假期"},{"id":"843b30f7528d4fc79b13a93d89743014","sort":3,"code":"C","content":"劳动者连续工作一年以上的，享受带薪休假"},{"id":"1899b4a9ceb540b383b20e8e339f74a3","sort":4,"code":"D","content":"国家法定休假日、休息日不计入年休假的假期"}],"keywords":"null"},{"id":"68882","type":"001007","level":"003001","content":"失业人员失业前所在单位和本人累计缴费时间满1年不足5年的，领取失业保险金的期限最长为（   ）个月；累计缴费时间满5年不足10年的，领取期限最长为（    ）个月。正确的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"2b3f6b7ad5fa434d9995ce62d123187d","sort":1,"code":"A","content":"12；18"},{"id":"06b277af2d8e4a2780135b097cad65a2","sort":2,"code":"B","content":"12；16"},{"id":"9407505c66634d758842464a3756d071","sort":3,"code":"C","content":"14；18"},{"id":"74c27dfb52744936bc44f0564ec4b6b8","sort":4,"code":"D","content":"14；20"}],"keywords":"null"},{"id":"68880","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;张某于2019年5月3日抢险救灾时下落不明，其工资应照发至（ &nbsp; ）&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"127280c3b21947bd83c139ab0afe1525","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;6月3日&amp;2526lt;/p&amp;2526gt;"},{"id":"e61d11d30f114ca2841bb86be8a794ce","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;8月3日&amp;2526lt;/p&amp;2526gt;"},{"id":"b56a349fbef64896b9f3db793695514f","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;7月3日&amp;2526lt;/p&amp;2526gt;"},{"id":"b9e7f32386634d0fb9b452255576da62","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;9月3日&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68837","type":"001007","level":"003001","content":"某企业当年职工工资薪金总额是500万，其职工教育经费税前扣除限额最多可以是（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"459dfc40b3f5452e99d33cf5b4df6943","sort":1,"code":"A","content":"40万"},{"id":"11ff239262924b8da1d20af41d5a85c8","sort":2,"code":"B","content":"48万"},{"id":"dcd8c487aa1941f5a6e719bda6da1174","sort":3,"code":"C","content":"30万"},{"id":"0c0f3a0c854d412fb505b2b75d53b4dc","sort":4,"code":"D","content":"60万"}],"keywords":"null"},{"id":"68881","type":"001007","level":"003001","content":"老王通过伪造病历骗得鉴定结论，领取2万元工伤保险待遇，可对老王处以罚款的金额是(   )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"794ad5829a614c6ab65dc1127389c70c","sort":1,"code":"A","content":"4万"},{"id":"42a15fa9c12f4704be5288f40d8b22e2","sort":2,"code":"B","content":"6万"},{"id":"9f8decdd44f3418a83d8553c7f12ea40","sort":3,"code":"C","content":"2万"},{"id":"65a8e2dfe0054c26974ff59955ce144b","sort":4,"code":"D","content":"8万"}],"keywords":"null"},{"id":"68847","type":"001007","level":"003001","content":"根据《就业促进法》，关于就业援助，表述错误的是（  ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5424280e994b4427a5d200ce234279b1","sort":1,"code":"A","content":"政府投资开发公益性岗位，应当优先安排就业困难人员和城镇低保群体"},{"id":"6e5dd6eab8564eb880c0223b5c8b2e71","sort":2,"code":"B","content":"被安排在公益性岗位工作的，按照国家规定给予岗位补贴，享受低息贷款"},{"id":"c59bceee897246e4a814a803ce236bd2","sort":3,"code":"C","content":"各级人民政府应当采取特别扶助措施，促进残疾人就业"},{"id":"0edadbad4f5a45529ce999408c093756","sort":4,"code":"D","content":"就业困难人员具体范围由省级人力资源社会保障行政部门确定"}],"keywords":"null"},{"id":"68840","type":"001007","level":"003001","content":"用人单位聘用外国人的岗位，必须同时符合（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"258a3c137fdf44fe9dc7c72644c6ed03","sort":1,"code":"A","content":"“高精尖缺”类岗位"},{"id":"76d77f46d19140f69a7dc84d8ee43e3c","sort":2,"code":"B","content":"有特殊需要"},{"id":"4e276585f194463f8462d1a1a2f24e4e","sort":3,"code":"C","content":"国内暂缺适当人选"},{"id":"33129fab2f454ada9e20fd93535a5a28","sort":4,"code":"D","content":"不违反国家有关规定的"}],"keywords":"null"},{"id":"68863","type":"001007","level":"003001","content":"关于工伤保险，表述正确的是（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"1d466911a5eb4415932a3f30a51aaa90","sort":1,"code":"A","content":"职工因工外出期间发生事故下落不明的，从事故发生当月起4个月内照发工资"},{"id":"ec984121aa8a4474be006e12416db0fa","sort":2,"code":"B","content":"五级伤残的，伤残津贴为本人工资的70%"},{"id":"07ee7181f1c54596a0680d60ff5230d1","sort":3,"code":"C","content":"职工再次发生工伤应当享受伤残津贴的，按照较高伤残等级享受伤残津贴待遇"},{"id":"bdccfc505e144ba898f7e53f16591200","sort":4,"code":"D","content":"五级伤残职工伤残津贴金额低于最低工资标准的，由工伤保险基金补足差额"}],"keywords":"null"},{"id":"68827","type":"001007","level":"003001","content":"女职工小张生育了双胞胎，应享受（   ）天产假，其中产前可以休假(    )天。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"556ddd6dc2494c7a98034c8d39556e9a","sort":1,"code":"A","content":"113；15"},{"id":"1f49390fdfb948b8a1d17d4eeed961fa","sort":2,"code":"B","content":"113；10"},{"id":"112fa8d673494116bb311d45816992cf","sort":3,"code":"C","content":"98；10"},{"id":"11e016825b454a0ea98c020e87812fec","sort":4,"code":"D","content":"128；15"}],"keywords":"null"},{"id":"68854","type":"001007","level":"003001","content":"关于专业技术人员资格考试，说法错误的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a6a35df78aa346158685046ae995f7ab","sort":1,"code":"A","content":"串通作弊的，当次全部科目考试成绩无效，并记入诚信档案库5年"},{"id":"ecc443ec330b4dbd822d983d96db1f98","sort":2,"code":"B","content":"行业协会或学会不得作为考试主管部门"},{"id":"592a767f0d29431fbcbfbb6a1b06c5c3","sort":3,"code":"C","content":"将试卷带出考场的，当次该科目考试成绩无效，并记入诚信档案"},{"id":"eb90797b8a254d4fbfc4a8972c07c107","sort":4,"code":"D","content":"作答内容雷同的具体认定方法和标准，由地市级以上考试机构确定"}],"keywords":"null"},{"id":"68883","type":"001007","level":"003001","content":"失业保险基金的来源包括(     )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c3ed11ca84554e67a9f94ab9197005b4","sort":1,"code":"A","content":"失业保险基金的利息"},{"id":"2de06cdca3dd4143b10c02b15391e2cf","sort":2,"code":"B","content":"失业保险费"},{"id":"9f56a96ef9e24530bdef83246bb6f780","sort":3,"code":"C","content":"财政补贴"},{"id":"d8bdec2b927340dcbd3533018a30b4d9","sort":4,"code":"D","content":"基金投资运营收入"}],"keywords":"null"},{"id":"68884","type":"001007","level":"003001","content":"关于参保人员跨统筹范围流动或从机关事业单位流动到企业，说法错误的是（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"0d116c8e06b448a4adbaffc5b419046b","sort":1,"code":"A","content":"个人缴费按本人养老保险个人账户储存额的12%转移"},{"id":"3d27ed246ea0457d9779e314ca5284ec","sort":2,"code":"B","content":"个人缴费和单位缴费部分应当全部转移"},{"id":"25430f9f4d73420cb45fd24e872f530a","sort":3,"code":"C","content":"单位缴费以本人工作年限为基数，按12%的总和转移"},{"id":"f7de8a9200754ff78404c0dc2ada30cf","sort":4,"code":"D","content":"个人缴费和单位缴费部分应暂且不予转移"}],"keywords":"null"},{"id":"68851","type":"001007","level":"003001","content":"关于劳动争议调解仲裁，说法正确的是（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"163b3cf3a2ca46eb85dd03cf9635f001","sort":1,"code":"A","content":"仲裁委应当在受理仲裁申请之日起7日内将仲裁庭组成情况书面通知当事人"},{"id":"884f3506569f452dbfa37ac67cb6a50e","sort":2,"code":"B","content":"仲裁委员会应当设仲裁员名册，并予以公告"},{"id":"c6a5490969be4ec1876827391980db94","sort":3,"code":"C","content":"仲裁庭裁决案件时，其中一部分事实已经清楚的，可以就该部分先行裁决"},{"id":"d240399623d54176a33d130b1be8546f","sort":4,"code":"D","content":"大型企业应当设立调解委员会，并配备专职工作人员"}],"keywords":"null"},{"id":"68834","type":"001007","level":"003001","content":"2019年4月1日，企业因经营不善经济性裁员若干人。2019年(     )前，如企业招用人员，应当同等条件下优先招用被裁减的人员。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"f9c623881f2941a19db6142754d14756","sort":1,"code":"A","content":"10月1日"},{"id":"009fb1aba81143349c11fac015e31035","sort":2,"code":"B","content":"9月1日"},{"id":"d5a971d704e448f78e0f60b6cd07aaca","sort":3,"code":"C","content":"8月1日"},{"id":"21ee026e9a654b41b82ebc412e754a87","sort":4,"code":"D","content":"11月1日"}],"keywords":"null"},{"id":"68829","type":"001007","level":"003001","content":"老王被劳务派遣公司派往A企业工作，但A企业不按照规定发放加班费，老王为主张权利申请劳动仲裁。本案仲裁被申请人应当是(     )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"707fc56671d94624876956640c45b9b0","sort":1,"code":"A","content":"劳务派遣公司"},{"id":"c2c416af591e49e3bc0afca0f18754cd","sort":2,"code":"B","content":"劳务派遣公司和A企业"},{"id":"41804ce96c5742b7bfc041cc0b5b248a","sort":3,"code":"C","content":"A企业"},{"id":"7ff8c33fbfeb457792776600334d716d","sort":4,"code":"D","content":"由老王来选择"}],"keywords":"null"},{"id":"68856","type":"001007","level":"003001","content":"《工伤保险条例》规定的待遇，计发基数相同的是（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a01b1160de5f4147902b0dd1e78d1947","sort":1,"code":"A","content":"一次性工伤医疗补助金"},{"id":"f084d31e41ad4029bf410135693c7203","sort":2,"code":"B","content":"伤残津贴"},{"id":"9478d50dd66142a48bbd3ea32d327e64","sort":3,"code":"C","content":"一次性伤残补助金"},{"id":"686eb1f55da24535812d1ea5f10d70be","sort":4,"code":"D","content":"供养亲属抚恤金"}],"keywords":"null"},{"id":"68841","type":"001007","level":"003001","content":"申请职业培训补贴时，应当提供的材料是（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"99b1954e609547f3a0e8c1a26cca26c2","sort":1,"code":"A","content":"培训合格证书复印件"},{"id":"a42158386b714e3782f8e49bfc96f8fa","sort":2,"code":"B","content":"职业资格证书"},{"id":"b62cfaa1dd524606bab3200a26dfdac4","sort":3,"code":"C","content":"职业技能等级证书"},{"id":"4dae92f5703b443aa3c9c4cbb7889766","sort":4,"code":"D","content":"专项职业能力证书复印件"}],"keywords":"null"},{"id":"68861","type":"001007","level":"003001","content":"小刘参加某市事业单位公开招聘考试，在某科目考试中在答题卡规定以外位置标注了本人名字被监考人员发现。根据《事业单位公开招聘违纪违规行为处理规定》规定，应对小刘处以（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"d6c2ac0d72ca48f8a823a51f23faa930","sort":1,"code":"A","content":"给予其当次全部科目考试成绩无效的处理，并将其违纪违规行为记入事业单位公开招聘应聘人员诚信档案库，长期记录"},{"id":"539b8fef68e047eb94d9a603f3309385","sort":2,"code":"B","content":"给予其当次该科目考试成绩无效"},{"id":"3a3853bbbdef4da6b03d49576783d49a","sort":3,"code":"C","content":"给予其当次该科目考试成绩无效的处理，并将其违纪违规行为记入事业单位公开招聘应聘人员诚信档案库，记录期限为五年"},{"id":"2cde27cb684c40a4b2c3b9df760174fd","sort":4,"code":"D","content":"给予其当次全部科目考试成绩无效"}],"keywords":"null"},{"id":"68831","type":"001007","level":"003001","content":"关于被征地农民政策，说法错误的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"83a47030e9e44af48d59bd8b4a5ec53c","sort":1,"code":"A","content":"征收农村集体所有的土地，应当按一定比例安排被征地农民的社会保险费"},{"id":"107b46e72e10436e915e125af2201106","sort":2,"code":"B","content":"按照国务院规定将被征地农民纳入社会保险制度"},{"id":"28e2a90629074a38a2fa43bd6db004c4","sort":3,"code":"C","content":"人社部门要以新被征地农民为重点人群，做好就业培训和社会保障工作"},{"id":"d4bdce0a26c648b98edfe862d71e300f","sort":4,"code":"D","content":"社会保障费用不落实的不得批准征地"}],"keywords":"null"},{"id":"68888","type":"001007","level":"003001","content":"劳动者可以随时解除劳动合同的法定情形是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"8930f77ac8b342ff9eda05d4f5771953","sort":1,"code":"A","content":"用人单位变更名称、法定代表人、主要负责人"},{"id":"68adabe3fd114a68bce0b9b4d98fdf0d","sort":2,"code":"B","content":"用人单位未依法为劳动者缴纳社会保险费"},{"id":"7538bc27612244e99d274fef3cba4f02","sort":3,"code":"C","content":"用人单位发生合并或者分立"},{"id":"39fbd50a61754942ab2247b7452275c7","sort":4,"code":"D","content":"用人单位变更投资人"}],"keywords":"null"},{"id":"68828","type":"001007","level":"003001","content":"李某（17岁）是甲公司招用的职工，双方订立了书面劳动合同。在试用期内，李某为发泄对公司的不满，在公司生产的饮料中放入了污物。下列观点正确的是(     )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"45e8528442cc42938a036a7497eecbad","sort":1,"code":"A","content":"李某与公司之间订立的劳动合同有效"},{"id":"4a68292b6d9145168a5e2cb0822f24fa","sort":2,"code":"B","content":"甲公司可以解除与李某的劳动合同"},{"id":"dfaebf59edb3401d8042213af48fb9ed","sort":3,"code":"C","content":"李某与甲公司之间订立的劳动合同是可撤销的合同"},{"id":"a0fea8a768864ca8a76d9f06aa254050","sort":4,"code":"D","content":"在试用期内，公司不能解除与李某的劳动合同"}],"keywords":"null"},{"id":"68869","type":"001007","level":"003001","content":"参加基本养老保险的个人因病或非因工死亡的，其遗属可以领取的待遇项目有(     )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4ce2ccafced74760afb8f0006a5e2ae7","sort":1,"code":"A","content":"丧葬补助金"},{"id":"063e7a671fe04c6f91cc89158f8869ef","sort":2,"code":"B","content":"一次性生活补助"},{"id":"6bd40c67d29d48bfbb7d6091f64a7ab1","sort":3,"code":"C","content":"因病特殊补助"},{"id":"e2ee747e637943fe88cd521ed30c20ec","sort":4,"code":"D","content":"非因工死亡医疗补助"}],"keywords":"null"},{"id":"68848","type":"001007","level":"003001","content":"根据《国务院关于高级专家离休退休若干问题的暂行规定》，经批准，教授最多可以延长离退年龄至（   ）周岁，副教授最多可以延长至（   ）周岁。符合规定的是：","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bfff89f2cf7b45d592361a5cbc966c7e","sort":1,"code":"A","content":"75；70"},{"id":"11d55982c6554cd9901e71c6a221ef52","sort":2,"code":"B","content":"70；65"},{"id":"2cff03309a7147438b2c95219941c91b","sort":3,"code":"C","content":"75；65"},{"id":"734bf757b78f4ff1bb696a2b4e9dee4c","sort":4,"code":"D","content":"70；70"}],"keywords":"null"},{"id":"68830","type":"001007","level":"003001","content":"档案转递时，以下不属于接收审核流动人员人事档案必备材料的是（   ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"37358b8cbaf04d58922b1bc44b3d4362","sort":1,"code":"A","content":"转正定级表"},{"id":"4fbf699d3a2c406ba3bd5829b0adcf2b","sort":2,"code":"B","content":"商调函件"},{"id":"4dff2e674be1469890a16a1b0f787cbe","sort":3,"code":"C","content":"行政（工资）介绍信"},{"id":"02a16cc342b2469abab0226c55bf8d13","sort":4,"code":"D","content":"调整改派手续"}],"keywords":"null"},{"id":"68868","type":"001007","level":"003001","content":"关于经济补偿金的说法，正确的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bba822519c9e441eb50a12a3c1e8d018","sort":1,"code":"A","content":"经济补偿按劳动者累计工作年限，每满1年支付一个月工资的标准支付"},{"id":"d15b773737d34d029772ad3ddd114332","sort":2,"code":"B","content":"经济补偿金的月工资标准，按照劳动者在劳动合同解除或者终止前上个月工资计算"},{"id":"d4c873cffe674546a1f73e77d070d056","sort":3,"code":"C","content":"用人单位违法解除劳动合同，同时支付经济补偿金和赔偿金"},{"id":"f3f36250503a40a69e98edbc4d4603f3","sort":4,"code":"D","content":"追索经济补偿金额不超过当地月最低工资标准12个月的，适用劳动争议仲裁终局裁决"}],"keywords":"null"},{"id":"68852","type":"001007","level":"003001","content":"以项目或标段为单位参加工伤保险时，对人工成本占比较低的工程建设项目，可按照人工成本乘以(     )的方式计算工伤保险费。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"37718e56b0da47258f2fc40be2f25e38","sort":1,"code":"A","content":"工伤保险行业最高费率"},{"id":"da21f3c3e8774192b533d2a73ab60667","sort":2,"code":"B","content":"工伤保险行业最低费率"},{"id":"d15e5505786348f38d625d9efdeb7d0a","sort":3,"code":"C","content":"工伤保险行业基准费率"},{"id":"1131e777182c43be8e5b01462b7fbafc","sort":4,"code":"D","content":"工伤保险行业平均费率"}],"keywords":"null"},{"id":"68873","type":"001007","level":"003001","content":"按照劳动合同法规定，企业裁减人员，应当优先留用的人员包括（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"7a789dbb3a934c49903352c6af8aa71f","sort":1,"code":"A","content":"与本单位订立较长期限的固定期限劳动合同的"},{"id":"d781e75926c6448a808026a0f8469969","sort":2,"code":"B","content":"与本单位订立无固定期限劳动合同的"},{"id":"979abc0c7fcd4082956411f9230cf673","sort":3,"code":"C","content":"知晓企业商业秘密的"},{"id":"b0dc196ed74849859c0d390c36b6196b","sort":4,"code":"D","content":"被裁减人员家庭中还有1人就业，但有2个孩子需要扶养"}],"keywords":"null"},{"id":"68889","type":"001007","level":"003001","content":"根据《工资集体协商试行办法》，劳动保障行政部门应在收到工资协议（   ）日内，对工资集体协商双方代表资格、（   ）和签订程序等进行审查。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"bc328f8d0ab34c93875320c9308618fc","sort":1,"code":"A","content":"10；具体证明材料"},{"id":"36f062b1ccf84bcab9527da44fea9897","sort":2,"code":"B","content":"10；工资协议的条款内容"},{"id":"459987bd425b4f6eaac61a7430cd4b9e","sort":3,"code":"C","content":"15；工资协议的条款内容"},{"id":"5d9a817c8b1041fa94d97914d3807740","sort":4,"code":"D","content":"15；具体证明材料"}],"keywords":"null"},{"id":"68839","type":"001007","level":"003001","content":"公司为张某提供专项培训费用10万元并进行了专业技术培训，约定服务期5年。下列做法正确的是（    ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"c056948ba3b94be1b0ae5298b5fbb3f4","sort":1,"code":"A","content":"张某服务满3年时辞职，公司可以要求支付违约金4万元"},{"id":"c25059762fe24432a0fd3ce735f90304","sort":2,"code":"B","content":"可以约定违约金15万元"},{"id":"c633f7c085334e88a67d30bbe8010ea0","sort":3,"code":"C","content":"公司可以要求张某参加培训获得的资格证书必须由其保管2年"},{"id":"a007e5e6106943d7892944ef3fa51ee1","sort":4,"code":"D","content":"张某服务满1年时辞职，公司要求支付违约金10万元"}],"keywords":"null"},{"id":"68826","type":"001007","level":"003001","content":"&amp;2526lt;p&amp;2526gt;关于职称评审，说法错误的是（ &nbsp;）&amp;2526lt;/p&amp;2526gt;","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4ad1b718b982423eab179779d0322a6b","sort":1,"code":"A","content":"&amp;2526lt;p&amp;2526gt;对不具备评审能力的单位，可组建社会化评审机构进行职称评审&amp;2526lt;/p&amp;2526gt;"},{"id":"8089f9554f844e7c8a1bf6ebf33e4ce5","sort":2,"code":"B","content":"&amp;2526lt;p&amp;2526gt;建立以同行专家评审为基础的业内评价机制，注重引入市场评价和社会评价&amp;2526lt;/p&amp;2526gt;"},{"id":"73ea1e5d7f3d4ce5b43d3243cd9439f1","sort":3,"code":"C","content":"&amp;2526lt;p&amp;2526gt;申报评审正高级职称的人员，一般应具有研究生及以上学历&amp;2526lt;/p&amp;2526gt;"},{"id":"2f3211d40692424dba0c06fcd6b53c42","sort":4,"code":"D","content":"&amp;2526lt;p&amp;2526gt;申报评审正高级职称的人员，需在副高级岗位上从事相关工作3年及以上&amp;2526lt;/p&amp;2526gt;"}],"keywords":"null"},{"id":"68864","type":"001007","level":"003001","content":"关于工资支付，下列说法正确的是（   ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5549aa9e862a4fb38c044f8ef907d3c2","sort":1,"code":"A","content":"根据法院判决，用人单位可以从个人工资中代扣抚养费、赡养费"},{"id":"7d7599daa9e64c81a0be3c7a8f88b0a4","sort":2,"code":"B","content":"因劳动者请事假等相应减发工资不属于违法克扣劳动者工资"},{"id":"b6de9252469a48899cb83f17b9c18c1b","sort":3,"code":"C","content":"劳动者依法享受婚假的，用人单位应按照劳动合同规定的标准支付劳动者工资"},{"id":"bd69d3f9b0234c60bc4c0a3f462a6955","sort":4,"code":"D","content":"劳动者依法享受探亲假的，用人单位应按劳动合同规定的标准支付劳动者工资"}],"keywords":"null"},{"id":"68844","type":"001007","level":"003001","content":"《国务院关于机关事业单位工作人员养老保险制度改革的决定》规定，本决定实施后参加工作、个人缴费年限满足规定的人员，退休后按月发给基本养老金。基本养老金由(     )组成。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"19c75ec19dae459bb52ef0541ffc2c5d","sort":1,"code":"A","content":"基础养老金和个人账户养老金"},{"id":"fcd67e2b1a7b43d78be7db3579e39ed3","sort":2,"code":"B","content":"基础养老金、个人账户养老金、过渡性养老金和职业年金"},{"id":"01f8eda2770b4d1d905bb85debd3e8cb","sort":3,"code":"C","content":"基础养老金、个人账户养老金和职业年金"},{"id":"aea7aad47609443a932d24d5ed0f65f7","sort":4,"code":"D","content":"基础养老金、个人账户养老金和过渡性养老金"}],"keywords":"null"},{"id":"68838","type":"001007","level":"003001","content":"关于最低工资，下列说法正确的是（     ）","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"a65dc2fec5764f5cab0026ffa1e43816","sort":1,"code":"A","content":"各地最低工资的确定主要取决于本地区城乡居民消费价格指数、平均工资、就业状况等因素"},{"id":"2fcdcd2105474543aac3ea1ba192cc67","sort":2,"code":"B","content":"剔除加班加点工资及特殊工作环境下的津贴后的工资可以低于当地最低工资标准。"},{"id":"794bf56f626841769b4ef12413b2c059","sort":3,"code":"C","content":"最低工资标准每三年至少调一次。"},{"id":"3a58984bc5e5418481b0621f814b497a","sort":4,"code":"D","content":"劳动者提供了正常劳动的，用人单位支付的工资不得低于当地最低工资标准"}],"keywords":"null"},{"id":"68862","type":"001007","level":"003001","content":"行政复议机关收到行政复议申请后，应当在(     )日内进行审查，决定是否受理。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"7e62937b46304fd2bef56d58b2a434f2","sort":1,"code":"A","content":"10"},{"id":"04d13433c116414aa6e645d71c4a95ff","sort":2,"code":"B","content":"5"},{"id":"538123fa9721498a8a25d5cebab1941f","sort":3,"code":"C","content":"7"},{"id":"22c977a3bd8d486ba5340b8259fb0d27","sort":4,"code":"D","content":"15"}],"keywords":"null"},{"id":"68865","type":"001007","level":"003001","content":"关于企业年金基金财产投资范围，正确的是（     ）。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"e161d16b87194a15b48c45bdd4ee9044","sort":1,"code":"A","content":"只能投资境内产品"},{"id":"a363504006aa4a4ba734575551b18439","sort":2,"code":"B","content":"可以投资国债、中央银行票据"},{"id":"7429a8b5523148c2ad97a5eab38c9897","sort":3,"code":"C","content":"鉴于近几年万能保险产品投资风险加大，基金不再投资该品种"},{"id":"4e0eefb211cc4a8e8efb13de7c9923d7","sort":4,"code":"D","content":"只能投资银行类股票"}],"keywords":"null"},{"id":"68855","type":"001007","level":"003001","content":"老王因工致残被鉴定为三级伤残，其每月工资为3000元。老王的一次性伤残补助金的标准为(    )。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"badbe584e4eb47c2bdd398533e64116e","sort":1,"code":"A","content":"48000元"},{"id":"b2a100a3a7f44288b029e5dad95b206b","sort":2,"code":"B","content":"36000元"},{"id":"9a3420daba1947748ba00648ad8d4300","sort":3,"code":"C","content":"30000元"},{"id":"d891007802564bdf9b3abc4574fd9fa5","sort":4,"code":"D","content":"63000元"}],"keywords":"null"},{"id":"68833","type":"001007","level":"003001","content":"根据《事业单位工作人员考核暂行规定》规定，表述正确的是(     )","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"6973013c871241dd80eccd2448837fdf","sort":1,"code":"A","content":"年度考核被确定为优秀等次的人数，一般掌握在本单位工作人员总人数的10%，最多不超过15%"},{"id":"4f3301afcbf44970980abc732f91d99f","sort":2,"code":"B","content":"考核结果要以书面形式通知被考核人，考核结果存入本人档案"},{"id":"06ff56e76f124763a8b0c93b19604954","sort":3,"code":"C","content":"考核委员会或考核小组一般由本单位负责人、人事机构和有关部门负责人及工作人员代表组成"},{"id":"2af88bb4c0d547feb9ae21070aa70d91","sort":4,"code":"D","content":"当年考核被确定为不合格等次的，不发年终奖金"}],"keywords":"null"}]},{"type":"001003","score":2.0,"totalScores":10.0,"totalNumbers":5,"description":"null","questions":[{"id":"68902","type":"001003","level":"003001","content":"用人单位违反规定拒不协助社会保险行政部门对工伤事故进行调查核实的，社会保险行政部门责令改正，并处一定数额的罚款。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"5ce3a069bcfd4f0590b967ff463ebdea","sort":1,"code":"A","content":"正确"},{"id":"e0e920706ebb4c5db5c9c07538ded01e","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68900","type":"001003","level":"003001","content":"城乡居民养老保险个人账户养老金的月计发标准，为个人缴费和政府补贴额除以139。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"4c7a16c6572b40a09ec5b69ac24c3231","sort":1,"code":"A","content":"正确"},{"id":"77cfd2a75e5343c8a9fd5136d0637b70","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68898","type":"001003","level":"003001","content":"2020年度调整退休人员基本养老金时，全国总体调整比例按照2019年退休人员月人均基本养老金的6%确定。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"16fe6d278514403c93bfe2f1606c88fd","sort":1,"code":"A","content":"正确"},{"id":"b6d1a819874944eaadcf98e1becdabd4","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68896","type":"001003","level":"003001","content":"集体合同由工会代表企业职工一方与用人单位订立，尚未建立工会的，由上级工会指导劳动者推举的代表与用人单位订立。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"9c4fe82806cb4b7d9ccbbdcecbbcdbd7","sort":1,"code":"A","content":"正确"},{"id":"508905bf3e7d4c379ca396645c8e2311","sort":2,"code":"B","content":"错误"}],"keywords":"null"},{"id":"68904","type":"001003","level":"003001","content":"用人单位未按规定申报应当缴纳的社保费数额的，按照该单位上月缴费额的120%确定应当缴纳数额。","answer":"null","analysis":"null","score":2.0,"userAnswer":"null","blanksNumber":"null","signed":0,"checkResult":"null","userScore":"null","tag":"008001","chapterName":"null","inCollection":0,"choices":[{"id":"aa6500237724450da8eafbeb5bced2bd","sort":1,"code":"A","content":"正确"},{"id":"4f61967861de498b87e15289118a85b7","sort":2,"code":"B","content":"错误"}],"keywords":"null"}]}]},"code":"SUCCESS"}


# 根据获取题目文本（不含答案）
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
        # print(res)
        print(id + ':' + content)
        print('A、' + optionA)
        print('B、' + optionB)
        print('C、' + optionC)
        print('D、' + optionD)
        print('答案：' + answer)

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
        # print(res)
        print(id + ':' + content)
        print('A、' + optionA)
        print('B、' + optionB)
        print('答案：' + answer)


# 根据获取题目文本（含答案）
def get_answer(jsons):
    json_str = json.loads(json.dumps(jsons, ensure_ascii=False))
    hunhe = json_str['data']

    for q in hunhe:
        id = get_new(q['id'])
        content = get_new(q['content'])
        optionA = get_new(q['choices'][0]['content'])
        optionB = get_new(q['choices'][1]['content'])
        if len(q['choices']) == 4:
          optionC = get_new(q['choices'][2]['content'])
          optionD = get_new(q['choices'][3]['content'])
        else:
          optionC = ""
          optionD = ""
        answer = get_new(q['answer'])
        analysis = ""
        optionE = ""
        chapterId = "0000"
        questionType = "001007"
        res = "{\"_id\":\"" + id + "\",\"content\":\"" + content + "\",\"answer\":\"" + answer + "\",\"analysis\":\"" + analysis + "\",\"optionA\":\"" + optionA + "\",\"optionB\":\"" + optionB + "\",\"optionC\":\"" + optionC + "\",\"optionD\":\"" + optionD + "\",\"optionE\":\"" + optionE + "\",\"chapterId\":\"" + chapterId + "\",\"questionType\":\"" + questionType + "\"}"
        # print(res)
        print(id + ':' + content)
        print('A、' + optionA)
        print('B、' + optionB)
        print('C、' + optionC)
        print('D、' + optionD)
        print('答案：' + answer)


get_text(json_0926)
# get_answer(json_0926)

