# # 1
#
# N = int(input())
#
# count = 1
# while count <= N:
#     print(count)
#     count = count * 2

# # 2
#
# N = int(input())
# count = 1
# while count <= N:
#     if count == N:
#         print("YES")
#         break
#     count = count * 2
# else:
#     print("NO")

# # 3
#
# N = int(input())
# count = 1
# while count <= N:
#     if count**2<=N:
#         print(count**2)
#     else:
#         break
#     count = count + 1

# Для отважных

count = 0
while True:
    N = int(input())
    if N > count:
        count = N
    if N == 0:
        break
print(count)
