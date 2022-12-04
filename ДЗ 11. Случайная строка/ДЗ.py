# Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.
#
# def get_random_string(length: int) -> str:
#   pass
#
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]



# import random, base64
#
# def get_random_string(n):
#     return base64.b64encode(random.randbytes(n//8*6+6)).replace(b'+', b'A').replace(b'/',b'B')[:n].decode()
#
# print(get_random_string(20))


# мои заметки
# import random
#
# def get_random_string(length: int) -> str:
#     # Создаем пустую строку
#     s = ""
#
#     # Перебираем диапазон от 0 до length
#     for i in range(length):
#         # Выбираем случайный символ из диапазона ASCII-кодов
#         # от 65 (А) до 122 (z), включая как буквы латинского алфавита
#         # так и цифры
#         c = chr(random.randint(65, 122))
#
#         # Добавляем символ в строку
#         s += c
#
#     # Возвращаем сгенерированную строку
#     return s
#
# Генерируем случайную строку длиной 10 символов
# s = get_random_string(10)
# print(s)
