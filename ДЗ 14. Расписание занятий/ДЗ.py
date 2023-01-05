# Занятия проходят по понедельникам и четвергам в 19:15
# Первое занятие произошло 17.10.2022. Всего 32 занятия.
# Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):
#
# Lecture  1: 17 Oct 2022 19:15
# Lecture  2: 20 Oct 2022 19:15
# ...
# Lecture  9: 14 Nov 2022 19:15
# Lecture 10: 17 Nov 2022 19:15
# ...
# Lecture 32: 02 Feb 2023 19:15

from datetime import *

a = 0
lecture_date = datetime(2022, 10, 13, 19, 15)
for _ in range(16):
    a += 1
    t1 = timedelta(days=4)
    t2 = timedelta(days=3)
    lecture_date += t1
    lecture_format = lecture_date.strftime('%d %b %Y %H:%M')
    print('Lecture' + '{:>3d}'.format(a) + f': {lecture_format}')
    a += 1
    lecture_date += t2
    lecture_format = lecture_date.strftime('%d %b %Y %H:%M')
    print('Lecture' + '{:>3d}'.format(a) + f': {lecture_format}')