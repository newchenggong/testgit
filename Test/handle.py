#coding:utf-8
# filename:handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
	def GET(self):
		try:
			data = web.input()
			if len(data) == 0:
				return "hello,this is handle view."
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = ""#公众平台基本配置中的信息
			llist = [token,timestamp,nonce]
			llist.sort()
			sha1 = hashlib.sha1()
			map(sha1.update,llist)
			hashcode = sha1.hexdigest()
			print "handle/GET func:hashcode,signature:",hashcode,signature
			if hashcode == signature:
				return echostr
			else:
				return ""
		except Exception,Argument:
			return Argument

	def POST(self):
		try:
			webData = web.data()
			print "Handle Post webdata is ",webData #后台打印日志
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				if recMsg.MsgType == 'text':
					content = "test"
					replyMsg = reply.TextMsg(toUser,fromUser,content)
					return replyMsg.send()
				if recMsg.MsgType == 'image':
					mediaId = recMsg.MediaId
					replyMsg = reply.IamgeMsg(toUser,fromUser,mediaId)
					return replyMsg.send()
				else:
					return reply.Msg().send()
			else:
				print "暂且不处理"
				return reply.Msg().send()
		except Exception,Argment:
			return Argment

		