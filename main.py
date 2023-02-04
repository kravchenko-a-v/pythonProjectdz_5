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

a = int(input())
b = int(input())
c = int(input())
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a
print(a,b,c)