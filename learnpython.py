###################--------day1--------###################

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(a)
# print(b)


# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Bob!'''

# print(n, f, s1, s2, s3, s4)
# print(n,end=',\n')
# print(f,end=',\n')
# print(s1,end=',\n')
# print(s2,end=',\n')
# print(s3,end=',\n')
# print(s4,end=',\n')

# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

# s1 = 72
# s2 = 85
# r = (s2-s1)/s1 * 100
# print(f"成绩的提升概率是{r:.2f}%。")

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

# birth = input('birth: ')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# height, weight = int(input('height: ')), float(input('weight: '));
# BMI = weight / (height/100) ** 2
# if BMI < 18.5:
#     print('过轻')
# elif BMI < 25:
#     print('正常')
# elif BMI < 28:
#     print('过重')
# elif BMI < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print(name);

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

'''
Key 必须可哈希，但 Value 可以是任何东西（包括列表、字典甚至另一个字典）,
列表、字典、集合这些可以改变的类型,都不能作为字典的key,因为它们是不可哈希的。
'''

'''
dict 是“键值对”的集合，而 set 是“只有键，没有值”的字典。
dict（字典）：存储的是 Key : Value（键值对）。你需要通过键来找到对应的值。
d = {'name': '张三', 'age': 18}
# 'name' 是键，'张三' 是值
set（集合）：只存储 Key（元素），没有值。它其实就是一堆唯一元素的集合。
s = {'张三', 18, '李四'}
# 里面只有元素，没有键值对应关系
'''
###################--------day2--------###################

# x = float('123.456789')
# print(x)

# n1 = 255
# n2 = 1000
# x1, x2 = hex(n1), hex(n2)
# print(x1, x2)

# a = int(input("请输入一个整数："))
# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(a))
# import math
# def quadratic(a, b, c):
#     delta = b ** 2 - 4*a*c
#     if delta < 0:
#         print("方程无实数解")
#     elif delta == 0:
#         x1 = x2 = -b/(2*a)
#         return x1,x2
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return x1,x2
# a,b,c = int(input("请输入二次方程的系数a: ")), int(input("请输入二次方程的系数b: ")), int(input("请输入二次方程的系数c: "))

# x1, x2 = quadratic(a, b, c)
# print(f"方程的解为：x1 = {x1}, x2 = {x2}")

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


# def mul(a, b = 6, *args):
#     s = a * b
#     for v in args:
#         s *= v
#     return s
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# a = fact(1)
# b = fact(5)
# c = fact(100)
# d = fact(1000)
# print(a, '\n', end='')
# print(b, '\n', end='')
# print(c, '\n', end='')
# print(d, '\n', end='')

'''
想象你在一栋大楼里找领导签字：

你（Frame 3）拿着文件，去找经理（Frame 2）。

经理说：“你先去拿财务（Frame 1）的盖章”。

财务盖完章（返回 1），经理才愿意签字（返回 2），你才能拿回文件（返回 6）。

栈帧，就是你在敲门时，把当前手里的文件“存”在门外的那个动作。等你拿到下一级的结果出来，你再从门外的文件里，继续往下写
'''

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         print(a, '-->', c)
#         move(n - 1, b, a, c)
# move(3, 'A', 'B', 'C')

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n >= 2:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#     else:
#         return 0

# print(fibonacci(10))

###################--------day3--------###################

# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s

# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None, None)
#     else:
#         min = L[0]
#         max = L[0]
#         for i in range(len(L)):
#             if L[i] < min:
#                 min = L[i]
#             elif L[i] > max:
#                 max = L[i]
#         return (min, max)


# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

'''
循环：代码里写了 for 或 while。

迭代：把一筐苹果一个个拿出来洗干净的过程。

递归：不用循环，靠函数自己喊自己，也能把苹果一个个洗了。

死循环：一直在洗同一个苹果，或者苹果洗完了还在洗空气（无限重复，没有推进，这叫“循环”，但不叫“迭代”，因为迭代必须有“逐步推进”的含义）。
'''

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]

# # 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

'''
列表：像一张写满数据的纸。你拿到手里，想怎么看就怎么看，想翻几次就翻几次，但纸很大，拿着很沉。

生成器：像一个会算数的秘书。你问她“下一个是多少？”，她算一下告诉你。你不问她就不算，而且她只记当前算到哪了，绝不在脑子里记住所有算过的数字。你问完一遍，她就不记得前面算过什么了（不能回头问）。
'''
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1] 

# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# # 第一个循环模拟：t 最后变成了最后一行
# t = [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# print("第一个循环结束后，t 的值是：", t)

# # results 就是一个大箱子
# results = [[1], [1, 1], [1, 2, 1]]

# # 第二个循环
# for t in results:
#     print("现在的 t 是：", t)

'''
普通函数：像你去找一个只会背书的学生。每次你问他“背第5首古诗”，他都要从第1首开始背，背到第5首给你听，然后立刻失忆。你下次问他第6首，他又从第1首开始背。

生成器（带 yield 的函数）：像你去找一个正在背书的学生。他背到第5首时，你说“停”，他就停在那里（保存了现场）。你去干别的事，回来跟他说“继续”，他从第6首接着背，不用从头再来。

迭代器（普通迭代器）：像一本印好的书，你只是放了个书签在里面，翻一页看一页，书的内容本身不变。
'''
# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-5, 6, abs))

'''
一、 什么是 Iterable（可迭代对象）？
定义：只要一个对象内部实现了 __iter__ 方法，它就是 Iterable。
通俗理解：凡是能用 for x in 它: 来遍历的东西，都是可迭代对象。
例子：列表 []、元组 ()、字符串 ''、字典 {}、集合 set()。

它的核心特点：
Iterable 自己没有记忆。它就像一筐苹果，你可以拿出一个啃一口，但筐本身不知道你啃到哪个了。
如果你写 for x in [1, 2, 3]: 循环两次，它会老老实实把 [1, 2, 3] 遍历两遍（因为每次 for 都会帮它重新生成一个迭代器）。

二、 什么是 Iterator（迭代器）？
定义：只要一个对象同时实现了 __iter__ 和 __next__ 方法，它就是 Iterator。
通俗理解：既能被 for 遍历，又能用 next() 一个一个取值的对象。
例子：iter([1, 2, 3]) 的返回值、生成器 (x for x in range(3))、带 yield 的函数返回的生成器。

它的核心特点：
Iterator 内部有状态记忆。它知道“我当前走到哪了”。它就像书签，翻一页就往后挪一格，并且不能回头（除非重新生成一个新的迭代器）。
'''
# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# print(reduce(fn, [1, 3, 5, 7, 9]))

# def normalize(name):
#     if not name:        # 如果字符串为空，直接返回（防止报错）
#         return name
#     return name[0].upper() + name[1:].lower()

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce

# def prod(L):
#     def multiply(x, y):
#         return x * y
#     return reduce(multiply, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

from functools import reduce

# def str2float(s):
#     def multiply(x, y):
#         return x * 10 + y
    
#     def char2num(c):
#         return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]
    
#     # 用 split 拆分整数和小数部分
#     parts = s.split('.')
    
#     # 整数部分
#     a = reduce(multiply, map(char2num, parts[0]))
    
#     if len(parts) == 1:
#         return a  # 没有小数点
    
#     # 小数部分
#     b = reduce(multiply, map(char2num, parts[1])) / (10 ** len(parts[1]))
#     return a + b

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def is_palindrome(n):
#     s = str(n)
#     reversed_s = s[::-1]
#     return s == reversed_s

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)





