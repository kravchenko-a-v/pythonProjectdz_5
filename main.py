# #Пешка
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if y2 == y1 + 1 and x2 == x1 + 1:
#     print('Бьёт')
# elif y2 == y1 + 1 and x2 == x1 - 1:
#     print('Бьёт')
# else:
#     print('Не бьёт')
#
# # Треугольник
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a<b+c and b<a+c and c<a+b:
#     print('YES')
# else:
#     print('NO')
#
# # Числа
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a==b!=c or a==c!=b or b==c!=a:
#     print(2)
# else:
#     print(0)
#
# # # Коробки
# #
# # A1 = int(input())
# # B1 = int(input())
# # C1 = int(input())
# # A2 = int(input())
# # B2 = int(input())
# # C2 = int(input())
# #
# # if A1+B1+C1 > A2+B2+C2:
# #     print('Коробку 2 можно разместить в коробку 1')
# # elif A1+B1+C1 > A2+B2+C2:
# #     print('Коробку 1 можно разместить в коробку 2')
# # else:
# #     print('Коробки 1 и 2 равны')
# #
# # if (A1>A2 and B1>B2) or (A1>A2 and C1>C2) or (B1>B2 and C1>C2):
# #     print('Коробку 2 можно разместить в коробку 1')
# # elif (A1<A2 and B1<B2) or (A1<A2 and C1<C2) or (B1<B2 and C1<C2):
# #     print('Коробку 1 можно разместить в коробку 2')
# # else:
# #     print('Коробки 1 и 2 равны')
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a>b:
#     a,b = b,a
# if b>c:
#     b,c = c,b
# if a>b:
#     a,b = b,a
# print(a,b,c)

# a = 1
# while a<=10:
#     print(a)
#     a = a+1

# a = int(input())
# n = int(input())
#
# temp = a
# count = 1
# while count < n:
#     a = a*temp
#     count = count+1
# print(a)

# a = int(input())
#
# count = 2
# while count<a:
#     print(count)
#     count = count+2

# a = int(input())
#
# count = a-1
# while count >=1:
#     if a%count == 0:
#         print(count)
#         break
#     count = count - 1

# a = 16**2
# print(a)

# a = int(input())
#
# count = 2
# while count < a:
#     print(count)
#     count = count + 2

# # Кароль
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if x2 == x1 + 1 and y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
#     print('Бьёт')
# if x2 == x1 - 1 and y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
#     print('Бьёт')
# if x2 == x1  and y2 == y1 + 1 or y2 == y1 - 1:
#     print('Бьёт')
# else:
#     print('Не бьёт')

# # Слон
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# if abs(x1 - x2) == abs(y1 - y2):
#     print('da')
# else:
#     print('no')

# s = 'python'
# for i in range (len(s)):
#     print(s[i])

# s = input()
# upper = 0
# lower = 0
# for i in range(len(s)):
#     if s[i].islower():
#         lower = lower+1
#     if s[i].isupper():
#         upper = upper + 1
# print(upper)
# print(lower)

# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i]== ' ':
#         count = count + 1
# print(count+1)

# s = input()
# c = input()
# count = 0
# for i in  s:
#     if i == c:
#         count=count+1
# print(count)

# s = input()
#
# digit = 0
# alpha = 0
#
# for i in s:
#     if i.isdigit():
#         digit += 1
#     if i.isalpha():
#         alpha += 1
# print(digit)
# print(alpha)

# li = []
# size = int(input())
# for i in range (size):
#     li.append(input())
# print(li)
#
# max = li[0]
# for i in li:
#     if len(i) > len(max):
#         max = i
# print(max)

# li = [1,2,3,4,5]
# print(li[::-1])

# li = [1, 'sasd', 45, 5]
# a = 0
# for i in li:
#     if isinstance(i, int) :
#         a = a+1
# print(a)

# li = [55, 6, 7, 88]
# min = li[0]
# for i in li:
#     if i < min:
#         min = i
# print(min)

# li = []
# size = int(input())
# for i in range (size):
#     li.append(int(input()))
# print(li)
# a = int(input())
# print(li.count(a))

# li = []
# size = int(input())
# for i in range(size):
#     li.append(int(input()))
# a = int(input())
# count = 0
# for i in li:
#     if i == a:
#         count = count + 1
# if count == 0:
#     print('НЕТ')
# else:
#     print('ЕСТЬ')

# li = [1, 23, 2, 5, 4, 6]
# count = 0
# for i in li:
#     if i % 2 == 0:
#         count = count + 1
# print(count)
#
# li = ['hgjhg', 'fuuu', 'hj', 'uu']
# a = input()
# count = 0
# for i in li:
#     if i[0] == a:
#         count += 1
# print(count)

# li = []
# size = int(input())
# for i in range(size):
#     li.append(input())
# min = li[0]
# for i in li:
#     if len(i)<len(min):
#         min = i
# print(min)


# a = input()
# b = a[::-1]
# if a == b:
#     print('Является полиндромом')
# else:
#     print('Не является полиндромом')


