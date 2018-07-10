#__author: Liu Zheng
#date:2018/7/1


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
# print(soup.prettify())
#获取内容
# print(soup.title.string)
#标签选择器
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)   #输出第一个匹配结果。
#获取名称
#print(soup.title.name) #获取标签的名称

#获取属性
# print(soup.a.attrs['href'])
# print(soup.a['href'])
#嵌套选择
#print(soup.head.title.string)

#子节点和子孙节点
#print(soup.p.contents) #以列表格式输出子节点

# print(soup.p.children)
# for i,child in enumerate(soup.p.children):  #children是一个迭代器
#     print(i,child)
#
# print(soup.p.descendants)   #获取所有子孙节点 返回类型为迭代器
# for i,child in enumerate(soup.p.descendants):
#     print(i,child)

#父节点，祖先节点
# print(soup.a.parent)
# print(soup.a.parents)

#兄弟节点
# print(list(enumerate(soup.p.next_siblings))) #之后的兄弟节点
# print(list(enumerate(soup.p.previous_siblings)))#之前的兄弟节点

#标准选择器
# find_all(name,attrs,recursive,text,**kwargs)
# 根据标签名，属性，内容查找文档

#name
# print(soup.find_all('a'),)
# for a in soup.find_all('a'):
#     print(a)

#attrs
# print(soup.find_all({'name':'dromouse'}))
# print(soup.find_all(id=''))
# # print(soup.find_all(class_=''))

#text
#print(soup.find_all(text='')) #s输出文本内容  用于内容匹配

# find(name,attrs,recursive,text,**kwargs) 返回单个元素
#print(soup.find('a'))

#CSS选择器
print((soup.select('.title'))) #class 选择  加. 点
print(soup.select('p b'))  #标签选择