
bar = {"a" : 1, "b" : 2, "c" : 3}

t, x, y = bar # python의 dict에서 언패킹의 기본은 key

print(t, x, y) # a b c

t, x, y = bar.values()

print(t, x, y) # 1 2 3


for key, value in bar.items():
    print(key, value)
    # a 1
    # b 2
    # c 3