from time import perf_counter

"""
A decorator to get the execution time of a function
"""
def timer(func):
    def search_func(*args, **kwargs):
        start_time = perf_counter()
        to_execute = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'
              .format(func.__name__, execution_time))
        return to_execute

    return search_func
