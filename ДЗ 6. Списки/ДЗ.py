#
# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список
#
#
# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка
#
#
# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
#
#
# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
#
#
# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C
#
#
# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла
# (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
#
#
# Задание 7:
# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример:
#
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
#
# Количество чисел: 3
#
#
# В качестве решения отправить ссылку на github репозиторий.



# 1
# my_list = []
#
# for _ in range(5):
#     number = int(input('Enter 5 numbers: '))
#     my_list.append(number)
# print(my_list)


# 1.1
# a = str(input('Enter 5 numbers: '))
# print([a])


# 1.2
# a = str(input('Enter 5 numbers: '))
# print(list(a))


# 2
# A = [1, 2, 3, 4, 5]
# del A[4]
# print(A)


# 2.1
# A = [1, 2, 3, 4, 5]
# A.remove(5)
# print(A)


# 2.2
# A = [1, 2, 3, 4, 5]
# print(A[0:4])


# 2.3
# A = [1, 2, 3, 4, 5]
# A.pop()
# print(A)


# 3
# A = []
#
# for _ in range(10):
#     number = int(input('Enter a number: '))
#     A.append(number)
# print(A)
#
# N = int(input('Enter a number N: '))
# print(A.count(N))


# 4
# A = []
#
# N = int(input('how many numbers will be in the list?: '))
# for i in range(1,N+1):
#     m = int(input(' ' + str(i) + ': '))
#     A.append(m)
# print(A[::-1])


# 4.1
# A = []
#
# N = int(input('how many numbers will be in the list?: '))
# for i in range(1,N+1):
#     m = int(input(' ' + str(i) + ': '))
#     A.append(m)
# A.reverse()
# print(A)

# 5
# A = []
#
# for _ in range(5):
#     number = int(input('Enter a number: '))
#     A.append(number)
# print(A)
# A = [x for x in A if x > 5]
# print(A)


# 5.1
# A = []
#
# for _ in range(5):
#     number = int(input('Enter a number: '))
#     A.append(number)
# print(A)
# print([elem for elem in A if elem > 5])


# 6 new
# N = int(input('how many numbers would you like to enter?: '))
# A = []
#
# for i in range(N):
#     number = int(input(f'Enter only integer № {i + 1}: '))
#     A.append(number)
# max_ = A[0]
# for x in A:
#     if x > max_:
#         max_ = x
# print(f'max: {max_}')
# min_ = A[0]
# for x in A:
#     if x < min_:
#         min_ = x
# print(f'min: {min_}')


# 7
# import re
#
# a = input('enter text: ')
# res = len(re.findall(r'\d+', a))
# if res:
#     print('amount of numbers:', res)
# else:
#     print('numbers not found')


# 7.1
# import re
#
# a = input('enter text: ')
# print('amount of numbers:', len(re.findall(r'\d+', a)))


# 7.2
# import re
#
# s = input('enter text: ')
# count = len(re.findall(r'\b\d+\b', s))
# print('amount of numbers:', count) \
#     if count \
#     else \
# print('numbers not found')
