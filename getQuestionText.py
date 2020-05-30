#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json


def get_new(str):
    return str.replace("2526gt;", "").replace("2526lt;", "")\
        .replace("&amp;", "").replace("/span", "").replace("span", "")\
        .replace("&nbsp;", "").replace("/p", "").replace("p", "").replace(" ", "")


test_dict = {
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
json_str = json.loads(json.dumps(test_dict, ensure_ascii=False))
duoxuans = json_str['data']['questionTypeSummaries'][0]['questions']
panduans = json_str['data']['questionTypeSummaries'][1]['questions']

for q in duoxuans:
    id = get_new(q['id'])
    content = get_new(q['content'])
    answerA = get_new(q['choices'][0]['content'])
    answerB = get_new(q['choices'][1]['content'])
    answerC = get_new(q['choices'][2]['content'])
    answerD = get_new(q['choices'][3]['content'])
    print("问题-" + id + "：" + content)
    print("A、" + answerA)
    print("B、" + answerB)
    print("C、" + answerC)
    print("D、" + answerD)
    print("")

for q in panduans:
    id = get_new(q['id'])
    content = get_new(q['content'])
    answerA = get_new(q['choices'][0]['content'])
    answerB = get_new(q['choices'][1]['content'])
    print("问题-" + id + "：" + content)
    print("A、" + answerA)
    print("B、" + answerB)
    print("")