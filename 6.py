def salam_decorator(func):
    def wrapper():
        print("hi!")
        func()
        print("bye!")
    return wrapper

@salam_decorator
def test():
    print("i'm in between")

test()


