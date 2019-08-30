# -*- coding:utf-8 -*-
# Author: Koctr


from bs4 import BeautifulSoup
import requests
import re


def clone(*username):
    """
    使用python获取github上一个用户的所有仓库
    1. 使用BeautifulSoup获取链接内容，注意404的情况
    2. 分析是否分页
    3. 分析a标签列表中的内容，判断是否为仓库
    4. 根据分析出的仓库逐个clone
    :param username: git 用户名
    :return:
    """
    pass


def pull(*username):
    """
    与用户的远程仓库同步，可以同步clone的仓库
    :param username:git 用户名
    :return:
    """
    pass


def push(*username):
    """
    提交所有修改到用户的远程仓库
    :param username: git 用户名
    :return:
    """
    pass


# todo
# 记录程序运行日志
# 使用正则表达式获取所有库名称，获取分页数（先不实现）
# git clone --branch master git@github.com:sixstars/ctf ctf --depth 1 