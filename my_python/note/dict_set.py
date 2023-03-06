# 字典是python唯一实现映射关系的内置类型 dict
# 3.8后有序

# 增
a = {'x': 1, 'y': 2}
b = dict(x=1, y=2)
c = dict([('x', 1), ('y', 2)])
d = dict(zip(['x', 'y'], [1, 2]))

d = dict.fromkeys('abcd', 0)    # 快速初始化，默认为None
d['e'] = 0                      # 存在为修改，不存在为新建

# 删
d.pop('e')      # 删除键为参数的元素，返回对应的值，不存在抛出异常，可指定参数取消
d.popitem()     # 删除最后添加的键值对
del d['c']      # 同sequence
d.clear()       # 清空字典

# 改
d = dict.fromkeys('abcde')
d.update({'a': 1, 'b': 2})    # 覆盖修改
d.update(a=1, b=2)            # 同上

# 查
d.get('a')            # 查找键对应的值，不存在抛异常，可指定参数取消
d.setdefault('d', 5)  # 对应键不存在，重新创建键值对
if 'a' in d:          # in 判断存在
    pass

# itrems keys values 获取视图对象随着字典改变
d.items()   # 返回键值对
d.keys()    # 返回键
d.values()  # 返回值

# copy
d.copy()    # 浅拷贝

# 字典推导式
d = {v: k for k, v in d.items()}
#######################################################
# 集合无序且唯一 set

s = {5, 5, 1, 1, 1, 2, 2, 2, 3, 5, 4}
a = set('abcdef')
b = set('accxyz')

# 方法可以传入可迭代对象， 运算符只能对集合进行运算
a.isdisjoint(b)                         # 检测是否相交
a.issubset(b),              a <= b      # 检测子集  a < b 检测真子集
a.issuperset(b),            a >= b      # 检测超集  a > b 检测真超集
a.union(b),                 a | b       # 求并集
a.intersection(b),          a & b       # 求交集
a.difference(b),            a - b       # 求差集
a.symmetric_difference(b),  a ^ b       # 求对称差，不可进行多参数

# 不可变集合
frozenset()     # 以上均可用，以下为set专属
# 集合嵌套可用

# 增
s.add()         # 加入一个元素
s.update()      # 加入多个可迭代对象
# intersection difference symmetric_difference + _update() 均可修改集合

# 删
s.remove(1)     # 删除元素，不存在抛异常
s.discard(2)    # 删除元素，不存在静默处理
s.pop()         # 随机弹出一个元素
s.clear()       # 清空集合

# 可哈希
hash(1)         # 计算哈希值，整数的哈希值是它本身，相同的值哈希值相同
# 大多数可哈希不可变
