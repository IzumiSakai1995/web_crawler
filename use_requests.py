#__author: Liu Zheng
#date:2018/6/29


import requests
url = 'http://httpbin.ogr'

# #requests.get()
# response = requests.get(url)
# print(response.text)
# print('type fo response=',type(response))

# #带参数的get：
# data={
#     'name':'Sakai',
#     'age': 22
# }
# response = requests.get(url,params=data)
# print(response.text)

# #解析json
# print(response.json())
# print(type(response.json()))
# #获取二进制文件
# print(response.content)
# print(type(response.content))
# with open('concent_test','wb') as f:
#     f.write(response.content)
#     f.close()

#添加UA
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
#
# #基本POST请求
# data = {
#     'name':'sakai'
# }
# response = requests.post(url,data=data)


#请求方式
# requests.post()
# requests.put()
#requests.delete()

#

#文件上传
# files = {'file':open('note','rb')}
# response = requests.post('url',files=files)

#会话维持



#代理设置
# proxies = {
#     'http':'http://',
#     'https':'https:user:password@//',
#     'https':'socks5://',
# }
# response = requests.get(url,proxies=proxies)