# li = []
# size = int(input())
# for i in range(size):
#     li.append(input())
# Lo = []
# for i in li:
#     b = 0
#     for a in li:
#         if i == a:
#             b = b + 1
#     if b == 1:
#         Lo.append(i)
# print(Lo)

# a = 'as12hg1'
# count = 0
# for i in a:
#     if i.isdigit():
#         count = count + 1
# print(count)

# di = {'Сидоров': 5674321, 'Петров': 7655432, 'Иванов': 8765432}
# print(di.get(input()))

# di = {'Сидоров': 5674321, 'Петров': 7655432, 'Иванов': 8765432, 'nbm' : 'fgugu', 654564: 7686}
# count = 0
# for key, value in di.items():
#     if isinstance(key, int):
#         count += 1
#     if isinstance(value, int):
#         count += 1
# print(count)

# di = {1: 'jh', 5: 'uyf', 3: 'ytf'}
# m = list(di.keys())[0]
# for i in di.keys():
#     if i > m:
#         m = i
# print(di.get(m))

# di = {'1': 'jh', '5': 'uyf', '3': 'ytf'}
# ke = input()
# va = input()
# for key, value in di.items():
#     if key == ke:
#         print('Есть ключ')
#     else:
#         print('Нет ключа')
#     if value == va:
#         print('Есть значение')
#     else:
#         print('Нет значения')
#
# d = {'1':'2', '2':'123'}
# k = input()
# v = input()
# value = d.get(k)
# if value == v:
#     print('содержит')
# else:
#     print('не содержит')

# li = []
# size = int(input())
# for i in range(size):
#     li.append(input())
# print(li[::-1])

# a = input()
# b = input()
# count = 0
# for i in a:
#     if i == b:
#         count +=1
# print(count)

# li = [1,2,3,4,5]
# a = 0
# for i in li:
#     a = a + i
# b = a/len(li)
# print(b)
# c = 1
# for i in li:
#     c = c * i
# d = c ** (1/len(li))
# print(d)

# st = 'hjfggggjhgjhgjh'
# li = list(st)
# a = li.count(li[0])
# b = li[0]
# for i in li:
#     if li.count(i) > a:
#         a = li.count(i)
#         b = i
# print(b)

# n = int(input())
# a = n-1
# for i in range(n,n*n,a):
#     print(i)

# import random
#
# l = []
# for i in range(5):
#     l.append((random.randint(1, 1000)))
# print(l)
# a = l[0]
# for i in l:
#     if i > a:
#         a = i
# b = l[0]
# for i in l:
#     if i > b and i != a:
#         b = i
# print(b)


# import random
#
# l = []
# for i in range(3):
#     l.append((random.randint(1, 1000)))
# print(l)
# s = 0
# p = 1
# for i in l:
#     s = s + i
#     p = p * i
# if s == p:
#     print('равны')
# else:
#     print('не равны')


# l = ['jhkh', 'Giuhh', 'Iho', 'hbkjh']
# for i in l:
#     if i[0].isupper():
#         print(i)
# import os
# f = open ('input.txt', 'r+')
# f.write ('5475765765')
#
# os.renames('input.txt', 'ort.txt')

# try:
#     a = int(input())
# except ValueError:
#     a = int(input('Введите число заново'))

import random as r
import os

# f = open('input.txt', 'r+')
#
# for i in f:
#     i = i.replace('\n', '')
#     s = i.split(' ')
#     if s[1] == '+':
#         if int(s[0]) + int(s[2]) == int(s[4]):
#             print('Правда')
#         else:
#             print('Неправда')
#     if s[1] == '-':
#         if int(s[0]) - int(s[2]) == int(s[4]):
#             print('Правда')
#         else:
#             print('Неправда')
#     if s[1] == '*':
#         if int(s[0]) * int(s[2]) == int(s[4]):
#             print('Правда')
#         else:
#             print('Неправда')
#     if s[1] == '/':
#         if int(s[0]) / int(s[2]) == int(s[4]):
#             print('Правда')
#         else:
#             print('Неправда')

# f = open('input.txt', 'r')
#
# l = []
# for i in f:
#     i = i.replace('\n', '')
#     s = i.split(' ')
#     for j in s:
#         try:
#             l.append(int(j))
#         except ValueError:
#             l.append(0)
# print(l)
# mi = l[0]
# ma = l[0]
# for i in l:
#     if i < mi:
#         mi = i
#     if i > ma:
#         ma = i
# print(mi)
# print(ma)
# l.sort(reverse=True)
# print(l)
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)

# f = open('input.txt', 'r')
# count = 0
# for i in f:
#     for j in i:
#         if j == '.':
#             count = count + 1
# print(count)


# f = open('input.txt', 'r', encoding='utf-8')
# ma = 0
# max = ''
# for i in f:
#     l = i.split('.')
#     for j in l:
#         if len(j) > len(max):
#             max = j
# print(f'{max} \nв нем содержится {len(max)} символов')

# # удалить из предложения все слова, длинна которых составляет одну букву
#
# f = open('input.txt', 'r', encoding='utf-8')
#
# max = ''
# for i in f:
#     l = i.split('.')
#     for j in l:
#         if len(j) > len(max):
#             max = j
# print(f'{max} \nв нем содержится {len(max)} символов')