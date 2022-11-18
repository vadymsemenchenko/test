#  1
# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
#
#  2
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
#
#  3
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
#
#  4
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
#
#
# В качестве решения отправить ссылку на репозиторий.


# 1
# lst = [1, 2, 3]
#
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
# print(change(lst))


# 2
# lst = [1, 2, 3, 4, 5]
#
# def to_dict(lst):
#     return {element: element for element in lst}
#
# print(to_dict(lst))


# 3
# start = int(input('Enter numbers: '))
# end = int(input('Enter numbers: '))
#
# def sum_range(start, end):
#     if start > end:
#         end, start = start, end
#     return sum(range(start, end + 1))
#
# print(sum_range(start, end))


# 4
# def read_last(lines: int, file):
#     if type(lines) == int and lines > 0:
#         for i in range(lines):
#             with open(f'{file}', 'r') as f:
#                 f = f.read()
#             f = list(f.splitlines())
#             f.reverse()
#             line = f[i]
#             print(line)
#     else:
#         print('Entered non-positive quantity')
#
# read_last(-1, 'file.txt')


# не корректно работает, это я сам для себя пробовал
#
# def read_last(lines, f):
#     if lines > 0:
#         with open('file.txt') as f:
#             f_lines = f.readlines()[-lines:]
#         for line in f_lines:
#             print(line.strip())
#         else:
#             print('Entered non-positive quantity')
#
# read_last(3, 'file.txt')
# read_last(-2, 'file.txt')