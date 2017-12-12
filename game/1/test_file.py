# print(int(0))
#
# l = [
#     {
#         'id': 1,
#     },
#     {
#         'id': 3,
#     },
#     {
#         'id': 4,
#     },
#     {
#         'id': 2,
#     },
# ]
#
# l.sort(key=lambda x: x['id'])
# print(l)

# def fun(*args, **kwargs):
#     print(args[1])
#
# fun(1)

# def test():
#     return 1
#
# def test2():
#     test()
#     print('awesome')
#
# test2()

# import math
#
# print(math.ceil(7 / 3))
# import uuid
#
#
# def create_64():
#     return str(uuid.uuid4()) + str(uuid.uuid4())
#
#
# print(create_64())
# print(create_64())
# print(create_64())

# class Test(object):
#     def __init__(self, form):
#         self.a = form.get('a', '')
#         self.b = form.get('b', '')
#
#
# d = {
#     'a': 1,
#     'b': 2,
# }
#
# c = Test(d)
# print(c.a, c.b)

# l = list(s)
# print(l)


from datetime import datetime
import time
from datetime import timedelta


def time_change(value):
    format = '%H:%M:%S'
    dt = time.strftime(format, value)
    print(dt)


# time_change(61.79)



# def log(*args, **kwargs):
#     format = '%Y/%m/%d %H:%M:%S'
#     value = time.localtime(int(61.79))
#     print('value', value)
#     dt = time.strftime(format, value)
#     print(dt, *args, **kwargs)
#
# log(1)

# print(type(float('72.28')))
#
# print(time.strftime("%M:%S", time.gmtime(float('72.28'))))


# def time_c(t):
#     m = int(t / 60)
#     s = int(t - m * 60)
#     f = str(t - m * 60 - s)[1:]
#     print(m, s, f)
#     return '[{:0>2}:{:0>2}{}]'.format(m, s, f)
#
# print(time_c(0.23))

# d = {
#     'id': 1,
# }
#
# print(d.keys())
# class A(object):
#     a = ''
#     b = ''
#
#     def __init__(self):
#         self.a = 'qqq'
#         self.b = 'aaa'
#         self.c = ''
#
# a = A()


# def pretty(m):
#     m = m.__dict__
#     l = []
#     for k, v in m.items():
#         l.append('{} = ({})'.format(k, v))
#     return l
#
# print(pretty(a))

# t = time.time()
# print(t)

"""
var l = ['ass', 'we', 'can']
l = JSON.stringify(l)

var form = {
    id: 1,
    billy: l
}
"""


# l = [1, 2, 3]
# l2 = [2, 3, 4, 5]
# l3 = list(set(l) - set(l2))
# print(l3)

# d = {
#     1: '1',
#     2: '2',
# }
# ks = d.keys()
# print(ks, set(ks))


def second_time():
    t = datetime.now()
    return t


def day_time():
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return t


def stamp_time():
    t = time.time()
    return t


s = second_time()
d = day_time()
ds = datetime.strptime(d, "%Y-%m-%d")
st = stamp_time()
print(s + timedelta(days=1), type(s), s)
print(d)
print(st)
print(s < ds, ds + timedelta(days=1) + timedelta(hours=6))
