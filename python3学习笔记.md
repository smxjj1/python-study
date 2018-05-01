### python3学习笔记

### 1、pyhon3的所有的常用的语法


​	1）、python 下载地址 http://www.python.org

​			python是一门脚本语言，

​				a、语法和结构比较简单

​				b、通常以容易修改程序的“解释”作为运作方式，而不需要“编译”

​				c、程序的开发产能由于运行性能

​				d、python的源码默认使用utf-8编码，支持中文变量名

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

```python
myString.isalnum()#所有字符是否是数字或者字母
myString.isalpha()#所有的字符是否是字母
myString.isdigit()#所有的字符是否为数字
myString.islower()#所有的字符是否都是小写
myString.isupper()#所有的字符都是大写
myString.istitle()#所有的单词是否首字母大写
myString.isspace()#所有的字符是否都是空白字符
```



​	获取变量的数据类型

​		type()

​	推荐使用

​		isinstance()

  	判断一个变量是不是数字的方法: isdigit()

​								while not temp.isdigit()

##### python算术操作符

​	python3中的整数除法，

​		//（表示双除号）会取地板除法，即得到的结果会向下取整。

​		/（表示一个除号），正常的除法

​		比较运算符的优先级大于逻辑运算符

```python
例如3<4 and 8>9 可以写成 (3<4) and (8>9)
幂运算和一元操作符的优先级:幂运算比左侧的一元操作符优先级高,例如-3**2=-9;比右侧的一元操作符低 例如 3**-2 = 0.1111111111111111,即3^(-2)次方
 **表示幂运算,3**2 == 3*3
```

```python
逻辑操作符
	and(与) not(非) or (或)
    优先级:not>and>or
    3<4<5===(3<4) and (4<5)
```

优先级:幂运算>正负号>算术运算符>比较运算符>逻辑运算符

##### python中分支和循环语句

​	打飞机小游戏的组成和结构：

```python
#加载背景音乐
#播放背景音乐(设置单曲循环)
#我方飞机诞生
intervar = 0 (设置小飞机加载的间隔,不然的话小飞机会出现的太多)
while True:
    if #用户是否点击关闭按钮
    	#退出程序
    interval+=1
    if interval==50:
        interval=0
        #小飞机诞生
    #小飞机移动一个位置
    #屏幕刷新
    if:#用户鼠标产生移动
        #我方飞机中心位置 = 用户鼠标位置
        #屏幕刷新
    if:#我方飞机与小飞机碰撞
        #我放飞机挂掉,播放装机音乐
        #修改我方飞机图案
        #显示游戏借宿
        #渐渐关闭音乐
```

####python中的条件表达式

​	三元操作符

```python
x , y  =  4, 5
if x < y:
    small = x
else:
    small = y
 #改为三元操作符
small = x if x < y else y
#assert断言
	当这个关键字后边的条件为假的时候，程序会
    自动崩溃并抛出AeertionError的异常
		flag = True
		temp = input("input your order")
		if temp=="1":
    		print(type(temp))
		else:
    		flag = False
		assert flag
		print('I am behind assert,hahaha')
```

#### while循环

```python
#break循环会跳出循环体
bingo = "草拟吗，楼上钻你妈坟头呢？"
answer = input('请输入现在最想说的话')
while True:
    if answer == bingo:
        break
    answer = input("骂的不爽，再来！！！")
print("傻逼玩意，半夜钻墙")
#continue会跳出本次循环,执行下一次循环
for i in range(10):
    if i%2= 0:
        print(i)
        continue
    i+=2
    print(i)
```



#### for循环

```python
#example one
forString = "ayada heheh balabala"
newString = ""
for i in forString:
    if i ==" ":
        i=""
    newString +=i+"+"
print(len(newString))#显示字符串的长度
#example two
myArray = ["one","mo\'ijo","smxjj","daji","lover is dreamer","laogou"]
for item in myArray:
    print(item)
#for循环和range方法
#range方法默认有三个参数,(startnum,endnum,step)
#起始位置,结束位置,步长
for i in range(10):
    print(i)

```

####python列表

##### 创建列表

```python
member = ["逗比","sayHello","minx",3.15415,["heheh"],{"first":'ggg'}]
for item in member:
    print(item)
#添加元素
member.append("isallright,这只能加一个元素")
member.extend(["gogo","卧槽啊,这要添加一个参数"])
```









​		

​	

#### 2、面向对象的编程思维

#### 3、运用模块进行变成

#### 4、游戏编程

#### 5、计算机仿真

