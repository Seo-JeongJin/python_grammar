def foo():
    return 1, "hello", 10.0 # -> Packing -> 세 개의 값을 하나의 튜플로 묶어서 반환

test = foo() # (1, "hello", 10.0) -> 반환 값이 여러개 일때, 튜플을 생성하여 값을 할당
print(test[0], test[1], test[2])
a, b, c = foo() # -> Unpacking -> foo()가 반환한 튜플을 각각 분해해서 저장

print(a, b, c)


# bar 함수 정의
def bar(a, b, c, d = 50, e = 60):
	print(a, b, c, d, e)

# bar 함수 호출
bar(1, 2, 3, 4, 5) # 1 2 3 4 5 -> default value가 존재하더라도 인자값이 우선임
bar(1, 2, 3, 4) # 1 2 3 4 60
bar(1, 2, 3) # 1 2 3 50 60
bar(1, 2) # Error