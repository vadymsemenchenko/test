# Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
# seq1 = [1, 2, 3, 4, 5]
# seq2 = [9, 8, 7]
# custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)]
# custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
#
# Встроенную функцию zip не используем.
#
# def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
#   pass
# """

from typing import Tuple, Iterable, List
from copy import *

def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    sequences_list = list(sequences)
    func_result = []
    minimal_len = min(map(len, sequences))
    maximal_len = max(map(len, sequences))
    if full:
        list_copy = deepcopy(sequences_list)
        for argument in list_copy:
            argument = list(argument.append(default) for _ in range(maximal_len - len(argument))
                            if len(argument) < maximal_len)
        for i in range(maximal_len):
            element = []
            for arg in list_copy:
                element.append(arg[i])
            func_result.append(tuple(element))
    else:
        for i in range(minimal_len):
            element = []
            for arg in sequences_list:
                element.append(arg[i])
            func_result.append(tuple(element))
    print(func_result)
