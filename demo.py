#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 * 本实例需要pycryptodome包
 * 安装方法
 * 1、
 * pip install pycryptodome
'''

import msgSend as send
import utils

account = "lijie02" #账号
password = "lijie02_lijie02" #密码
phone = "18703807701" #手机号码
msg = "您的验证码：2048【世界和平】" #短信内容
uid = "1000102" #产品Id

#发送普通短信
#send.msgSend(account,password,phone,msg,uid)

#发送变量
#params = "18703807701,1122;18703807703,3333;" #手机号码
#msg = "您的验证码：{$var}【世界和平】" #短信内容

#send.mgVariable(account,password,params,msg,uid)

#短信包短信
msg = "msg=18703807701|您的短信包短信验证码：11111【世界和平】&msg=18703807702|您的短信包短信验证码：2222【世界和平】" #短信内容

send.msgPackage(account,password,msg,uid)


#余额查询 查询间隔要大于10秒
#send.queryBalance(account,password,uid)
