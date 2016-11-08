#coding:utf-8
import os

'''
#开始微信公众号的步骤
一.接入指南
1.填写服务器信息
	URL:
	Token:#用于验证开发者的服务器
	EncodingAESKey:
	#备注：消息体加解密的算法
2.验证服务器地址的有效性
	GET请求：参数--signature/timestamp/nonce/echostr，请求原样返回echostr内容算成功
		分别是微信加密签名，时间戳，随机数，随机字符串
		加密/校验流程：
		a.将token/timestamp/nonce三个参数进行字典序排序
		b.将三个参数字符串拼接成一个字符串进行sha1加密
		c.开发者获得加密后的字符串可与signature对比，标识该请求来源于微信

'''
#1接入指南
def checkSignatureAndReturn():
	pass

import web
from handle import Handle
urls = (
		'/wx','Handle',
	)

# class Handle(object):
# 	def GET(self):
# 		return "hello,this is a test"

if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()