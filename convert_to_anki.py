# -*- coding: utf-8 -*-
# author = 'K0ctr'


import os

"""
将原始文本转换为anki格式的文本
"""


def convert_to_anki1(init_file_name,tag):
    """
    针对以下情况：
    1、每道题都是数字开头
    2、每道题的答案前有“答案”两字
    3、答案总是在单独一行
    :param init_file_name: 原始文件的文件名，需要完整路径
    :param tag: anki中的标签名
    :return:
    """
    with open(init_file_name,"r",encoding="utf-8") as conv_file:
        with open("anki.txt","w",encoding="utf-8") as anki:
            for line in conv_file:
                if line.strip().startswith("答案"):
                    line = "\t" + line.strip()+"\t"+tag+os.linesep
                    print(line)
                    anki.write(line)
                else:
                    anki.write(line.strip())

convert_to_anki1("test.txt","TEST")

