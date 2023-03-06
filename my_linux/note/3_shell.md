
## shell语法

### 概述

`shell`是我们通过命令行与操作系统沟通的语言

`shell`脚本可以直接在命令行中执行，也可以将一套逻辑组织成一个文件，方便复用
`Terminal`中的命令行可以看成是一个`shell`脚本在逐行执行

`Linux`中常见的`shell`脚本有很多种，常见的有：

- Bourne Shell(`/usr/bin/sh`或`/bin/sh`)
- Bourne Again Shell(`/bin/bash`)
- C Shell(`/usr/bin/csh`)
- K Shell(`/usr/bin/ksh`)
- ......

Linux系统中一般默认使用bash，所以接下来讲解bash中的语法。
文件开头需要写`#! /bin/bash`，指明bash为脚本解释器

- **新建.sh文件示例**

        #! /bin/bash
        echo "Hello World!"

- **运行方式**

        chmod +x name.sh    # 增加可执行权限
        ./name.sh           # 执行name.sh文件

        bash name.sh        # 解释器执行

### 注释

```bash
echo Hello World    # 单行注释

:<<!
多行注释
多行注释
!
```

### 变量

- **定义**

        a=123
        b=abc
- **使用**

        echo $a         # 输出123
        echo ${a}       # 同上
        echo ${a}4      # 输出1234
- **只读变量**

        readonly b      
        declare -r b    # 两种写法均可

        b=123           # 报错b为只读
- **删除变量**

        unset b
        echo $b         # 输出空行
- **变量类型**
  - 自定义变量(局部变量)
  - 环境变量(全局变量)
  - 局部转全局

        x=666
        export x        # 方法一
        declaer -x x    # 方法二
  - 全局转局部

        export x=666    # 定义环境变量
        declaer +x x    # 改为自定义变量
