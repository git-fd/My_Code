# Markdown 语法

## 0. 目录

```
[TOC]
```

显示效果:

[TOC]

## 1. 斜体,粗体,删除线,高亮

```
*斜体*
**粗体**
***加粗斜体***
~~删除线~~
==高亮==
```

显示效果:

*这是斜体*
**这是粗体**
***这是加粗斜体***
~~这是删除线~~
==这是高亮==

## 2. 分级标题

```
# 一级标题
## 二级标题
### 三级标题
......
```

## 3. 超链接

### 3.1 行内式

```
[这是百度](https://www.baidu.com/)
```

显示效果:

[这是百度](https://www.baidu.com/)

### 3.2 参考式

```
[这是百度][1]
[这是acwing][2]
[这是pta][]

[1]:http://www.baidu.com/
[2]:http://www.acwing.com/
[这是pta]:https://pintia.cn/
```

显示效果:

[这是百度][1]
[这是acwing][2]
[这是pta][]

[1]:http://www.baidu.com/
[2]:http://www.acwing.com/
[这是pta]:https://pintia.cn/

### 3.3 自动链接

```
<http://www.baidu.com/>
<1397818213@qq.com>
```

显示效果:

<http://www.baidu.com/>
<1397818213@qq.com>

## 4. 锚点

```
跳转到[目录](#0-目录)
```

显示效果:

跳转到[目录](#0-目录)

## 5. 列表

### 5.1 无序列表

```
- 无序列表一
- 无序列表二
- 无序列表三
```

显示效果:

- 无序列表一
- 无序列表二
- 无序列表三

### 5.2 有序列表

```
1. 有序列表一
2. 有序列表二
3. 有序列表三
```

显示效果:

1. 有序列表一
2. 有序列表二
3. 有序列表三

### 5.3 定义型列表

```
Markdown
:   轻量级文本标记语言
```

显示效果:

Markdown
:   轻量级文本标记语言

### 5.4 包含引用的列表

```
* 阅读的方法:
    > 打开书本。
    > 打开电灯。
```

显示效果:

- 阅读的方法:
    > 打开书本。
    > 打开电灯。

### 5.5 包含代码块的列表

```
- 代码块

        <代码写这里>
```

显示效果:

- 代码块

        #include <iostream>
        int main() {
            std::cout << "Hello, World!!!" << std::endl;
            return 0;
        }

### 5.6 任务列表

```
- [ ] 吃饭
- [ ] 睡觉
- [x] 打豆豆
```

显示效果:

- [ ] 吃饭
- [ ] 睡觉
- [x] 打豆豆

## 6. 引用

```
> 这是一个有两段文字的引用
>
> 占行文字1
> 占行文字2
>
> 占行文字3
> 占行文字4
```

显示效果:

> 这是一个有两段文字的引用
>
> 占行文字1
> 占行文字2
>
> 占行文字3
> 占行文字4

### 6.1 引用的多层嵌套

```
> Markdwon怎么学?
>> 自己看教程!
>>> 教程在哪?
```

显示效果:

> Markdwon怎么学?
>> 自己看教程!
>>> 教程在哪?

### 6.2 引用其他要素

```
> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
> 
> 例子代码：
> 
>     sudo rm /* -rf
```

显示效果:

> 1. 这是第一行列表项。
> 2. 这是第二行列表项。
>
> 例子代码：
>
>     sudo rm /* -rf

## 7. 图像

### 7.1 行内式

```
头像:
![头像](./res/chinese_youth.jpg)
```

显示效果:

头像:
![头像](./res/chinese_youth.jpg)

### 7.2 参考式

```
头像:
![头像][local]

[local]: ./res/chinese_youth.jpg
```

显示效果:

头像:
![头像][local]

[local]: ./res/chinese_youth.jpg

## 8. 注脚

```
使用Markdown[^1]可以效率书写文档,直接转换成HTML[^2],你可以使用VsCode[^3]进行书写

[^1]: Markdown是一种纯文本标记语言
[^2]: HyperText Markup Language 超文本标记语言
[^3]: Microsoft旗下一款开源多功能编辑器
```

显示效果:

使用Markdown[^1]可以效率书写文档,直接转换成HTML[^2],你可以使用VsCode[^3]进行书写

[^1]: Markdown是一种纯文本标记语言
[^2]: HyperText Markup Language 超文本标记语言
[^3]: Microsoft旗下一款开源多功能编辑器

## 9. LaTeX公式

### 9.1 行内公式

```
勾股定理: $a^2 + b^2 = c^2$
```

显示效果:

勾股定理: $a^2 + b^2 = c^2$

### 9.2 整行公式

```
$$\sum_{i=1}^n a_i=0$$
$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$
$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$
```

显示效果:

$$\sum_{i=1}^n a_i=0$$
$$f(x_1,x_x,\ldots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2 $$
$$\sum^{j-1}_{k=0}{\widehat{\gamma}_{kj} z_k}$$

## 10. 表格

### 10.1 简单方式

```
学号|姓名|分数
-|-|-
1|张三|85
2|李四|60
3|王五|100
```

显示效果:

学号|姓名|分数
-|-|-
1|张三|85
2|李四|60
3|王五|100

### 10.2 原生方式

```
|产品|销量|价格|
|:-|:-:|-:|
|低级|20|100|
|中级|10|200|
|高级|2|1000|
```

显示效果:

|产品|销量|价格|
|:-|:-:|-:|
|低级|20|100|
|中级|10|200|
|高级|2|1000|

## 11. 分割线

```
***
```

显示效果:

***

## 12. 代码

### 12.1 行内式

```
不要执行`sudo rm /* -rf`
```

显示效果:

不要执行`sudo rm /* -rf`

### 12.2 缩进式多行代码

    #include <iostream>

    int main() {
        std::cout << "Hello, World!" << std::endl;
        return 0;
    }

### 12.3 ```包裹的代码

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

```

### 12.4 内联HTML原始码

```
<div>
    <u><font style="color:red">Hello, World!</font></u>
</div>

<table>
    <tr>
        <th rowspan="2">值班人员</th>
        <th>星期一</th>
        <th>星期二</th>
        <th>星期三</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>李四</td>
        <td>王五</td>
    </tr>
</table>
```

显示效果:

<div>
    <u><font style="color:red">Hello, World!</font></u>
</div>

<table>
    <tr>
        <th rowspan="2">值班人员</th>
        <th>星期一</th>
        <th>星期二</th>
        <th>星期三</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>李四</td>
        <td>王五</td>
    </tr>
</table>

## 13. Emoji表情

```
:sweat_smile:
:drooling_face:
:clown_face:
```

显示效果:

:sweat_smile:
:drooling_face:
:clown_face:
