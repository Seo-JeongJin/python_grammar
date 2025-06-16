
bar = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}

foo = {"a" : 1, "b" : 2, "c" : 3}

print(len(bar)) # 4


bar = {"a" : 1, "b" : 2, "c" : 3}

foo = {"b" : 2, "a" : 1, "c" : 3} # -> 입력된 순서로 데이터가 저장되는 것이 아님

if bar == foo:
	print("True") # True
else:
	print("False")
 

bar = {"a" : 1, "b" : 2, "c" : 3}

foo = {"b" : 2, "a" : 5, "c" : 3, "d" : 10}

test = bar | foo

print(test)