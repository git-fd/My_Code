# 函数 def 定义

# 参数
def func(s, v, o):
    return ' '.join((s, v, o))


# 位置参数
func('I', 'love', 'you')
func('You', 'love', 'me')

# 关键字参数
func(s='I', v='love', o='you')

# 混合使用位置参数必须在关键字参数之前
func('I', 'love', o='you')


def func(s, v, o='you'):  # 定义时默认参数放在最后
    return ' '.join((s, v, o))


func('I', 'love')         # 使用默认参数
func('I', 'love', 'her')  # 指定参数


def func(a, /, b):    # /左侧的参数必须是位置参数，右侧随便
    pass


def func(a, *, b):    # *左侧随意，右侧必须是关键字参数--匿名的收集参数
    pass

# 收集参数
def func(*args):          # args收集多个参--元组打包
    pass


def func(*args, a, b):    # 有其他参数时需要用关键字参数
    pass


def func(**kwargs):       # 关键字参数收集--字典打包
    pass
# 混合使用需要注意使用顺序
def func(a, *b, **c):     # myfunc(1, 2, 3, x=4, y=5)
    pass

# 解包参数
def func(a, b, c, d):
    pass


x = (1, 2, 3, 4)
func(*x)    # func(x)错误，缺少参数，**解包字典

# 作用域，局部变量，全局变量，局部覆盖全局
# global 在函数内声明后，可对全局变量做出修改

# 嵌套函数
def A():
    def B():
        print('B')
    B()         # 外部无法调用
    print('A')
# nonlocal 在内部函数声明后，内部函数可以修改外部函数的值

### LEGB 变量解析机制 ###
# L   local       局部作用域
# E   enclosed    嵌套函数的外层作用域
# G   global      全局作用域
# B   build-in    内置作用域


# 闭包--工厂函数
def power(exp):       # 嵌套函数的外层作用域会被保留
    def exp_of(base):
        return base ** exp
    return exp_of


square = power(2)
cube = power(3)


def outer():
    x, y = 0, 0     # 带记忆功能的函数，x，y值随着参数x1，y1修改

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f'x = {x}, y = {y}')
    return inner
# 例如设计角色移动的方法，并对角色坐标进行保护


# 装饰器--闭包加函数作为参数
def time_master(func):
    def call_func():        # 检测函数运行时间
        b = __import__('time').time()
        func()
        e = __import__('time').time()
        print(f'{e-b:.4f}')
    return call_func


@time_master        # test=time_master(test)
def test():
    __import__('time').sleep(2)

# 进阶装饰器参数
def logger(msg):
    def time_master(func):
        def call_func():
            b = __import__('time').time()
            func()
            e = __import__('time').time()
            print(f'{msg}:{e-b:.4f}')
        return call_func
    return time_master


@logger(msg='6')    # test=logger(msg='6')(test )
def test():
    __import__('time').sleep(2)


# lambda 能够出现在def不能出现的地方，简单的实现
x = [lambda x: x * x, 2]   # x[0](x[1])
list(filter(lambda x: x % 2, range(10)))

# 生成器 yield--制造机器（特殊的迭代器）支持next函数
def counter():  # 生成一个数据并且暂停函数，等到下一次调用
    for i in range(10):
        yield i


def fib():
    a, b = 0, 1
    while b < 100:
        yield a
        a, b = b, a + b


# 生成器推导式每次产生一个数据，列表推导式产生所有数据
(i * 2 for i in range(10))

# 函数调用自己--递归
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


def hanoi(n, x='A', y='B', z='C'):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, '-->', z)
        hanoi(n - 1, y, x, z)

# 函数文档 help()
# 类型注释：期望 list[int], dict[str, int]
def exchange(dollar: int, reat: float = 6.32) -> float:
    '''
    功能：汇率转换， 美元 -> 人民币
    参数：
    - dollar 美元数量
    - rate  汇率， 默认6.32
    返回值：
    - 人民币数量
    '''
    return dollar * reat


# 内省
exchange.__name__           # 函数的名字
exchange.__annotations__    # 函数类型注释
exchange.__doc__            # 函数文档，一般用help


# 高阶函数functools 使用函数作为参数的函数
__import__('functools').reduce(lambda x,y:x*y, range(1, 11)) # 10的阶乘

# 偏函数(类似闭包) 对指定的函数进行二次包装通常将现有的函数部分参数预先绑定
square = __import__('functools').partial(pow, exp=2)

# 普通装饰器修改函数名  @functools.wraps装饰器改回来
