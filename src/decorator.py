def publish(function, *args, **kwargs):
    import timeit
    try:
        start_time = timeit.default_timer()
        function(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
    except Exception as ex:
        exception_type = type(ex).__name__