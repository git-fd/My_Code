-- 数据定义语言：定义或改变表的结构


-- 创建表
/*
CREATE TABLE test (

字段名1（列名） 类型（宽度） 约束条件，     
字段名2 类型（宽度）约束条件，
........

)
-- 整形
    tinyint         1字节
    smallint        2字节
    mediumint       3字节
    int             4字节
    bigint          8字节
宽度配合zerofill使用 列如：int(4) UNSIGNED zerofill, 查询结果为 0001，0002

-- 浮点型
    float(m, d)     4字节，单精度，m总长，小数位
    double(m, d)    8字节，双精度
    decimal(m, d)   存储字符串的浮点数，对应java中的Bigdecimal
对于float(5, 3)  插入123.45678 得到99.999， 插入12.34567 得到12.346

-- 字符串数据类型
    char(n)         固定长度，最多255B
    varchar(n)      可变长度，最大64KB
    tinytext        可变长度，最大255B
    text            可变长度，最大64KB
    mediumtext      可变长度，最大16MB
    longtext        可变长度，最大4GB
n 代表字符的个数，并不代表字节个数，比如 char(30) 就可以存储 30 个字符

-- 日期时间数据类型
    date            3字节，日期，格式xxxx-xx-xx
    time            3字节，时间，格式xx:xx:xx
    datetime        8字节，日期时间，格式xxxx-xx-xx xx:xx:xx
    timestamp       4字节，自动存储记录修改时间 时间戳
    year            1字节，年份
*/

