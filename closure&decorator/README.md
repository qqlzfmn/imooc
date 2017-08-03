# 闭包 closure 和装饰器 decorator
### 一、LEGB 原则
L > E > G > B

|字母|含义|作用域|
|---:|---:|------|
|L|local|函数内部作用域|
|E|enclosing|函数内部及内嵌函数之间|
|G|global|全局作用域|
|B|build_in|内置作用域|

### 二、闭包
闭包是内部函数对enclosing作用域的变量的使用，可实现代码复用，减少代码量  

闭包内层函数实现相同功能的部分  
不同的参数、属性、功能通过外层函数传递进来  
实现想要的逻辑之后外层函数返回一个函数

---
* 例 1 ：


    def set_passline(passline):
        def cmp(val):
            if val >= passline:
                print('Pass')
            else:
                print('Failed')
    
        return cmp

这里内层函数 cmp 实现判断是否及格  
外层函数传入及格线是多少分  
当执行如下这条语句后

    f_100 = set_passline(60)

f_100 就是一个当 passline = 60 的时候的 cmp 函数  
所以可以进行下面这句操作

    f_100(89)

---
* 例 2 ：  


    def dec(func):
        def in_dec(*args):
            if len(args) == 0:
                return 0
            for arg in args:
                if not isinstance(arg, int):
                    return 0
            return func(*args)
    
        return in_dec
    
    
    def my_sum(*args):
        return sum(args)

这里内层函数 in_dec 实现判断传入的参数是否是整数且数量大于0
外层函数传入一个求和函数
当执行如下这条语句后

    my_sum = dec(my_sum)

my_sum 就是一个含有判断功能的 my_sum 函数  
所以可以进行下面这句操作而不报错

    print(my_sum(1, '2', 3, 4, 5))

注：这个例子里的 *args 是一个不定长参数，可以接收任意个变量  
**当传入外层函数的参数变为函数的时候，该闭包就是一个装饰器**

### 三、装饰器
**装饰器的实质就是对闭包的使用**
* 例：下面两个代码段是等价的


    def dec(func):
        def in_dec(*args):
            if len(args) == 0:
                return 0
            for arg in args:
                if not isinstance(arg, int):
                    return 0
            return func(*args)
    
        return in_dec
    
    
    @dec  # 使用装饰器语法糖
    def my_sum(*args):
        return sum(args)

---

    def dec(func):
        def in_dec(*args):
            if len(args) == 0:
                return 0
            for arg in args:
                if not isinstance(arg, int):
                    return 0
            return func(*args)
    
        return in_dec
    
    
    def my_sum(*args):
        return sum(args)
    
    
    my_sum = dec(my_sum)  # 使用调用闭包的方法

注： 使用了”@”语法糖后，我们就不需要额外代码来给”my_sum”重新赋值了，其实”@dec”的本质就是”my_sum = dec(my_sum)”，当认清了这一点后，后面看带参数的装饰器就简单了。

---
* 抽象


    def deco(func):
        def in_deco(x, y):
            print('in deco')
            func(x, y)
    
        print('call deco')
        return in_deco
    
    
    @deco
    def bar(x, y):
        print('in bar')
        print(x + y)
    
    
    bar(1, 2)

当调用 bar(1, 2) 的时候 Python 解释器都做了什么：
1. @deco
    1. deco(bar)
    2. print('call deco')
    3. return in_deco
2. bar(1, 2)
    1. in_deco(1, 2)
    2. print('in deco')
3. print('in bar')
4. print(x + y)

