import time


def timer(func):
    def wrapper(*args, **kwargs):
        # save the start time
        start_time = time.time()
        # call the original function and save the result
        result = func(*args, **kwargs)
        # save the end time
        end_time = time.time()
        # print the execution time to the console
        print(f"Elapsed time: {end_time - start_time:.2f} seconds")
        return result

    return wrapper
