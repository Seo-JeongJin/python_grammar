
bar = [3, 4, 5]
foo = [6, 7, 8]

pos = bar + foo

print(pos)

bar += foo # 새로운 리스트를 생성하는 것이 아님
print(bar)
print(foo)