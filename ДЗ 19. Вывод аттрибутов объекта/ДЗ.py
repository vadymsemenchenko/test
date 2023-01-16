# Написать класс-миксин, наследуя который объект будет выводится в консоль
# в виде имени класса и словаря аттрибутов со значениями:
#
# ClassName: {
#     key: value
# }
#
# class AttributePrinterMixin:
#     pass
#
# Протектед и приватные аттрибуты должны выводить только свое имя
# (без знака подчеркивания для протектед и префикса "_<имя класса>__")
# Каждя строка с полем начинается с символа табуляции.
# Если класс наслудует другие классы, их аттрибуты тоже должны выводится по тем же правилам.
# Свойства обрабатывать не надо.
#
# Пример:
#
# class A(AttributePrinterMixin):
#     def __init__(self):
#         self.public_filed = 3
#         self._protected_field = 'q'
#         self.__private_field = [1, 2, 3]
#
# a = A()
# print(a)
# A: {
#    public_filed: 3
#    protected_field: q
#    private_field: [1, 2, 3]
# }


import re


class AttributePrinterMixin:
    def __repr__(self):
        symbol1 = "{"
        symbol2 = "}"
        attributes = self.__dict__
        attr_list = ''
        private_pattern = '[\S]*__[\S]*'
        protected_pattern = '_[\S]*'
        for i in attributes.items():
            key = i[0]
            if re.fullmatch(protected_pattern, key):
                key = key[key.find("_") + 1:]
            if re.fullmatch(private_pattern, key):
                key = key[key.find("__") + 2:]
            attr_list += f"\t{key}: {i[1]} \n"
        return f'{self.__class__.__name__}: {symbol1}\n' \
               f'{attr_list}{symbol2}'


class Class_A(AttributePrinterMixin):
    def __init__(self):
        self.public_field = 3
        self._protected_field = "Q"
        self.__private_field = [1, 2, 3]
