# 大小写字母转换
s = 'I love Python'
s.capitalize()      # 将全句第一个字母大写
s.casefold()        # 所有字母都小写
s.title()           # 每个单词首字母大写，其他字母小写
s.swapcase()        # 大小学反转
s.upper()           # 英文字母大写
s.lower()           # 英文字母小写

# 左中右对齐   参数小于长度原样输出
# 默认填充字符为空格
s = '有内鬼，停止交易！'
s.center(15)        # 居中
s.ljust(15)         # 左对齐
s.rjust(15)         # 右对齐
s.zfill(15)         # 用0填充左侧

# 查找 [)
s = '上海自来水来自海上'
s.count('海')       # 字串出现的次数
s.find('海')        # 从左往右查找第一次出现字串的索引，未找到返回-1
s.rfind('海')       # 从右往左查找第一次出现字串的索引，未找到返回-1
s.index('海')       # 同上，未找到抛出异常
s.rindex('海')      # 同上

# 替换
s = '''print()      print() print()'''
s.expandtabs(4)     # 用空格替换tab，参数为替换个数
s.replace('print', '666')   # 新串替换旧串，默认替换全部，可指定替换次数
s.translate(str.maketrans('()', '[]'))  # 按照转换规则替换，可添加忽略

# 判断 (可元组匹配) [)
s = 'I love you'
s.startswith('I')   # 判断开头子串
s.endswith('you')   # 判断结束子串
s.istitle()         # 判断每个单词首字母大写
s.isupper()         # 判断每个字符是字母大写
s.islower()         # 判断每个字符是字母小写
s.isalpha()         # 判断每个字符是字母
s.isspace()         # 判断每个字符是空白字符
s.isprintable()     # 判断每个字符是可打印字符
s.isalnum()         # 判断每个字符是数字（各种数字）
s.isidentifier()    # 判断是否为合法标识符
__import__('keyword').iskeyword('if')   # 判断是否为关键字

# 截取
s = '     I love you     '
s.lstrip()          # 左侧不留白
s.rstrip()          # 右侧不留白
s.strip()           # 左右不留白， 默认去除空白,参数匹配字符
s.removeprefix('')    # 删除指定前缀， 参数匹配字符串
s.removesuffix()    # 删除指定后缀， 参数匹配字符串

# 拆分、拼接
s = 'I love you'
s.partition(' ')    # 以分割符为界分割为三元组（包括分隔符）
s.rpartition(' ')   # 同上反向
s.split()           # 按照参数切分成list，默认分割全部，可指定分割次数
s.rsplit()          # 同上反向
s.splitlines()      # 按行分割，默认不包括换行符
' '.join(['I', 'love', 'you'])  # 根据字符串拼接一个可迭代对象

# 格式化字符串
s = 'I love {}'.format('you')
# 参数中的字符会当作元组来对待，{}中为下表索引
s = '1+2={0}, 2^2={1}, 3^3={2}'.format(1+2, 2*2, 3**3)
s = '我叫{name}, 我爱{fav}'.format(name='王', fav='喊66')    # 可以使用关键字参数
s = '{:^10}'.format(6)          # ^居中
s = '{:>10}'.format(6)          # >右对齐
s = '{:<10}'.format(6)          # <左对齐
s = '{:010}'.format(6)          # 0填充，只对数字
s = '{:%>10}'.format(6)         # 任意字符填充
s = '{:+}{:-}'.format(6, -6)    # 数字前加符号
s = '{:,}'.format(123456)       # 千分位分割
s = '{:.2f}'.format(3.14)       # 小数点后几位
s = '{:.2g}'.format(3.14)       # 小数点前后共几位
s = '{:.2}'.format('666')       # 非数字截取功能
s = '{:.2}'.format(666)         # 不允许

# b——二进制显示     c——Unico编码显示    d——十进制   o——八进制   xX——十六进制 （#——追加前缀）
# eE——科学记数法默认精度为6     fF——定点表示法默认精度为6无穷'inf'  gG——通用格式小数f大数e
# 大小写只区分显示大小写    %——f*100显示后带%   n——同g添加适当的分隔符
# 可任意混合并且以参数传入
# f-string '{}'.format(6) == f'{6}'
s = f'{3.1415:+^10.3g}'
