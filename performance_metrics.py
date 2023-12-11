import time

def measure_time(function, *args, **kwargs):
    start = time.time()
    function(*args, **kwargs)  # Execute the function with the provided arguments.
    end = time.time()
    return end - start
