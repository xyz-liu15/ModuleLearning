"""
pathlib模块的学习与掌握
pathlib--操作文件的瑞士军刀（文件的读写与增删改查），取代了os.path
"""
from pathlib import Path

path = Path()

print("打印当前目录：",path.cwd())

print("打印当前用户的主目录：",path.home())

# 不必担心你是Windows，MacOS,还是Linux系统，pathlib会自动处理好斜杠和反斜杠的区别。
test_path = path.cwd() / "test" / "test.py"

print("测试脚本的路径是：",test_path)

# 打印测试脚本的名称
print("测试脚本的名称：",test_path.name)
# 打印后缀名
print("打印后缀名：",test_path.suffix)
# 打印父目录
print("打印父目录：",test_path.parent)
# 打印不带后缀名的名称
print("不带后缀名的的名称：",test_path.stem)


# 检查文件类型
print("它是文件夹吗:",test_path.is_dir())
print("它是文件吗：",test_path.is_file())

# 检查文件是否存在
print("它存在吗：",test_path.exists())



# 创建test文件夹及test.py文件
test_path.parent.mkdir(exist_ok = True) 
test_path.touch() # pathlib无法一步到位的创建test/test.py，只能分开创建。


# 给测试脚本中写一些代码
code_content = """print("欢迎来到Python编程世界！")"""
test_path.write_text(data = code_content,encoding = "utf-8")

read_test = test_path.read_text(encoding = "utf-8")

print("这是读取的test.py中的数据：",read_test)


# 删除文件加以及文件
test_path.unlink() # 删除test.py文件
test_path.parent.rmdir() # 删除test文件夹


# 查找文件
path_plus = Path()
print("当前路径：",path_plus)
images_found = path_plus.rglob("*.jpg") # glob()在当前路径下寻找，rglob()在当前路径下递归寻找
for image in images_found:
    print(image)