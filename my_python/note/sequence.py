# 可以通过索引获得每一个元素
# 从0开始，均可切片
# +拼接 *重复拷贝
# 可变序列：list
# 不可变序列：tuple str

a = [1, 2, 3]
a += a
a *= 3
s = '123'
s += s
s *= 3

# += *= 对与str tuple 会重新生成一个数据

id(a)   # 查看唯一地址值 is 判断id是否相等

if '1' in s:    # in 判断是否包含于
    pass

x = 'I love you'
y = [1, 2, 3]
del x, y        # 删除变量
x = [1, 2, 3, 4, 5]
del x[1:4]      # 删除第二到第四元素 x[1:4] = []
del x[:]        # 清空x x[:] = []

# 相互转换
x = '12345'
y = [1, 2, 3]
list(x)     # 转换为list
tuple(x)    # 转换为tuple
str(y)      # 转换为str

# min max len sum
min(y), max(y)
min(1, 2), max(2, 1)
max([], default='6')        # None时，异常，传入参数default min同
len(range(2 ** 63 - 1))     # len 调用c语言结构体对象长度，64位机位2^63-1
sum([1, 0, 0, 0, 8, 6])     # 求和，默认起始值为0

# sorted reversed
s = [1, 2, 3, 0, 6]
sorted(s)          # 任何可迭代对象排序，并返回一个列表，使用同list的sort方法
reversed(s)        # 返回一个反向迭代器

# all any
x = [1, 1, 1]
y = [1, 1, 0]
all(x)      # 判断可迭代对象所有元素为真
any(y)      # 判断可迭代对象中存在元素为真

# enumerate zip map filter
a = ['a', 'b', 'c', 'd']
b = [0, 1, 2, 3, 4]
enumerate(a)    # 返回一个二元组构成列表的迭代器，二元组为(i, a[i]), 默认i从0开始
zip(a, b)       # 返回多个可迭代对象聚合的元组，第i个元组包括每个参数第i个元素，取最短
__import__('zipitertools').zip_longest(a, b)    # 同上取最长不足的补None
map(ord, 'ab')  # 对可迭代对象进行函数加工，返回迭代器，根据加工函数的参数传入对应的可迭代对象， 长度zip
filter(str.islower(), 'aAvAcD')        # 同上只保留真值，过滤器

# 迭代器肯定时可迭代对象 迭代器一次性，可迭代对象重复使用
y = iter(x)     # 将可迭代对象返回为迭代器
next(y)         # 迭代一次，并返回值，结束时异常，加参数处理异常