- **字符串**

        x=world
        echo 'hello, $x \"hh\"'     # 单引号字符串输出 hello, $name \"hh\"  # 原样输出,不执行,不取变量
        echo "hello, $x \"hh\""     # 双引号字符串，输出 hello, world "hh"  
        echo ${#x}                  # 获取字符串长度
        echo ${x:0:3}               # 提取子串从0开始3个字符

### 默认变量

- **文件参数变量**

        $1, $2, ...         # 向脚本传入的参数
        $0                  # 包含路径的文件名

- **其他参数**
    参数|说明
    -|-
    `$#`|文件传入参数的个数
    `$*`|由所有参数构成的用空格隔开的字符串，`"$1 $2"`
    `$@`|每个参数分别用双引号括起来的字符串，`"$1" "$2"`
    `$$`|脚本当前运行的进程ID
    `$?`|上一条命令的退出状态，0表示正常退出，其他值表示错误
    `$(command)`|返回command这条命令的stdout(可嵌套)
    `` `command` ``|返回command这条命令的stdout（不可嵌套）

### 数组

```bash
arr=(1, abc, xx, 3)  # 定义，无大小要求
arr[9]=9             # 任意位置赋值
${arr[index]}        # 调用格式
${arr[@]}            # 读取整个数组 法一
${arr[*]}            # 法二
${#arr[@]}           # 读取数组长度 法一
${#arr[*]}           # 法二 
```

### expr 命令

- **说明**
  - 用空格隔开每一项
  - 用反斜杠放在shell特定的字符前面（发现表达式运行错误时，可以试试转义）
  - 对包含空格和其他特殊字符的字符串要用引号括起来
  - expr会在`stdout`中输出结果。如果为逻辑关系表达式，则结果为真，`stdout`为1，否则为0
  - expr的`exitcode`：如果为逻辑关系表达式，则结果为真，`exitcode`为0，否则为1

- **字符串表达式**
  - `length STRING` 返回`STRING`的长度
  - `index STRING CHARSET`  
  `CHARSET`中任意单个字符在`STRING`中最前面的字符位置，下标从1开始。如果在`STRING`中完全不存在`CHARSET`中的字符，则返回0
  - `substr STRING POSITION LENGTH`  
  返回`STRING`字符串中从`POSITION`开始，长度最大为`LENGTH`的子串。如果`POSITION`或`LENGTH`为负数，0或非数值，则返回空字符串
  - 示例

        str="Hello World!"

        echo `expr length "$str"`        # ``不是单引号，表示执行该命令，输出12
        echo `expr index "$str" aWd`     # 输出7，下标从1开始
        echo `expr substr "$str" 2 3`    # 输出 ell

- **整数表达式**
  - `+ -` 加减运算。两端参数会转换为整数，如果转换失败则报错
  - `* / %` 乘，除，取模运算。两端参数会转换为整数，如果转换失败则报错
  - `()` 可以改变优先级，但需要用反斜杠转义
  - 示例

        a=3
        b=4

        echo `expr $a + $b`     # 输出7
        echo `expr $a - $b`     # 输出-1
        echo `expr $a \* $b`    # 输出12，*需要转义
        echo `expr $a / $b`     # 输出0，整除
        echo `expr $a % $b`     # 输出3
        echo `expr \( $a + 1 \) \* \( $b + 1 \)`  # 输出20，值为(a + 1) * (b + 1)

- **逻辑关系表达式**
  - `|`
  如果第一个参数非空且非0，则返回第一个参数的值，否则返回第二个参数的值，但要求第二个参数的值也是非空或非0，否则返回0。如果第一个参数是非空或非0时，不会计算第二个参数
  - `&`
  如果两个参数都非空且非0，则返回第一个参数，否则返回0。如果第一个参为0或为空，则不会计算第二个参数
  - `< <= = == != >= >`
  比较两端的参数，如果为true，则返回1，否则返回0。”==”是”=”的同义词。”expr”首先尝试将两端参数转换为整数，并做算术比较，如果转换失败，则按字符集排序规则做字符比较
  - `()` 可以改变优先级，但需要用反斜杠转义
  - 示例

        a=3
        b=4

        echo `expr $a \> $b`    # 输出0，>需要转义
        echo `expr $a '<' $b`   # 输出1，也可以将特殊字符用引号引起来
        echo `expr $a '>=' $b`  # 输出0
        echo `expr $a \<\= $b`  # 输出1

        c=0
        d=5

        echo `expr $c \& $d`  # 输出0
        echo `expr $a \& $b`  # 输出3
        echo `expr $c \| $d`  # 输出5
        echo `expr $a \| $b`  # 输出3

### read 命令

`read`命令用于从标准输入中读取单行数据。当读到文件结束符时，`exitcode`为1，否则为0

- **参数说明**
  - `-p` 后面可以接提示信息
  - `-t` 后面跟秒数，定义输入字符的等待时间，超过等待时间后会自动忽略此命令
- **示例**

        read name
        read -p "Please input your name: " -t 30 name

### echo 命令

- **`echo`用于输出字符串**

        echo "Hello World"
        echo Hello World                # 引号可以省略
        echo "\"Hello AC Terminal\""    # 注意只能使用双引号，如果使用单引号，则不转义
        cho \"Hello AC Terminal\"       # 也可以省略双引号
        str="Hello, World"
        echo $str                       # 输出变量
        echo -e "Hi\n"                  # 显示换行
        echo -e "Hi\c"                  # 显示不换行
        echo '$str\"'                   # 原样输出 $str\"
        echo `date`                     # 显示命令的执行结果
- **输出重定向**

        echo Holle, World > output.txt      # 将内容以覆盖的方式输出到output.txt

### printf 命令

`printf`命令用于格式化输出，类似于`C/C++`中的`printf`函数 默认不会在字符串末尾添加换行符

- **示例**

        printf "%10d.\n" 123                        # 占10位，右对齐
        printf "%-10.2f.\n" 123.123321              # 占10位，保留2位小数，左对齐
        printf "My name is %s\n" "yxc"              # 格式化输出字符串
        printf "%d * %d = %d\n"  2 3 `expr 2 \* 3`  # 表达式的值作为参数

### test and []

- **逻辑运算符&&和||**
  - `&&` 表示`与`, `||`表示`或`
  - 均具有短路逻辑

        expr1 && expr2: 当expr1为假时，直接忽略expr2
        expr1 || expr2: 当expr1为真时，直接忽略expr2
  - 表达式的`exitcode`为0，表示真；为非零，表示假。（与`C/C++`中的定义相反）

#### test

`test`命令用于判断文件类型，以及对变量做比较
`test`命令用`exitcode`返回结果，而不是使用`stdout`; 0表示真，非0表示假

- **文件类型判断**
    测试参数|含义
    -|-
    `-e`|文件是否存在
    `-f`|是否为文件
    `-d`|是否为目录
- **文件权限判断**
    测试参数|含义
    -|-
    `-r`|是否可读
    `-w`|是否可写
    `-x`|是否可执行
    `-s`|是否非空
- **整数之间的比较**
    测试参数|含义
    -|-
    `-eq`|a == b
    `-ne`|a != b
    `-gt`|a > b
    `-lt`|a < b
    `-ge`|a >= b
    `-le`|a <= b
- **字符串比较**
    测试参数|含义
    -|-
    `test -z STRING`|判断STRING是否为空，如果为空，则返回true
    `test -n STRING`|判断STRING是否非空，如果非空，则返回true（-n可以省略）
    `test str1 == str2`|判断str1是否等于str2
    `test str1 != str2`|判断str1是否不等于str2
- **多重条件判定**
    测试参数|含义
    -|-
    `-a`|两条件是否同时成立
    `-o`|两条件是否至少一个成立
    `!`|取反。如 test ! -x file，当file不可执行时，返回true

#### [ ]

`[]`与`test`用法几乎一模一样，更常用于`if`语句中。另外`[[]]`是`[]`的加强版，支持的特性更多

- **注意**
  - `[]`内的每一项都要用空格隔开
  - 中括号内的变量，最好用双引号括起来
  - 中括号内的常数，最好用单或双引号括起来

### 判断语句

类似于`C/C++`中的`if-else`语句

- **`if`**

        a=3
        b=4
        if [ $a -lt $b ]
        then
            echo $a 小于 $b
        fi
- **`if-else`**

        if ! [ $a -lt $b ]
        then
            echo $a 不小于 $b
        else
            echo $a 小于 $b
        fi
- **`if-elif-else`**

        if [ $a -eq 1 ]
        then
            echo $a等于1
        elif [ $a -eq 2 ]
        then
            echo $a等于2
        elif [ $a -eq 3 ]
        then
            echo $a等于3
        else
            echo 不是1, 2, 3
        fi
- **`case...esac`** 类似于`C/C++`中的`switch`语句

        case $b in
            1)
                echo $a 等于 1
                ;;
            2)
                echo $a 等于 2
                ;;
            3)
                echo $a 等于 3
                ;;
            *)
                echo 不是1, 2, 3
                ;;
        esac

