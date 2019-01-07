# def now():
#     print('现在时间是2019-01-04')

# f = now
# f()
#
# print(now.__name__)
# print(f.__name__)

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' %func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print('现在时间是2019-01-04')
#
# now()

import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s call %s():' %(text, func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
#
# @log('你是谁')
# def now():
#     print('现在时间是2019-01-04')
#
# now()
# print(now.__name__)

import time

def metric(fn):
    def wrapper(*args, **kw):
        t1 = time.time()
        f = fn(*args, **kw)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, (t2 - t1) * 1000))
        return f
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return  x+y

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

print(fast(1,2))
print(slow(3,4,5))