# def if_even(a, b = 3, c = [1,2,3], d = '123'):
#     if a % 2 == 0:
#         print('Чётное')
#     else:
#         print('Не чётное')
# def if_positive(a):
#     if a > 0:
#         print('Положительное')
#     else:
#         print('Отрицательное')
# n = int(input())
# if_even(n)
# if_positive(n)

# def sum(a,b):
#     return a+b
# def min(a,b):
#     return a-b
# def um(a,b):
#     return a*b
# def de(a,b):
#     return a/b
# print(sum(1,2))

# def count_numbers(a):
#     count = 0
#     for i in a:
#         if isinstance(i, int):
#             count +=1
#     return count
# print(count_numbers([1, 2, 'fgg']))


# def if_number(a):
#     try:
#         int(a)
#         return True
#     except ValueError:
#         return False
#     except TypeError:
#         return False
# print(if_number([21,32]))

# def max_key(a):
#     b = ''
#     for i in a.keys():
#         if len(i) > len(b):
#             b = i
#     return b
#
#
# def max_value(a):
#     b = ''
#     for i in a.values():
#         if len(i) > len(b):
#             b = i
#     return b
#
#
# print(max_value({'a': 'ghg', 'sda': 'oijiojo', 'yuyu3': 'i'}))


def fun(*args):
    count = 0
    for i in args:
        if isinstance(i, int):
            if i % 2 == 0:
                count +=1
    return count
print(fun(1,4, 'fd', 2))