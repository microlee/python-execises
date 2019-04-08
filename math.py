# -*- coding: utf-8 -*-
# math.py
# @author microlee
# @description 湘师实验小学二年级数学口算出题
# @created Wed Nov 14 2018 08:35:13 GMT+0800 (中国标准时间)
# @last-modified Mon Apr 08 2019 12:01:09 GMT+0800 (中国标准时间)

from random import randint

sym = [' + ', ' - ']

fobj = open('math.txt', 'w')
fobj.writelines(
    r'                     用时______分钟           对______题（共120题）           家长签名：'
    + '\r\n')
fobj.writelines(
    r'                                   湘师实验小学二年级一班学生数学口算训练专用           ' +
    '\r\n')


def pmbase(pmin, pmax, mmin, mmax, multimin, multimax):

    # 单加法
    plus1 = randint(pmin, pmax - 1)
    plus2 = randint(pmin, pmax - plus1)
    plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' ='

    # 单减法
    minus1 = randint(mmin, mmax)
    minus2 = randint(mmin, mmax)
    minussum = minus1 + minus2
    minus = str(minussum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' ='

    # 单加法
    plus1 = randint(pmin, pmax - 1)
    plus2 = randint(pmin, pmax - plus1)
    plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' ='

    # 单乘法
    multi1 = randint(multimin, multimax)
    multi2 = randint(multimin, multimax)
    multi = str(multi1).rjust(2) + ' x ' + str(multi2).rjust(2) + ' ='

    baseline = [plus, minus, plus, multi]
    line = (28 * ' ').join(baseline)
    print(line)
    fobj.writelines(line + '\r\n')


def oneline(pmin, pmax, mmin, mmax, multimin, multimax):

    # 单加法
    plus1 = randint(pmin, pmax - 1)
    plus2 = randint(pmin, pmax - plus1)
    plus = str(plus1).rjust(2) + ' + ' + str(plus2).rjust(2) + ' ='

    # 单减法
    minus1 = randint(mmin, mmax)
    minus2 = randint(mmin, mmax)
    minussum = minus1 + minus2
    minus = str(minussum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' ='

    # 加减混合
    sym1 = sym[randint(0, 1)]
    sym2 = sym[randint(0, 1)]

    if sym1 == ' + ' and sym2 == ' + ':
        temp = randint(3, 100)
        first = randint(1, temp - 2)
        second = temp - first
        second = randint(1, second - 1)
        third = temp - first - second
    elif sym1 == ' + ' and sym2 == ' - ':
        temp = randint(2, 100)
        first = randint(1, temp - 1)
        second = temp - first
        third = randint(1, temp)
    elif sym1 == ' - ' and sym2 == ' + ':
        first = randint(2, 100)
        second = randint(1, first)
        third = randint(1, 100 - first + second)
    elif sym1 == ' - ' and sym2 == ' - ':
        first = randint(3, 100)
        second = randint(1, first)
        third = first - second
        if third <= 1:
            third = 1
        else:
            third = randint(1, third)
    pm = str(first).rjust(2) + sym1 + str(second).rjust(2) + sym2 + str(
        third).rjust(2) + ' ='

    # 乘加减混合
    sym1 = sym[randint(0, 1)]
    first = randint(multimin, multimax)
    second = randint(multimin, multimax)
    temp = first * second
    if temp <= 10:
        if sym1 == ' - ':
            third = randint(1, temp)
        else:
            third = randint(1, 9)
    else:
        third = randint(1, 9)
    mix = str(first).rjust(2) + ' x ' + str(second).rjust(2) + sym1 + str(
        third).rjust(2) + ' ='

    lineitem = [plus, minus, pm, mix]
    line = (28 * ' ').join(lineitem)
    print(line)
    fobj.writelines(line + '\r\n')


def oral_exeicise():
    for col in range(12):
        pmbase(1, 100, 1, 50, 1, 6)
    for col in range(18):
        oneline(1, 100, 1, 50, 1, 6)


oral_exeicise()
fobj.close()
