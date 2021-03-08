def dec(f):
    def wrapper():
        print('Before')
        f()
        print('After')

    return wrapper


@dec
def my_func():
    print('I am f')


@dec
def my_func2():
    print('I am F2')


my_func()
my_func2()