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


@call_times('foo.txt')
def foo():
  pass

@call_times('foo.txt')
def boo():
  pass

@call_times('calls.txt')
def doo():
  pass

foo()
boo()
foo()
foo()
boo()
doo()