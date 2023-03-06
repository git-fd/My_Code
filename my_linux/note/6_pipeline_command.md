## pipeline(`|`) and command

### pipeline

- **概念**
    类似文件重定向，可以将一个前一个命令的`stdout`重新定向到下一个命令的`stdin`

- **要点**
  - 管道命令仅处理`stdout`，会忽略`stderr`
  - 管道右边的命令必须能接受`stdin`
  - 多个管道命令可以串联

- **与文件重定向的区别**
  - 文件重定向左边为命令，右边为文件
  - 管道左右两边均为命令，左边有`stdout`，右边有`stdin`

- **示例**
    统计当前目录所有`python`文件的总行数

        find . -name *.py | xargs cat | wc -l

### command

- **系统状态**
  - **`top`**：查看进程信息(任务管理器)
    - `M`：按照内存占用排序
    - `P`：按照CPU占用排序
    - `q`：退出
  - **`df -h`**：查看硬盘信息
  - **`free -h`**：查看内存使用情况
  - **`du -sh`**：常看当前目录占用磁盘空间
  - **`ps aux`**：查看所有进程
  - **`kill -9 pid`**：杀死编号为`pid`的进程
  - **`netstat -nt`**：查看所有的网络连接
  - **`w`**：列出当前登录用户
  - **`ping www.baidu.com`**：检查是否联网

- **文件权限**
  - **`chmod`**：修改文件权限
    - `r`：读权限，二进制第一位
    - `w`：写权限，二进制第二位
    - `x`：执行权限，二进制第三位
    - **`chmod +x xxx`**：给`xxx`增加可执行权限
    - **`chmod -x xxx`**：去掉`xxx`的可执行权限
    - **`chmod 777 xxx`**：给`xxx`增加所有用户的所有权限(数字分别对应为`作者,同组,其他人`权限三位二进制的十进制数字)

- **文件检索**
  - **`find path -name *.py`**：搜索`path`路径下的`.py`文件
  - **`grep xxx`**：`stdin`读取，若某行包含`xxx`则输出该行，否则忽略
  - **`wc`**：统计行数、单词数、字节数(`stdin`读取，也可以从命令行参数中传入文件名列表)
    - **`wc -l`**：统计行数
    - **`wc -w`**：统计单词数
    - **`wc -c`**：统计字节数
  - **`tree`**：展示当前文件目录结构
    - **`tree -a ~`**：展示家目录下所有文件的结构
  - **`ag xxx`**：搜索当前目录下所有文件，检索`xxx`字符串
  - **`cut`**：`stdin`读取
    - **`echo $PATH | cut -d ':' -f 3,5`**：输出`PATH`用`:`分割`3、5`列数据
    - **`echo $PATH | cut -d ':' -f 3-5`**：输出`PATH`用`:`分割`3-5`列数据
    - **`echo $PATH | cut -c 3,5`**：输出`PATH`的`第3、5`个字符
    - **`echo $PATH | cut -c 3,5`**：输出`PATH`的`第3-5`个字符
  - **`sort`**：将每行内容按照字典序排序(`stdin`and命令行参数)
  - **`xargs`**：将`stdin`中的数据根据空格或者回车分割为命令行参数

- **查看文件内容**
  - **`more`**：浏览文件内容
    - **`回车`**：下一行
    - **`空格`**：下一页
    - **`b`**：上一页
    - **`q`**：退出
  - **`less`**：与`more`相似，功能更全
    - **`回车`**：下一行
    - **`y`**：上一行
    - **`Page Down`**：下一页
    - **`Page Up`**：上一页
    - **`q`**：退出
  - **`head -3 xxx`**：显示`xxx`的前3行(`stdin`)
  - **`tail -3 xxx`**：显示`xxx`的末3行(`stdin`)

- **工具**
  - **`md5sum`**：计算`md5`哈希值(`stdin`and命令行参数传入文件名)
  - **`time command`**：统计`command`执行时间
  - **`tar`**：压缩文件
    - **`tar -zcvf xxx.tar.gz /path/to/file/*`**：压缩
    - **`tar -zxvf xxx.tar.gz`**：解压缩
  - **`diff xxx yyy`**：查找文件`xxx`和`yyy`不同的地方

- **安装软件**
  - **`sudo command`**：以`root`身份执行`command`
  - **`apt-get install xxx`**：安装`xxx`
  - **`apt-get update`**：更新软件包
  - **`pip install xxx --user --upgrade`**：安装`python`包
