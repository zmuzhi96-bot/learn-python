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

def fibonacci(n):
    if n == 1:
        return 1
    elif n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 0

print(fibonacci(10))
