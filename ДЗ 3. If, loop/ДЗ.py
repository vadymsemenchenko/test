# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10
# и первые два числа делятся на 3, то вывести yes, иначе no
# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них
# и запишите в переменную max.
# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
#
#
# В качестве решения отправить ссылку на github репозиторий.

a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))

if a > 10 and a % 3 == 0 and b > 10 and b % 3 == 0 and c > 10:
    print('yes')
else:
    print('no')
