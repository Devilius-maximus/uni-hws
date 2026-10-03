def type_check(f):
    def something(x, y):
        try:
            x = int(x)
            y = float(y)
            return f(x, y)
        except:
            print("something wenet wrong ")
            pass

    return something

@type_check
def f(x: int, y: float) -> float:
    return 2*x + y

print(f(2 , 2.2))



