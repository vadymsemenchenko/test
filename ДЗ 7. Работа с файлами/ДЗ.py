# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
#
# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt
#
# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
#
# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
#
# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
#
# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
#
# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4
#
# В качестве решения отправить ссылку на github репозиторий



# 0
# import re
# a = []
#
# f = open('temp.txt', 'r')
# temp = f.readline()
# count = len(re.findall(r'\b\d+\b', temp))
# print('amount of numbers:', count) \
#     if count \
#     else \
# print('numbers not found')
# f.close()
#
# print()


# 1
# numbers = []
#
# with open('temp.txt') as f:
#     file_input = f.read().split()
#     for i in file_input:
#         try:
#             numbers.append(int(i))
#         except:
#             pass
# print(numbers)


# 1.1
# numbers = []
#
# with open('temp.txt') as f:
#     file_input = f.readline().split()
#     for i in file_input:
#         try:
#             numbers.append(int(i))
#         except:
#             pass
# print(numbers)


# 2
# s = input('enter text: ')
# f = open('data.txt', 'w')
# print(s, file=f)
# f.close()


# 2.1
# data = []
#
# s = input('enter text: ')
# data.append(s + '\n')
# f = open('data.txt', 'w')
# for s in data:
#     f.write(s)
# f.close()


# 2.2
# data = []
#
# for i in range(4):
#     s = input('Enter text: ' + str(i+1) + ": ")
#     data.append(s + '\n')
# with open('data.txt', 'w') as f:
#     f.writelines(data)


# 2.3
# data = []
#
# for i in range(4):
#     s = input('Enter text: ' + str(i+1) + ": ")
#     data.append(s + '\n')
# f = open('data.txt', 'w')
# for s in data:
#     f.write(s)
# f.close()


# 3
# data = []
#
# N = int(input('how many numbers will be in the list?: '))
# for i in range(1,N+1):
#     m = str(input(' ' + str(i) + ': '))
#     data.append(' ' + m)
# with open('data.txt', 'w') as f:
#     f.writelines(data)


# 3.1
# data = []
#
# N = int(input('how many numbers will be in the list?: '))
# for i in range(1,N+1):
#     m = str(input(' ' + str(i) + ': '))
#     data.append(' ' + m)
# f = open('data.txt', 'w')
# for m in data:
#     f.write(m)
# f.close()


# 4
# from random import randint
#
# with open('random_numbers.txt', 'w') as f:
#     for number in (randint(0, 100) for _ in range(100)):
#         f.write(str(number) + '\n')


# 4.1
# import random
#
# with open('random_numbers.txt', 'w') as f:
#     for i in range(100):
#         number = random.randint(0, 100)
#         f.write(str(number) + '\n')


# 5
# f = open('temp.txt')
# temp = f.read()
# words = temp.split()
#
# print('Number of words in file :', len(words))
# f.close()


# 6 цифры
# with open('random_numbers.txt') as f:
#     print(sum(int(i) for i in f.read().strip().split()))


# 6.1 числа
# with open('random_numbers.txt') as f:
#         print(sum(map(int, filter(str.isdigit, ''.join(f.read())))))


# 7
# from collections import Counter
# import re
#
# words = re.findall(r'\w+', open('temp.txt').read().lower())
# counter = Counter(words).most_common(5)
# print (counter)

