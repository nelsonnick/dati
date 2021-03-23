#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import datetime
from dateutil.relativedelta import relativedelta

# 计发月数
monthsNum = {
    40: 233,
    41: 230,
    42: 226,
    43: 223,
    44: 220,
    45: 216,
    46: 212,
    47: 208,
    48: 204,
    49: 199,
    50: 195,
    51: 190,
    52: 185,
    53: 180,
    54: 175,
    55: 170,
    56: 164,
    57: 158,
    58: 152,
    59: 145,
    60: 139,
    61: 132,
    62: 125,
    63: 117,
    64: 109,
    65: 101,
    66: 93,
    67: 84,
    68: 75,
    69: 65,
    70: 56,
}


# 获取个人账户金、获取企业缴费中个人要缴费的金额
# base_num：缴费基数
def getPrivateAccount(base_num):
    return base_num * 0.08


# 获取个人账户金总额
# base_num：缴费基数
# pay_month：缴费月数
def getPrivateAccount(base_num, pay_month):
    return base_num * 0.08 * pay_month


# 获取灵活就业实际缴费金额
# base_num：缴费基数
def getRealPayOfLingHuo(base_num):
    return base_num * 0.2


# 获取基础养老金
# up_average_wage：上年度社平工资
# index_num：缴费指数
# pay_month：缴费月数
def getBasicPension(up_average_wage, index_num, pay_month):
    return float('%.2f' % (up_average_wage * (1 + index_num) / 2 * pay_month / 12 * 0.01))


# 获取个人账户养老金
# private_account：个人账户总额
# retire_age：退休年龄
def getPrivateAccountPension(private_account, retire_age):
    return float('%.2f' % (private_account / monthsNum[retire_age]))


# 获取月养老金
# up_average_wage：上年度社平工资
# index_num：缴费指数
# pay_month：缴费月数
# private_account：个人账户
# retire_age：退休年龄
def getPenion(up_average_wage, index_num, pay_month, private_account, retire_age):
    return float('%.2f' % (up_average_wage * (1 + index_num) / 2 * pay_month / 12 * 0.01 + private_account / monthsNum[
        retire_age]))


# 获取定投复利计算金额
# investment：定投金额
# rate：利率
# times：次数
def getInvestmentByTimes(investment, rate, times):
    total = 0
    t = 0
    while t < times:
        total += investment * (1 + rate) ** (times - t)
        t += 1
    return total


# 获取复利
# up_average_wage：上年度社平工资
# index_num：缴费指数
# rate：年化利率
# pay_month：缴费月数
def getInvestment(up_average_wage, index_num, pay_month, rate):
    return float('%.2f' % (getInvestmentByTimes(up_average_wage * index_num * 0.2, rate/12, pay_month)))


# 获取月养老金--社平工资为固定值
# up_average_wage：上年度社平工资
# index_num：缴费指数
# pay_month：缴费月数
# retire_age：退休年龄
def getPenion(up_average_wage, index_num, pay_month, retire_age):
    return float('%.2f' % (
            up_average_wage * (1 + index_num) / 2 * pay_month / 12 * 0.01 + up_average_wage * 0.08 * pay_month /
            monthsNum[retire_age]))


# 缴费指数从0.6增长到3
def indexInc(up_average_wage, pay_month, retire_age, rate):
    print('缴费基数\t月缴费额\t缴费月数\t缴费总额\t退休工资\t到期存款')
    for i in range(600, 3001, 100):
        print(str(i / 1000) + '\t' + str(up_average_wage * i / 1000 * 0.2) + '\t' + str(pay_month) + '\t' +
              str(up_average_wage * i / 1000 * 0.2 * pay_month) + '\t' +
              str(getPenion(up_average_wage, i / 1000, pay_month, retire_age))+'\t'+
              str(getInvestment(up_average_wage, i / 1000, pay_month, rate)))


# 缴费月数从180月开始增加
def monthInc(index_num, up_average_wage, pay_month, retire_age, rate):
    print('缴费基数\t月缴费额\t缴费月数\t缴费总额\t退休工资\t到期存款')
    for i in range(180, pay_month + 1, 1):
        print(str(index_num) + '\t' + str(up_average_wage * index_num * 0.2) + '\t' + str(i) + '\t' +
              str(up_average_wage * index_num * 0.2 * i) + '\t' +
              str(getPenion(up_average_wage, index_num, i, retire_age)) + '\t' +
              str(getInvestment(up_average_wage, index_num, i, rate)))


indexInc(5000, 180, 60, 0.0325)
# monthInc(0.6, 5000, 190, 60, 0.0325)
