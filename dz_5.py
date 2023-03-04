# # №1
# a = input('Введите слово: ')
# a1 = 'AEIOULNSTRАВЕИНОРСТ'
# a2 = 'DGДКЛМПУ'
# a3 = 'BCMPБГЁЬЯ'
# a4 = 'FHVWYЙЫ'
# a5 = 'KЖЗХЦЧ'
# a8 = 'JXШЭЮ'
# a10 = 'QZФЩЪ'
#
# su = 0
#
# for i in a:
#     if i in a1:
#         su += 1
#     if i in a2:
#         su += 2
#     if i in a3:
#         su += 3
#     if i in a4:
#         su += 4
#     if i in a5:
#         su += 5
#     if i in a8:
#         su += 8
#     if i in a10:
#         su += 10
# print(su)

# №2
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
a = []
for key, value in emails.items():
    for i in range(len(value)):
        a.append(value[i]+'@'+key)
a.sort()
print(a)
