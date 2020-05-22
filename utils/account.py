#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: account.py  time: 2020/5/20 20:11
from bcrypt import hashpw, gensalt

# 这个是随机生成的盐
# salt = gensalt(12)

# 这个是通过盐去加密
# passwd = hashpw("123456".encode('utf8'), salt)

# 将输入的明文密码与密文密码进行加密，是否等于密文密码。

def pas_encryption(pwd, passwd=None, b=True):
    if b:
        # 这个是随机生成的盐
        salt = gensalt(12)
        # 这个是通过盐去加密
        passwd = hashpw(pwd.encode('utf8'), salt)
        return passwd
    else:
        return hashpw(pwd.encode('utf8'), passwd.encode("utf8"))