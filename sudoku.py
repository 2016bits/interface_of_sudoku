#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
from _ctypes import byref
from tkinter import *
from ctypes import *
import random
from  numpy import *
from string import *


class Sudo(object):
    """将所有函数包装在该类中"""
    def __init__(self):
        # A用于存储显示题目数据（含0），B用于存储终局数据（不含0）
        self.B = []
        self.A = []

        # ET用于存储文本框
        self.ET = []
        # Answer用于存储空格处原来的数字
        self.Answer = []
        # count记录空格个数
        self.count = 1

    def fun1(self):
        """生成题目"""
        root = Tk()
        root.geometry('1000x1000+300+300')

        # 生成9*9的矩阵
        for i in range(81):
            self.B.append(0)
            self.A.append(0)

        # 生成数组
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # 获得随机序列
        random.shuffle(a)

        # 偏移量序列
        b = [3, 6, 1, 4, 7, 2, 5, 8]

        # 生成数独终局循环
        for i in range(81):
            if i > 8:
                # 第二行到第九行
                self.A[i] = a[(int(i % 9) + b[int((i - 9) / 9)]) % 9]
            else:
                # 第一行
                self.A[i] = a[int(i % 9)]
            self.B[i] = self.A[i]

        # 随机挖空，原则是先在每个3*3里面空出两个，之后再在剩余地方进行扣除，允许重复，达到随机
        for i in range(9):
            x1 = random.randint(0, 2)
            y1 = random.randint(0, 2)
            self.A[int(i / 3) * 27 + (i % 3) * 3 + x1 * 9 + y1] = 0
            x1 = random.randint(0, 2)
            y1 = random.randint(0, 2)
            self.A[int(i / 3) * 27 + (i % 3) * 3 + x1 * 9 + y1] = 0

        # 保证至少42个空
        for i in range(42):
            j = random.randint(0, 80)
            if self.A[j] != 0:
                self.A[j] = 0

        BU = []
        # 生成9*9的矩阵
        for i in range(81):
            BU.append(0)

        count = 1
        for i in range(81):
            if self.A[i] == 0:
                # 可输入的文本框
                entry = Entry(root, width=3)
                entry.grid(row=int(i / 9), column=int(i % 9))
                self.ET.append(entry)
                self.Answer.append(self.B[i])
                count += 1
            else:
                v = self.A[i]
                BU[i] = Button(root, text=str(v), width=3, height=1)
                BU[i].grid(row=int(i / 9), column=int(i % 9))

        # 生成“生成”和“检验”两个按钮
        BU = Button(root, text='生成', width=3, height=2, command=self.fun1)
        BU.grid(row=31, column=0)

        # 生成下一题的按钮
        BU = Button(root, text='检验', width=3, height=2, command=self.fun2)
        # 下一题按钮位置
        BU.grid(row=31, column=24)


    def fun2(self):
        """检验答案"""
        count = self.count
        Answer = self.Answer
        ET = self.ET
        flag = True
        for i in range(1, count + 1):
            if str(Answer[i]) != ET[i].get():
                flag = False
                print(i)
                break

        # 响应检验结果
        if flag:
            # 结果正确
            root2 = Tk()
            root2.geometry('500x500+25+25')
            bu= Button(root2, text='正确', width=25, height=25)
            bu.grid(row=25,column=25)
        else:
            # 结果错误
            root3 = Tk()
            root3.geometry('500x500+25+25')
            bu = Button(root3, text='错误', width=25, height=25)
            bu.grid(row=25, column=25)


def main():
    """主函数"""
    sudo = Sudo()
    # 根窗口
    root = Tk()
    root.geometry('1000x1000+300+300')

    BU=[]
    for i in range(81):
        BU.append(0)
    for i in range(81):
        BU[i] = Button(root, text='',width=3,height=1)
        BU[i].grid(row=int(i/9), column=int(i%9))

    # 生成下一题的按钮
    BU = Button(root, text='生成',width=3,height=2,command=sudo.fun1)

    # 下一题按钮位置
    BU.grid(row=31, column=0)

    # 生成下一题的按钮
    BU = Button(root, text='检验',width=3,height=2,command=sudo.fun2)

    # 下一题按钮位置
    BU.grid(row=31, column=12)
    root.mainloop()


main()

