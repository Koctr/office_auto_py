# -*- coding: utf-8 -*-
# author = 'K0ctr'


def format_excel_questions(fullname):
    """

    :param filename:
    :return:
    """
    pass


with open(r"D:\网络安全合规指引.txt", "r", encoding="utf-8") as f1:
    with open(r"网络安全合规指引.txt", "w", encoding="utf-8") as f2:
        for line in f1:
            """
            if line.startswith("答案"):
                line = "\t" + line
            """
            if line[0].isdigit() or line[0:2].isdigit() or line[0:3].isdigit():
                line = "\n" + line.rstrip("\r\n")
            else:
                line = line.rstrip("\r\n")
            f2.write(line)
with open(r"网络安全合规指引.txt", 'r', encoding="utf-8") as f1:
    with open(r'网络安全合规指引.xls', "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line.strip() + "\t" + "网络安全合规指引" + "\n")

with open(r"D:\信息安全管理实践.txt", 'r', encoding="utf-8") as f1:
    with open(r"信息安全管理实践.txt", 'w', encoding="utf-8") as f2:
        for line in f1:
            """
            if line.startswith("答案"):
                line = "\t" + line
            """
            if line[0].isdigit() or line[0:2].isdigit() or line[0:3].isdigit():
                line = "\n" + line.rstrip("\r\n")
            else:
                line = line.rstrip("\r\n")
            f2.write(line)
with open(r"信息安全管理实践.txt", 'r', encoding="utf-8") as f1:
    with open(r'信息安全管理实践.xls', "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(line.strip() + "\t" + "信息安全管理实践" + "\n")
