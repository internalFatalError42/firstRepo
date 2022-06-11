from threading import Thread


def threaded(func):
    """
    Decorator that multithreads the target function
    with the given parameters. Returns the thread
    created for the function
    """
    def wrapper(*args, **kwargs):
        thread = Thread(target=func, args=args)
        thread.start()
        return thread
    return wrapper


# Usage


# just add the threaded decorator above the function
# you want to multithread
@threaded
def some_func(results):
    value = 'some_compute_heavy_value'
    results.append(value)


@threaded
def other_func(results):
    value = 'some_other_compute_heavy_value'
    results.append(value)


@threaded
def third_func(results):
    value = 'another_compute_heavy_value'
    results.append(value)


threads = []
results = []
for _ in range(10):
    threads.append(some_func(results))
    threads.append(other_func(results))
    threads.append(third_func(results))

# wait for all threads to finish before moving on
for thread in threads:
    thread.join()


for i in enumerate(results):
    print(i)
