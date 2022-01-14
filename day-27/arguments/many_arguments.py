def add(*args):
    """Return sum of numbers added as params"""
    sum = 0
    for n in args:
        sum += n
    return sum


def add_second(n, **kwargs):
    return (n+kwargs["add"])*kwargs["multiply"]


print(add_second(3, add=2, multiply=5))
print(add(19, 20, 30))
