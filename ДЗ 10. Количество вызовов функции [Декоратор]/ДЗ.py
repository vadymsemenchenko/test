# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'
# Пример:
#
# @call_times('foo.txt')
# def foo():
#   pass
#
# @call_times('foo.txt')
# def boo():
#   pass
#
# @call_times('calls.txt')
# def doo():
#   pass
#
# foo()
# boo()
# foo()
# foo()
# boo()
# doo()
#
# Файл foo.txt:
# foo была вызвана 3 раза
# boo была вызвана 2 раза
# Файл calls.txt:
# doo была вызвана 1 раза
#
#
# В качестве решения отправить ссылку на github репозиторий.


# counter = {}
# text = 'Function {} was called {} times.\n'
#
# def call_times(file_name):
#     def inner(func):
#         def wrapper():
#           wrapper.count += 1
#           counter[func.__name__] = wrapper.count
#           with open(file_name, 'w') as f:
#                for func_name, quantity in counter.items():
#                   f.write(text.format(func_name, quantity))
#           return func()
#         wrapper.count = 0
#         return wrapper
#     return inner
#
# @call_times('foo.txt')
# def foo():
#     pass
#
# @call_times('foo.txt')
# def boo():
#     pass
#
# @call_times('calls.txt')
# def doo():
#     pass
#
# for i in range(5):
#     foo()
#
# for i in range(10):
#     boo()
#
# dict.clear(counter)
#
# for i in range(15):
#     doo()
