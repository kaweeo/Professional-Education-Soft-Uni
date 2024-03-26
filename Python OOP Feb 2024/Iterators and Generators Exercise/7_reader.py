
def read_next(*args):
    for argument in args:
        # for el in argument:
        #     yield el
        yield from argument



for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)