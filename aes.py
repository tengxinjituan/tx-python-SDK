#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
from Crypto.Cipher import AES
'''
参考
https://www.cnblogs.com/raymond531/p/10420751.html
'''
class aes():
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]   

    #填充函数，使被加密数据的字节码长度是block_size的整数倍
    def pad(self, text):
        text = text.encode('utf-8')
        count = len(text)
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add).encode('utf-8')
        return entext

    # 加密函数
    def encrypt(self, text):  
        res = self.aes.encrypt(self.pad(text))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    # 解密函数
    def decrypt(self, text):  
        res = base64.decodebytes(text.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)