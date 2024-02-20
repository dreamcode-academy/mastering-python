def setup(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print(setup(theme='dark', time_out=30))