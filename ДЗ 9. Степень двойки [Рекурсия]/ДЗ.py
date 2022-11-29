# Написать функцию которая принимает целое число - number.
# Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
# Запрещено пользоваться функцией или оператором возведение в степень.
#
# Пример:
# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
# is_power_of_two(125) # 'no' потому что это не степень двойки
#
# В качестве решения отправить ссылку на github репозиторий.


# def is_power_of_two(n):
#     return 'YES'\
#         if (n & (n-1)) == 0\
#         else 'NO'
#
# print(is_power_of_two(int(input('Enter an integer: '))))


# def is_power_of_two(n):
#     if n%1:
#         return 'NO'
#     if n>2:
#         return f(n/2)
#     if n:
#         return 'YES'
#     return 'NO'
#
# print(is_power_of_two(int(input('Enter an integer: '))))


# def is_power_of_two(n):
#     if n == 1:
#         return 'Yes'
#     if n < 1 or n % 2 != 0:
#         return 'No'
#     return is_power_of_two(n // 2)
#
#
# n = int(input('Enter an integer: '))
# print(is_power_of_two(n))
