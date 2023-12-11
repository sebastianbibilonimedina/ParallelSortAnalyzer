import time

def measure_time(function, *args):
    start = time.time()
    result = function(*args)
    end = time.time()
    return result, end - start
