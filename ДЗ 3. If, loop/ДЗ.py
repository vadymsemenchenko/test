# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10
# и первые два числа делятся на 3, то вывести yes, иначе no
# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них
# и запишите в переменную max.
# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
#
#
# В качестве решения отправить ссылку на github репозиторий.

# 1
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# if a > 10 and a % 3 == 0 and b > 10 and b % 3 == 0 and c > 10:
#     print('yes')
# else:
#     print('no')


# 2.0
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# print (max(a, b, c))


# 2.1
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# if a > b and a > c:
#     print( a )
# if b > a and b > c:
#     print( b )
# if c > a and c > b:
#     print( c )


# 2.2
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# if a >= b and a >= c:
#     print( a )
# elif b >= a and b >= c:
#     print( b )
# else:
#     print( c )


# 2.3
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# print( a if a >= b and a >= c else b if b >= a and b >= c else c )


# 3
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# summch = 0
# for i in range(a, b, + 1):
#     if i % 2 == 0:
#         summch += i
#         print("Сумма четных: ", summch)