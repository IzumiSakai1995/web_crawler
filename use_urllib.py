#__author: Liu Zheng
#date:2018/6/29

#urllib.request 请求模块
#urllib.error 异常处理模块
#urllib.parse rul解析模块
#urllib.robots
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
