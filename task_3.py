from random import randint


def decomaker(n):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, int):
                return result * n
        return wrapped_func
    return decorator


@decomaker(randint(2, 10))
def foo(n):
    return n


@decomaker(randint(2, 10))
def bar(n):
    return n ** 2


@decomaker(randint(2, 10))
def foobar(n):
    return foo(n) + bar(n)


if __name__ == '__main__':
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(foobar(i))
        elif i % 3 == 0:
            print(foo(i))
        elif i % 5 == 0:
            print(bar(i))
        else:
            print(i)
    print(str(foo("Надеюсь, что все задания понял правильно :)")) + "theless")