### 循环语句

- **`for…in…do…done`**

        for i in a b c      # 依次输出a b c, 每个元素一行
        do
            echo &i
        done           

        for file in `ls`    # 输出当前路径下的所有文件名，每个文件名一行
        do
            echo &file
        done

        for i in `seq 1 10` # 输出1-10
        do
            echo $i
        done

        for i in {a..z}     # 输出a-z
        do
            echo $i
        done
- **`for ((…;…;…)) do…done`**

        for ((i=1; i<=10; i++))     # 输出1-10
        do
            echo $i
        done
- **`while…do…done`**

        while read name             # 文件结束符为Ctrl+d，输入文件结束符后read指令返回false
        do
            echo $name
        done
- **`until…do…done`**

        until [ "${word}" == "yes" ] || [ "${word}" == "YES" ]  # 当输入yes或者YES时结束，否则一直等待读入
        do
            read -p "Please input yes/YES to stop this program: " word
        done

- **`break`** `break`不能跳出`case`语句

        while read name         # 读入非EOF的字符串，会输出一遍1-7
        do
            for ((i=1;i<=10;i++))
            do
                case $i in
                    8)
                        break
                        ;;
                    *)
                        echo $i
                        ;;
                esac
            done
        done
- **`continue`**

        for ((i=1;i<=10;i++))       # 输出1-10中的所有奇数
        do
            if [ `expr $i % 2` -eq 0 ]
            then
                continue
            fi
            echo $i
        done

