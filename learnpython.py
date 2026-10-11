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

