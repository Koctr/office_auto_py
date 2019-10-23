# -*- coding: utf-8 -*-
# author = 'K0ctr'


import os

"""
将原始文本转换为anki格式的文本
"""


def convert_to_anki1(init_file_name, tag):
    """
    针对以下情况：
    1、每道题都是数字开头
    2、每道题的答案前有“答案”两字
    3、答案总是在单独一行
    :param init_file_name: 原始文件的文件名，需要完整路径
    :param tag: anki中的标签名
    :return:
    """
    with open(init_file_name, "r", encoding="utf-8") as conv_file:
        with open("anki.txt", "w", encoding="utf-8") as anki:
            for line in conv_file:
                if line.strip().startswith("答案"):
                    line = "\t" + line.strip() + "\t" + tag + os.linesep
                    print(line)
                    anki.write(line)
                else:
                    anki.write(line.strip())


def convert_evernote_to_anki(init_file_name):
    """
    将Q&A笔记转换为导入anki的文件
    :param init_file_name:
        从Q&A笔记中拷贝出来的文字形成的文件
        每一组卡片的第一行是tag
        最后要有两个空行
    :return:
    """
    tag = ""
    w_line = ""
    with open(init_file_name, 'r', encoding="utf-8") as conv_file:
        with open("anki.txt", 'w', encoding='utf-8') as anki:
            for line in conv_file:
                if line.strip().startswith("TAG："):
                    tag = line.strip().replace("TAG：", "")
                    # 查找到tag时要清除上一条卡片的w_line
                    w_line = ""
                elif line.strip().startswith('Q：'):
                    w_line = line.rstrip() + "\t"
                elif line.strip().startswith("A："):
                    w_line = '"' + line.lstrip()
                elif line == '\n':
                    w_line = '"' + line.rstrip() + '\t' + tag + os.linesep
                else:
                    w_line = line
                anki.write(w_line)


convert_evernote_to_anki("init.txt")
