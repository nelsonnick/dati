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

# 济南市社平工资
averageWage = {
    1995: 488,
    1996: 586,
    1997: 658,
    1998: 667,
    1999: 676,
    2000: 733,
    2001: 820,
    2002: 978,
    2003: 1080,
    2004: 1255,
    2005: 1377,
    2006: 1586,
    2007: 1898,
    2008: 2194,
    2009: 2491,
    2010: 2592,
    2011: 2953,
    2012: 3349,
    2013: 3873,
    2014: 4376,
    2015: 4882,
    2016: 5333,
    2017: 5850,
    2018: 5448
}

# 缴费上限
topLimit = {
    1995: 1463,
    1996: 1758,
    1997: 1974,
    1998: 2003,
    1999: 2024,
    2000: 2197,
    2001: 2460,
    2002: 2934,
    2003: 3240,
    2004: 3765,
    2005: 4131,
    2006: 4758,
    2007: 5694,
    2008: 6582,
    2009: 7374,
    2010: 7776,
    2011: 8859,
    2012: 10447,
    2013: 11619,
    2014: 13128,
    2015: 14646,
    2016: 15999,
    2017: 17550,
    2018: 16346,
}

# 缴费下限
bottomLimit = {
    1995: 293,
    1996: 352,
    1997: 395,
    1998: 401,
    1999: 406,
    2000: 440,
    2001: 492,
    2002: 587,
    2003: 648,
    2004: 753,
    2005: 827,
    2006: 952,
    2007: 1139,
    2008: 1317,
    2009: 1495,
    2010: 1556,
    2011: 1772,
    2012: 2010,
    2013: 2324,
    2014: 2626,
    2015: 2930,
    2016: 3200,
    2017: 3510,
    2018: 3269,
}


# 根据缴费基数获取个人账户金
def getPrivateAccount(base_num):
    return base_num * 0.08


# 根据缴费基数获取实际缴费金额
def getRealPay(base_num):
    return base_num * 0.2


# 根据社平工资和缴费指数获取缴费基数
def getBaseNum(average_wage, index_num):
    return math.ceil(average_wage * index_num)


# 根据缴费年月返回社平工资
def getAverageWage(year_month):
    if 199603 < year_month < 199704:
        return averageWage[1995]
    elif 199703 < year_month < 199804:
        return averageWage[1996]
    elif 199803 < year_month < 199904:
        return averageWage[1997]
    elif 199903 < year_month < 200004:
        return averageWage[1998]
    elif 200003 < year_month < 200104:
        return averageWage[1999]
    elif 200103 < year_month < 200204:
        return averageWage[2000]
    elif 200203 < year_month < 200304:
        return averageWage[2001]
    elif 200303 < year_month < 200404:
        return averageWage[2002]
    elif 200403 < year_month < 200504:
        return averageWage[2003]
    elif 200503 < year_month < 200604:
        return averageWage[2004]
    elif 200603 < year_month < 200704:
        return averageWage[2005]
    elif 200703 < year_month < 200804:
        return averageWage[2006]
    elif 200803 < year_month < 200904:
        return averageWage[2007]
    elif 200903 < year_month < 201004:
        return averageWage[2008]
    elif 201003 < year_month < 201104:
        return averageWage[2009]
    elif 201103 < year_month < 201204:
        return averageWage[2010]
    elif 201203 < year_month < 201304:
        return averageWage[2011]
    elif 201303 < year_month < 201407:
        return averageWage[2012]
    elif 201406 < year_month < 201507:
        return averageWage[2013]
    elif 201506 < year_month < 201607:
        return averageWage[2014]
    elif 201606 < year_month < 201707:
        return averageWage[2015]
    elif 201706 < year_month < 201807:
        return averageWage[2016]
    elif 201806 < year_month < 201907:
        return averageWage[2017]
    elif 201806 < year_month < 202007:
        return averageWage[2018]
    else:
        return 0


# 根据上年度社平工资、缴费指数、缴费月数计算基础养老金
def getBasicPension(up_average_wage, index_num, pay_month):
    return float('%.2f' % (up_average_wage*(1+index_num)/2*pay_month/12*0.01))


# 根据个人账户、退休年龄计算个人账户养老金
def getPrivateAccountPension(private_account, age):
    return float('%.2f' % (private_account/monthsNum[age]))


# 根据开始年月、终止年月、缴费基数获取缴费基数总和
def getBaseNumTotal(start_year_month, end_year_month, index_num):
    start = datetime.datetime.strptime(str(start_year_month), '%Y%m')
    end = datetime.datetime.strptime(str(end_year_month), '%Y%m')
    baseNumTotal = 0
    while start <= end:
        baseNumTotal = baseNumTotal + getBaseNum(getAverageWage(int(start.strftime('%Y%m'))), index_num)
        start += relativedelta(months=+1)
    return baseNumTotal


# 根据开始年月、终止年月获取缴费月数
def getMonthTotal(start_year_month, end_year_month):
    start = datetime.datetime.strptime(str(start_year_month), '%Y%m')
    end = datetime.datetime.strptime(str(end_year_month), '%Y%m')
    monthTotal = 0
    while start <= end:
        monthTotal = monthTotal + 1
        start += relativedelta(months=+1)
    return monthTotal


# 根据上年度社平工资、缴费指数、缴费月数、个人账户、退休年龄计算月养老金
def getPenion(up_average_wage, index_num, pay_month, private_account, retire_age):
    return float('%.2f' % (up_average_wage*(1+index_num)/2*pay_month/12*0.01 + private_account/monthsNum[retire_age]))


# 拿回本金所需年限
def getMoneyYear(up_average_wage, index_num, pay_month, private_account, retire_age):
    penion = getPenion(up_average_wage, index_num, pay_month, private_account, retire_age)
    return float('%.2f' % (private_account/2*5/penion/12))


age = [50, 55, 60]
indexNum = 3
startYeaMonth = 200401
endYearMonth = 201812
upAverageWage = 5448
# realPay = getRealPay(getBaseNumTotal(startYeaMonth, endYearMonth, indexNum))
# privateAccount = getPrivateAccount(getBaseNumTotal(startYeaMonth, endYearMonth, indexNum))
# monthTotal = getMonthTotal(startYeaMonth, endYearMonth)


# for a in age:
#     print(getPenion(upAverageWage, indexNum, monthTotal, privateAccount, a))

# 缴费指数从0.6增长到3
def indexInc(start_year_month, end_year_month):
    for i in range(600, 3001, 1):
        privateAccount = getPrivateAccount(getBaseNumTotal(start_year_month, end_year_month, i/1000))
        monthTotal = getMonthTotal(start_year_month, end_year_month)
        print(getPenion(upAverageWage, i/1000, monthTotal, privateAccount, 50))


# 缴费指数固定，缴费时间从180月增加到191月
def monthInc(index_num):
    privateAccount = getPrivateAccount(getBaseNumTotal(200401, 201812, index_num))
    monthTotal = getMonthTotal(200401, 201812)
    print(getPenion(upAverageWage, index_num, monthTotal, privateAccount, 50))
    for e in range(201901, 201911, 1):
        privateAccount = getPrivateAccount(getBaseNumTotal(200401, e, index_num))
        monthTotal = getMonthTotal(200401, e)
        print(getPenion(upAverageWage, index_num, monthTotal, privateAccount, 50))


privateAccount = getPrivateAccount(getBaseNumTotal(200401, 201812, 0.6))
print(getMoneyYear(upAverageWage, 0.6, 180, privateAccount, 50))
