"""
json模块的学习
序列化：
json.dumps() 将Python对象变成内存中的JSON字符串。适用于网络传输，存入数据库等场景。
json.dump() 将Pyhon对象直接写入一个文件指针。适用于直接将程序状态保存为.json文件。

反序列化：
json.loads() 将内存中的JSON字符串解析成Python对象。
json.load() 从一个文件指针中读取文本并且解析成Python对象。
"""
import json
from rich.pretty import pprint

with open("纳兰性德诗集.json","r",encoding = "utf-8") as f:
    poems = json.load(f)
    print(type(poems))


if isinstance(poems,list):
    print(len(poems))
    pprint(poems)
    