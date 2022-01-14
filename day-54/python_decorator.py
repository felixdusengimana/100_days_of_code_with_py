import time

current_time = time.time()
print(f"Current time: {current_time}")


def calc_time_decorator(function):
    def wrapper_function():
        start_time = time.time()
        print(f"{function.__name__} start time: {start_time}")
        function()
        end_time = time.time()
        print(f"{function.__name__} end time: {end_time}")
        print(f"Time taken: {end_time-start_time}")

    return wrapper_function()


@calc_time_decorator
def fast_func():
    for i in range(10000):
        multy = i * i


@calc_time_decorator
def slow_func():
    for i in range(100000000):
        multy = i*i