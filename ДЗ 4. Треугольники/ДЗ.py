# Запросить у пользователя число N - ширина треугольника.
#
# Задание максимум на 80 баллов:
#
# Вывести треугольник #1 с шириной N с помощью цикла while
# Вывести треугольник #2 с шириной N с помощью цикла while
# Задание со звездочкой:
#
# Вывести треугольник #3 с шириной N с помощью цикла while
# Вывести треугольник #4 с шириной N с помощью цикла while
#
#
# В качестве решения нужно отправить ссылку на github репозиторий.


# 1
# N = int(input('Enter width of triangle #1: '))
# while N > 0:
#    print(f'#' * N)
#    N -= 1


# 2
# N = int(input('Enter width of triangle #2: '))
# i = 0
# while i < N:
#    i += 1
#    print(f'#' * i)


# 3
# N = int(input('Enter width of triangle #3: '))
# i = 0
# while i < N:
#    print(f' ' * i + '#' * (N-i) )
#    i += 1


# 4
# N = int(input('Enter width of triangle #4: '))
# i = 0
# while i < N:
#    i += 1
#    print(f' ' * (N-i) + '#' * i)
