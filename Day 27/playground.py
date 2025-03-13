def add(*args):
    print(f"your second input number is {args[1]}")
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 6, 5))


def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.motor = kw.get("motor")  # set None by default unless it changed


my_car = Car(make="Nissan", model="GT-R")
print(my_car.motor)
