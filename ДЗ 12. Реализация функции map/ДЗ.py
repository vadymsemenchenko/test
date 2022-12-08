# 2. Написать функцию, которая возвращает список результатов выполнения заданной функции,
# к соответствующим элементам переданных итерируемых объектов.
# Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
#
# custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]
#
# Встроенную функцию map не используем.
#
# def custom_map(function: Callable, *iterables: Iterable) -> Iterable:
#   pass


def custom_map(function, *iterables):
    out = []
    min_len = None
    for i in iterables:
        if min_len is None or len(i) < min_len:
            min_len = len(i)
    for i in range(min_len):
        args = []
        for j in iterables:
            args.append(j[i])
        out.append(function(*args))
    return out

a = [1, 2, 3]
b = [2, 4, 0, 6]
c = [4, 6, 2, 8]
res = custom_map(lambda x, y, z: x + y + z, a, b, c)

print(list(res))