# Задание 1:
# Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'
#
# Задание 2:
# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
#
# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.
#
# Задание 4:
# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
#
# Задание 5:
# Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
# что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"
#
# В качестве решения нужно отправить ссылку на github репозиторий.


# 1.0
# a = str(input('Enter a word: '))
# b = a[::-1]
# if a == b:
#   print('+')
# else:
#   print('-')


# 1.1
# a = str(input('Enter a word: '))
# if a == a[::-1]:
#     print('+')
# else:
#     print('-')


# 2
# a = str(input('Enter text: '))
# b = str(input('Enter find word: '))
# if b in a:
#     print('YES')
# else:
#     print('NO')


# 3
# a = str(input('Enter text: '))
# if a:[:3] == 'abc':
#      a = 'www' + a[3:]
#    else:
#      a += 'zzz'
#    return a
# print(a)


# 3
# a = str(input('Enter text: '))
# def f(a):
#     if a.startswith('abc'):
#         return 'www' + a[3:]
#     return a + 'zzz'
# print(f(a))


# 3.1
# a = str(input('Enter text: '))
# def f(a):
#     if a[:3] == 'abc':
#         a = 'www' + a[3:]
#     else:
#         a += 'zzz'
#     return a
# print(f(a))


# 4
# a = str(input('Enter text: '))
# import re
# a1 = re.sub('[1|2|3|4|5|6|7|8|9|0]', '', a)
# print(a1)


# 5
# a = str(input('Enter your mail: '))
# if a.find('@') != -1 and a.find('.') != -1:
#     print('YES')
# else:
#     print('NO')

