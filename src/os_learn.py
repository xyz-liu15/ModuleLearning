"""
os模块学习
主要聚焦与os模块中无法被替代的功能。
获取环境变量、系统信息
"""
import os

# 第一部分：读取“环境变量”
# os.environ的使用
print("os.environ的类型是：",type(os.environ))

# 获取PATH环境变量
path_variable = os.environ["PATH"] # Windows中是Path

print("我的系统环境变量包括：",path_variable)

print("\n---系统中的部分环境变量---")

count = 0
for key,value in os.environ.items():
    if count < 5:
        print(f"{key} = {value}...")
        count += 1


# 使用os.getenv()，这是最安全最推荐的方式

# 获取一个已存在的环境变量
platform = os.getenv("PLATFORM")
print("PLATFORM环境变量：",platform)

# 获取一个不存在的环境变量
api_key = os.getenv("API_KEY")
print("不存在的环境变量：",api_key)


# 获取一个不存在的环境变量，但是提供一个默认值
run_mode = os.getenv("APP_MODE","production")
print("当前应用模式：",run_mode)


# 第二部分：获取“系统信息”

# os.name

print(os.name) # 获取操作系统的内核名称，在Windows上返回nt，在linux和macos上返回posix
# 可以使用if os.name == "nt":来编写只在Windows上运行的代码。

# os.uname 获取更加详细的系统信息，但是这个函数只在Linux,MacOS上存在！！！
print(os.uname())


# os.cpu_count() 获取电脑的逻辑CPU核心数
print(os.cpu_count())


# os.getlogin() 获取当前登陆系统的用户名
# print(os.getlogin()) # 工作方式老派，有可能会报错（文件或文件夹找不到）

import getpass

print(getpass.getuser())