### 函数

`bash`中的函数类似于`C/C++`中的函数，但`return`的返回值与`C/C++`不同，返回的是`exitcode`，取值为0-255，0表示正常结束

如果想获取函数的输出结果，可以通过`echo`输出到`stdout`中，然后通过`$(function_name)`来获取`stdout`中的结果

函数的`return`值可以通过`$?`来获取

- **返回值**

        func() {
            echo "Hello, World"
            return 10
        }

        func            # 输出Hello, World
        echo $(func)    # 输出Hello, World
        echo $?         # 输出 10
- **输入参数**
        在函数内，`$1`表示第一个输入参数，`$2`表示第二个输入参数，依此类推
        注意：函数内的`$0`仍然是文件名，而不是函数名

        func() {  # 递归计算 $1 + ($1 - 1) + ($1 - 2) + ... + 0
            word=""
            while [ "${word}" != 'y' ] && [ "${word}" != 'n' ]
            do
                read -p "要进入func($1)函数吗？请输入y/n：" word
            done

            if [ "$word" == 'n' ]
            then
                echo 0
                return 0
            fi  

            if [ $1 -le 0 ] 
            then
                echo 0
                return 0
            fi  

            sum=$(func $(expr $1 - 1))
            echo $(expr $sum + $1)
        }

        echo $(func 10)
- **函数内的局部变量**
        可以在函数内定义局部变量，作用范围仅在当前函数内
        可以在递归函数中定义局部变量

        #! /bin/bash

        func() {
            local name=张三
            echo $name
        }

        echo $name      # 没有变量

### exit 命令

`exit`命令用来退出当前`shell`进程，并返回一个退出状态；使用`$?`可以接收这个退出状态
`exit`命令可以接受一个整数值作为参数，代表退出状态: 如果不指定，默认状态值是 0
`exit`退出状态只能是一个介于 0~255 之间的整数，其中只有 0 表示成功，其它值都表示失败

```bash
if [ $# -ne 1 ]  # 如果传入参数个数等于1，则正常退出；否则非正常退出。
    then
    echo "arguments not valid"
    exit 1
else
    echo "arguments valid"
    exit 0
fi
```

### 文件重定向

- 每个进程默认打开3个文件描述符
  - `stdin`标准输入，从命令行读取数据，文件描述符为0
  - `stdout`标准输出，向命令行输出数据，文件描述符为1
  - `stderr`标准错误输出，向命令行输出数据，文件描述符为2

- **重定向命令列表**
    命令|说明
    -|-
    `command > file`|将`stdout`重定向到`file`中
    `command < file`|将`stdin`重定向到`file`中
    `command >> file`|将`stdout`以追加方式重定向到`file`中
    `command n > file`|将文件描述符`n`重定向到`file`中
    `command n >> file`|将文件描述符`n`以追加方式重定向到`file`中
- **输入和输出重定向**

        echo -e "Hello \c" > output.txt     # 将stdout重定向到output.txt中
        echo "World" >> output.txt          # 将字符串追加到output.txt中
        read str < output.txt               # 从output.txt中读取字符串
        echo $str                           # 输出结果：Hello World
- **同时重定向stdin和stdout**
  - test.sh文件

        #! /bin/bash
        read a
        read b
        echo `expr $a + $b`
  - input.txt文件

        2
        3
  - 命令行语句

        ./test.sh < input.txt > output.txt
        cat output.txt

### 引入外部脚本

类似于`C/C++`中的`include`操作，`bash`也可以引入其他文件中的代码

- **格式**

        . filename          # 导入文件
        source filename     # 同上
- **示例**
  - test1.sh

        #! /bin/bash
        name=张三  # 定义变量name
  - test2.sh

        #! /bin/bash
        source test1.sh         # 或 . test1.sh
        echo My name is: $name  # 可以使用test1.sh中的变量
