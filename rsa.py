#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

#RSA加密
def encrypt(public_key, message):
    #默认1024位
    RSA.generate(1024)
    rsakey = RSA.importKey(public_key)# 导入读取到的公钥
    cipher = Cipher_pkcs1_v1_5.new(rsakey)  # 生成对象
    return base64.b64encode(cipher.encrypt(message.encode('utf-8'))).decode("utf8")