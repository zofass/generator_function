from inspect import isgenerator

def generator_decorator(func):
    def generate_numbers(begin, end):
        current = begin
        count = 0

        while count < end:
            yield current
            current = func(current)
            count += 1

    return generate_numbers

@generator_decorator
def pow(x):
    return x ** 2

assert isgenerator(pow(2, 4)) == True, 'Test1'
assert list(pow(2, 4)) == [2, 4, 16, 256], 'Test2'
print('OK')
