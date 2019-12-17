#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import parse
import requests
import json
import rsa
import aes
import utils


"""
公钥
-----BEGIN RSA PUBLIC KEY-----
.......
-----END RSA PUBLIC KEY-----
必须要用
"""
publicKey = '''-----BEGIN RSA PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCExkDB2nbdopq7lYgKhwzrVgMo
M7WJqz3THpMjGg0sGV6kydiYSXTc/+OdMUIaIWfuY0T2CLpKmrNG+4FHqMOfnCU7
1gqysbmd02zpNW+d9AtN07NoxeekgiWJxLtKI3LSaY/SgOjrpIDEFWXUTEZ7hNNw
ga1hRkfxliA1MSK2jQIDAQAB
-----END RSA PUBLIC KEY-----'''

"""普通短信"""
def msgSend(account, password, phone, msg, uid):
    url = 'http://10.10.50.3:8082/msg/send/json'
    body = {
        "account":account,#账号
        "password":password,#密码
        "msg":msg,#短信内容
        "phone":phone,#手机号码
        "sendtime":"",#定时时间 定时发送短信时间。格式为yyyyMMddHHmm，值小于或等于当前时间则立即发送，默认立即发送
        "report":"true",#是否需要状态报告（默认false）
        "extend":"555",#下发短信号码扩展码，纯数字，建议1-3位，选填
        "uid":uid,#该条短信在您业务系统内的ID，如产品号或者短信发送记录流水号，选填
        "format":"json",#请求相应格式json或者xml或者txt，选填
        "useragent":"http"#来源(cmpp,web,http)，默认http，选填
    }
    headers = {'content-type': "application/json"}

    key = utils.randomKey()
    pc = aes.aes(key) 

    rsaBody = {
        "account":account,
        "data":pc.encrypt(json.dumps(body)),
        "key":rsa.encrypt(publicKey,key)
    }
    # 普通提交 
    #response = requests.post(url, data = json.dumps(body), headers = headers)
    # 加密提交 
    response  = requests.post(url+"/rsa", json = rsaBody, headers = headers)
    
    # 返回信息
    print(response.text)
    # 返回响应头
    print(response.status_code)

"""变量短信"""
def msgVariable(account, password, params, msg, uid):
    url = 'http://10.10.50.3:8082/msg/variable/json'
    body = {
        "account":account,#账号
        "password":password,#密码
        "msg":msg,#短信内容
        "params":params,#手机号码和变量参数，多组参数使用英文分号;区分，必填
        "sendtime":"",#定时时间 定时发送短信时间。格式为yyyyMMddHHmm，值小于或等于当前时间则立即发送，默认立即发送
        "report":"true",#是否需要状态报告（默认false）
        "extend":"555",#下发短信号码扩展码，纯数字，建议1-3位，选填
        "uid":uid,#该条短信在您业务系统内的ID，如产品号或者短信发送记录流水号，选填
        "format":"json",#请求相应格式json或者xml或者txt，选填
        "useragent":"http"#来源(cmpp,web,http)，默认http，选填
    }
    headers = {'content-type': "application/json"}

    key = utils.randomKey()
    pc = aes.aes(key) 

    rsaBody = {
        "account":account,
        "data":pc.encrypt(json.dumps(body)),
        "key":rsa.encrypt(publicKey,key)
    }
    # 普通提交 
    #response = requests.post(url, data = json.dumps(body), headers = headers)
    # 加密提交 
    response  = requests.post(url+"/rsa", json = rsaBody, headers = headers)
    
    # 返回信息
    print(response.text)
    # 返回响应头
    print(response.status_code)

"""短信包发送"""
def msgPackage(account, password, msg, uid):
    url = 'http://10.10.50.3:8082/msg/sendpackage/json'
    body = 'account={account}&password={password}&{msg}&sendtime=201908080000&report=true&extend=555&uid={uid}&format=json&useragent=http'
    headers = {'content-type': "application/x-www-form-urlencoded"}

    key = utils.randomKey()
    pc = aes.aes(key) 

    rsaBody = {
        "account":account,
        "data":pc.encrypt(body.format(account=account,password=password,msg=msg,uid=uid)),
        "key":rsa.encrypt(publicKey,key)
    }

    # 普通提交 
     #response = requests.post(url, data = body.format(account=account,password=password,msg=msg,uid=uid).encode('utf-8'), headers = headers)
    # 加密提交 
    response  = requests.post(url+"/rsa", data =parse.urlencode(rsaBody), headers = headers)
    
    # 返回信息
    print(response.text)
    # 返回响应头
    print(response.status_code)    

"""余额查询"""
def queryBalance(account, password, uid):
    url = 'http://10.10.50.3:8082/msg/balance/json'
    body = {
        "account":account,#账号
        "password":password,#密码
        "uid":uid,#该条短信在您业务系统内的ID，如产品号或者短信发送记录流水号，选填
        "format":"json"#请求相应格式json或者xml或者txt，选填
    }
    headers = {'content-type': "application/json"}

    key = utils.randomKey()
    pc = aes.aes(key) 

    rsaBody = {
        "account":account,
        "data":pc.encrypt(json.dumps(body)),
        "key":rsa.encrypt(publicKey,key)
    }
    # 普通提交 
    #response = requests.post(url, data = json.dumps(body), headers = headers)
    # 加密提交 
    response  = requests.post(url+"/rsa", json = rsaBody, headers = headers)
    
    # 返回信息
    print(response.text)
    # 返回响应头
    print(response.status_code)