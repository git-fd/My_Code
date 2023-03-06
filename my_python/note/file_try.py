# 文件

# r 读取
# w 写入，文件存在则清空
# a 追加
# b 二进制
# + 混合模式

from pathlib import Path
f = open('test.txt', 'w')          # 打开文件
f.write('666\n')                   # 写入字符串，返回写入的数量
f.writelines(['555\n', '444\n'])   # 写入多个，不自动换行
for i in range(3, 0, -1):
    f.write(str(i) * 3 + '\n')
f.readable()                       # 判断读取功能
f.writable()                       # 判断写入功能
f.close()                          # 关闭文件
f = open('test.txt', 'r')
for e in f:                        # 遍历文件
    print(e, end='')
f.tell()                           # 文件指针的位置
f.seek(0)                          # 修改文件指针的位置
f.readline()                       # 读取一行内容
f.read()                           # 读取文件内容，默认全部
# f.truncate()                     # 截取到文件位置，默认截取到的当前指针位置
f.flush()                          # 刷新缓存区
f.close()

__import__('time').sleep(1)

# 路径处理
Path.cwd()                      # 获取当前目录的路径
p = Path('D:/Microsoft/Code')
q = p / 'test.txt'
p.is_dir()                      # 判断是否是文件夹
q.is_file()                     # 判断是否是文件
p.exists()                      # 检测路径是否存在
p.name                          # 获取路径的最后一个部分
q.stem                          # 获取文件名
q.suffix                        # 获取文件后缀名
q.parent                        # 获取父级目录
q.parents                       # 获得逻辑祖先路径构成的序列，支持索引
q.parts                         # 将路径的各个组件拆封成元组
q.stat()                        # 查询文件或者文件夹的信息
Path('./test.txt').resolve()    # 相对路径转换绝对路径
p.iterdir()                     # 获取当前路径下的所有子文件夹和子文件
(p / 'test').mkdir()            # 创建文件夹，默认文件存在异常，默认父路径不存在异常
q.rename('newtest.txt')         # 修改文件名
__import__('time').sleep(1)
(p / 'newtest.txt').unlink()    # 删除文件
(p/'test').rmdir()              # 删除文件夹，目录不空不随意删除
p.glob('*.py')                  # 查找以.txt为后缀的文件 **为递归搜索

# with 上下文管理器（确保文件正常关闭）
with open('test.txt', 'w') as f:
    f.write('I love you\n')
    f.write('666')
    # 1 / 0
__import__('time').sleep(1)
__import__('os').remove('test.txt')

# pickle 序列化py对象
with open('data.pkl', 'wb') as f:   # dump 序列化py对象，并写入文件
    __import__('pickle').dump((1, [1], {1}, '1'), f)

with open('data.pkl', 'rb') as f:   # load 反序列化py对象，并以元组返回
    print(__import__('pickle').load(f))

__import__('time').sleep(1)
__import__('os').remove('data.pkl')

##########################################################################
# 异常 try-except-else-finally try-except try-finally 可嵌套
try:
    1 / 0
except ZeroDivisionError as e:  # 可用元组包含多个异常
    print(e)
except Exception as e:          # 捕获未知异常
    print(e)
except:         # 有未主动捕获异常处理，与上不共用
    pass
else:           # 没有检测任何异常执行
    pass        
finally:        # 无论异常是否发生都会执行
    pass

# raise 抛出一个存在的异常
# raise-from    异常链
try:
    raise ValueError('666')
except:
    pass
try:
    raise ValueError('666') from ZeroDivisionError('6')
except:
    pass

# assert 只能引发 AssertionError异常（调试用）
s = '666'
assert s == '666'

# 异常实现goto
try:
    while 1:
        while 1:
            for i in range(10):
                if i > 5:
                    raise
except:
    pass