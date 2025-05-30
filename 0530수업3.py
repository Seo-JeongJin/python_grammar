
def bar(a, b, c, d, e = 100):
	print(a, b, c, d, e)

bar(1, 2, 3, 4, 5) # 1 2 3 4 5
bar(1, 2, 3, 4) # 1 2 3 4 100
bar(1, 2, 3) # Error