import time


def add():
    return 10 + 10


start = time.time()
add()
print('It took', time.time() - start, 'seconds')


def decorator(func):
    def wrapper():
        return func
    return wrapper()


add2 = decorator(add())

print(add2)
