# # 1
#
# li = []
# size = int(input())
# for i in range(size):
#     li.append(int(input()))
# a = []
# for i in li:
#     if i % 2 == 0:
#         a.append(i)
# print(a)

# # 2
#
# li = []
# size = int(input())
# for i in range(size):
#     li.append(int(input()))
# a = 0
# for i in li:
#     if i > 0:
#         a = a + 1
# print(a)

# # 3
#
# li = []
# size = int(input())
# for i in range(size):
#     li.append(int(input()))
# a = li[0]
# b = []
# for i in li:
#     if i > a:
#         b.append(i)
#     a = i
# print(b)

# 4

li = []
size = int(input())
for i in range(size):
    li.append(int(input()))
a = li[0]
b = []
li.pop(0)
for i in li:
    if i > 0 and a > 0 or i < 0 and a < 0 :
        b.append(a)
        b.append(i)
        break
    a = i
print(b)