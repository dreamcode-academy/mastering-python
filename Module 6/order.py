def example(a, b, *args, **kwargs):
    print('Default: ', a, b)
    print('Args: ', args)
    print('Kwargs: ', kwargs)

example(1,2,3,4, name='Python')