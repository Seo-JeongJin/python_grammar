
bar = [val for val in range(1, 6)]

# Multiple assignment operator
# 여러 변수에 같은 값 또는 한꺼번에 값 지정
foo, pos, kin = 2, 3, 4
print(foo, pos, kin)

# Unpacking
# 하나의 iterable(리스트, 튜플 등)을 여러 변수로 푸는 것
a, b, c, d, e = bar

foo = [1, 2, 3]
pos = [4, 5, 6]

for x, y in zip(foo, pos):
    print(f"{x}, {y}")
    

bar = [5, 6, 7]
foo = bar 
a, b, c = bar
sol, *pos = bar

print(foo)
print(sol, pos)


def test(*args): # *args 값들을 set -> packing
    pass

bar = [2, 3, 4]

test(*bar) # *bar에서 값을 get해서 각 인자로 set -> unpacking