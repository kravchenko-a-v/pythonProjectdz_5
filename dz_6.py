# # №1
# def list (a):
#     li = []
#     for i in range(a):
#         i = input()
#         li.append(i)
#     return li
# print(list(5))

# # №2
#
# def dic(a):
#     b = []
#     c = []
#     for k in range(a):
#         i = input()
#         b.append(i)
#         j = input()
#         c.append(j)
#     di = dict(zip(b, c))
#
#     return di
# print(dic(3))

# № 3

def un(*args):
    b = []
    for i in args:
        if args.count(i) == 1:
            b.append(i)
    return b
print(un(1, 34, 'gjg', 34, 67))
