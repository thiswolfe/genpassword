# -*- coding: utf-8 -*-
# name        : ui_gen.py
# Description : Generate a random password 
# Date        : 2021/11/01
# Author      : wolfe

import os
import sys
import argparse
import random
import string
import tkinter
import tkinter.messagebox
import pyperclip
import logging

root = tkinter.Tk()
root.title("密码生成器")
# root.iconbitmap("gen.ico")
str_result = tkinter.StringVar()
str_result.set("")
run_copy = tkinter.Button(root, text = "复制密码")

def showinfo():
    global str_result
    global run_copy
    result_passwd = str_result.get()
    pyperclip.copy(result_passwd)
    logging.info("复制密码：" + result_passwd)
    tkinter.messagebox.showinfo('复制成功', result_passwd + "\n已复制到剪切板。")
    run_copy['state'] = tkinter.DISABLED

def proc(str_ext, is_upp, is_low, is_num, str_other):

    global str_result
    global run_copy

    RES_SIZE = 10
    ADD_UPP = False
    ADD_LOW = True
    ADD_NUM = True
    OTHER_CHAR = ""

    RES_SIZE = str_ext.get()
    if (0 >= RES_SIZE):
        tkinter.messagebox.showinfo('提示', "密码长度必须大于零！")
        return

    if (1 == is_upp.get()):
        ADD_UPP = True
    if (0 == is_low.get()):
        ADD_LOW = False
    if (0 == is_num.get()):
        ADD_NUM = False
    # 获取内容并去掉全部空格
    OTHER_CHAR = str_other.get().replace(" ","")

    apply_random_str = ""
    if (ADD_UPP):
        apply_random_str += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (ADD_LOW):
        apply_random_str += "abcdefghijklmnopqrstuvwxyz"
    if (ADD_NUM):
        apply_random_str += "0123456789"
    if (len(OTHER_CHAR) > 0):
        apply_random_str += OTHER_CHAR

    use_param = "密码长度[" + str(RES_SIZE) + "];" \
              + "使用大写字母[" + str(ADD_UPP) + "];" \
              + "使用小写字母[" + str(ADD_LOW) + "];" \
              + "使用阿拉伯数字[" + str(ADD_NUM) + "];" \
              + "其他字符[" + str(OTHER_CHAR) + "]"
    logging.info(use_param)

    param = ""
    for i in range(RES_SIZE):
          param += random.choice(str(apply_random_str))
    print(param)

    str_result.set(param)
    logging.info("密码结果：" + param)
    run_copy['state'] = tkinter.NORMAL

def main():

    global str_result
    global root
    
    ui_place = tkinter.Label(root, text="")
    ui_place.grid(row=0, column=4)

    ui_ext_label = tkinter.Label(root, text="密码长度：")
    ui_ext_label.grid(row=1, column=1)
    str_ext = tkinter.IntVar()
    str_ext.set(10)
    ui_ext = tkinter.Spinbox(root, from_=0, to=32, textvariable=str_ext)
    ui_ext.grid(row=1, column=2)

    is_upp = tkinter.IntVar()
    is_upp.set(0)
    ui_upp = tkinter.Checkbutton(root, text="大写字母", variable=is_upp, onvalue=1, offvalue=0)
    ui_upp.grid(row=2, column=1)

    is_low = tkinter.IntVar()
    is_low.set(1)
    ui_low = tkinter.Checkbutton(root, text="小写字母", variable=is_low, onvalue=1, offvalue=0)
    ui_low.grid(row=2, column=2)

    is_num = tkinter.IntVar()
    is_num.set(1)
    ui_num = tkinter.Checkbutton(root, text="阿拉伯数字", variable=is_num, onvalue=1, offvalue=0)
    ui_num.grid(row=2, column=3)

    ui_other_info = tkinter.Label(root, text="其它字符:")
    ui_other_info.grid(row=3, column=1)

    str_other = tkinter.StringVar()
    str_other.set("")
    ui_other = tkinter.Entry(root, textvariable=str_other)
    ui_other.grid(row=3, column=2)

    ui_place = tkinter.Label(root, text="")
    ui_place.grid(row=3, column=3)

    ui_result_label = tkinter.Label(root, text="密码：")
    ui_result_label.grid(row=4, column=1)

    ui_result_info = tkinter.Entry(root, textvariable=str_result, fg='red', bg='gray94', relief='flat')
    ui_result_info['state'] = 'readonly'
    ui_result_info.grid(row=4, column=2)

    run_proc = tkinter.Button(root, text = "获取密码", command = lambda:proc(str_ext, is_upp, is_low, is_num, str_other))
    run_proc.grid(row=5, column=2)

    run_copy['command'] = showinfo
    run_copy['state'] = tkinter.DISABLED
    run_copy.grid(row=5, column=3)

    ui_place = tkinter.Label(root, text="")
    ui_place.grid(row=6, column=0)

    # 固定窗口不可拉伸
    root.resizable(width=False, height=False)
    # 获取屏幕大小
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root.update()
    # 获取窗口大小
    ww = root.winfo_width()
    wh = root.winfo_height()
    x = (sw-ww) / 2
    y = (sh-wh) / 2
    # 设置窗口居中
    root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    # 进入消息循环
    root.mainloop()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.INFO)
    print(" --------- [ START ] --------- ")
    main()
    print(" --------- [  END  ] --------- ")
    pass
