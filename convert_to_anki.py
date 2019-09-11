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


def convert_evernote_to_anki(init_file_name, tag):
    """
    将Q&A笔记转换为导入anki的文件
    :param init_file_name: 从Q&A笔记中拷贝出来的文字形成的文件，最后要有两个空行
    :param tag: anki中的标签
    :return:
    """
    with open(init_file_name, 'r', encoding="utf-8") as conv_file:
        with open("anki.txt", 'w', encoding='utf-8') as anki:
            for line in conv_file:
                if line.strip().startswith('Q：'):
                    line = line.rstrip() + "\t"
                elif line.strip().startswith("A："):
                    line = '"' + line.lstrip()
                elif line == '\n':
                    line = '"' + line.rstrip() + '\t' + tag + os.linesep
                else:
                    pass
                anki.write(line)


convert_evernote_to_anki("init.txt", "全栈网络安全专家")
