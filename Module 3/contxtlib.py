import contextlib

@contextlib.contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file('example', 'w') as f:
    f.write("Example")