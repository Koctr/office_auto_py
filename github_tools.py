# -*- coding:utf-8 -*-
# Author: Koctr


from bs4 import BeautifulSoup
import re


def clone(*username):
    """
    克隆username所有仓库
    :param username: git 用户名
    :return:
    """
    pass


def check(*username):
    """
    检查usernam所有仓库是否更新
    :param username:git 用户名
    :return:
    """
    pass


def pull(**repo):
    """
    与远程库同步
    :param repo:远程仓库名称
    :return:
    """
    pass


def push(**repo):
    """
    提交修改到元仓库
    :param repo: 远程仓库名称
    :return:
    """
    pass


# todo
# 记录程序运行日志
# 使用正则表达式获取所有库名称，获取分页数（先不实现）
# git clone --branch master git@github.com:sixstars/ctf ctf --depth 1 