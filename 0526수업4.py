
def test(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)

arg_1 = [1, 2, 3, 4, 5, 6, 7]
arg_2 = [10, 20, 30, 40, 50, 60, 70]

# unpacking for a list
test(*arg_1) # 1 2 3 4 5 6 7
test(*arg_2) # 10 20 30 40 50 60 70


def test(*args): # Conduct packing for the arguments
    for val in args:
        print(val, end="\t")
    print()

test(1) # 1
test(1, 2) # 1      2
test(1, 2, 3) # 1       2       3
test(1, 2, 3, 4) # 1        2       3       4


def test(*args):
    print(args)
    print(type(args))

test(1, 2, 3, 4) # (1, 2, 3, 4)