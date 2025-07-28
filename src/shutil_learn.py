import shutil
from pathlib import Path


path = Path()

# 创建一个test文件夹
test_dictonary = path / "test"
test_dictonary.mkdir(exist_ok = True)

# 在test文件夹下创建一个test.py文件
test_script = test_dictonary / "test.py"
test_script.touch(exist_ok = True)

# 在test.py文件中写一些代码。
code_content = """print('The Python World')\nprint('你好！Python编程世界！！！')"""

test_script.write_text(data = code_content,encoding = "utf-8")

# 一、shutil复制功能：
# 1. shutil.copyfile(src,dst) 仅仅复制文件内容，不保留任何权限和时间戳
# src和dst都必须是完整的路径（字符串或者pathlin.Path对象）
# 如果dst文件不存在，会被创建，存在的话，会被覆盖。
# dst不能是目录。
# 这个函数不复制任何文件的权限等元数据。
test_copy = path / "test_copy"
test_copy.mkdir(exist_ok = True)
test_copy_script = test_copy / "test_copy.py"
shutil.copyfile(test_script,test_copy_script)


# 2. shutil.copy():复制文件内容+权限
# 这个函数比copyfile()更常用，因为他更灵活
# src必须是一个文件
# dst可以是文件名，也可以是目录
# 如果dst是一个文件名字，行为类似copyfile()
# 如果dst是一个目录，则会在dst目录下创建一个和src同名的文件，并将内容和权限复制过去。
# 不复制其他元数据，如创建时间和修改时间。


# 3.shutil.copy2():最完整的单文件复制
# 会复制所有元数据


# 4. shutil.copytree(src,dst,dirs_exist_ok,ignore):递归复制目录
# 默认情况下，dst目录必须不存在。
# dirs_exist_ok = True时，会把src下的文件和子目录合并到dst中去
# ignore接受一个列表，用于被会略的文件和目录（不被复制）


# 二、移动和重命名
# shutil.move(src,dst)
# 递归的移动文件后者目录src到dst
# 如果dst存在，则直接移动到dst下
# 如果dst不存在，src会被移动并且重命名为src。
# 如果dst是一个已存在的文件，则抛出异常。
move_test = path / "move_test"
move_test.mkdir(exist_ok = True)

# shutil.move(test_dictonary,move_test)


# 三、删除操作
# shutil.rmtree(path)
# 参数ignore_errors = True，删除过程中出现的错误将会被忽略（如权限问题）
# 参数onerror，可以传递一个可调用对象（函数），当发生错误时调用它。

# 删除 test_copy文件夹
shutil.rmtree(test_copy)

# 四、归档（压缩和解压）
# shutil.make_archive(base_name,format,root_dir)
# 参数base_name不包含扩展名
shutil.make_archive("test_archive","zip",test_dictonary)

# shutil.unpack_archive(filename,extract_dir)
# 解压一个归档的文件
shutil.unpack_archive("test_archive.zip",path)