### python3学习笔记

### 1、pyhon3的所有的常用的语法


​	1）、python 下载地址 http://www.python.org

​			python是一门脚本语言，

​				a、语法和结构比较简单

​				b、通常以容易修改程序的“解释”作为运作方式，而不需要“编译”

​				c、程序的开发产能由于运行性能

​	2）、用IDLE 编译python Shell 是键入python语言文本和程序交互的途径

​	3）、>>>print("hello world"*5)是正确的指令,而>>>print(" hello world"+5)报错

​			因为python不支持把完全不同的语言加在一起

​	4)、python支持\,可以用\",\n等转义字符.

​	 键：Alt+n  回到上一个语句，alt+p发到下一条语句	

​	python语法:

​		python中没有大括号的,python中的缩进很重要,缩进写错会引起程序执行失败.

​		python里面变量是没有类型的区分

​	python的内置函数BIF:

​		python 查看内置函数的方法：

​		直接输入:

```py
			dir(__builtins__)
```

​		或者引入builtins模块

```python
			import builtins
			dir(builtins)
			/**查看长度*/
			len(dir(__builtins__))
			/**遍历内置函数列表,(注意空格,按两次回车显示内容)*/
			for item in dir(__builtins__):
    			print(item)
```



​			input:内容会显示到桌面上,并且要求用户输入一个值;

​			int:将变量变为一个整型

​		python的变量使用：

​			1、python在使用变量之前，需要对其先赋值。

​			2、变量名可以包括字母，数字，下划线，但变量名不能以数字开头

​			3、字母可以是大写或者小写，但是大小写是不同的

​			4、变量名尽量语义化

​		pyhton的字符串：

​			python字符串包含在单引号或者双引号之间

​				原始字符串：

​			在普通字符串前面加上一个r就行

​				例如：str = 'c:\now'

​					在print(str) 时 \n会转义成换行符号,

​			可以使用`str = 'c:\\now`来代替或者使用原始符号代替

​				str = r'c:\now'

​			字符串的换行:三重引号字符串

​					例如:

						
						str = """ python 
								好耶,
								好屌"""
​			引入随机random模块

​				rabdom模块里面会有一个randint()函数,会返回一个随机的整

```py
				import random
				random.randint(1,10)
				temp = input('guess number')
				guess = int(tem)
					n=1
				while guess !=anwser and n<3:

```

#### pythom的数据类型

​	整型:整数型,转换的方法int(),会将一个数字的字符串,或者浮点型直接去掉后面的小		    数点,向下取整.

​	浮点型:带小数点 ,转换方法 float()

​	布尔值:True 和 False,python中能看做是False的是 False None 0 "" '' () [] {};

​	字符串:引号括住的文字,多行字符串的话需要用"""  """" 包含住,将一个对象转换为字符串 str()

​	获取变量的数据类型

​		type()

​		推荐使用

​			isinstance()

#### 2、面向对象的编程思维

#### 3、运用模块进行变成

#### 4、游戏编程

#### 5、计算机仿真

