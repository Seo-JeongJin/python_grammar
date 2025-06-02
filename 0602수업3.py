
# bar 함수 정의
def bar(a, b, c, d = 50, e = 60, f = 70, g = 80, h = 90):
	print(a, b, c, d, e, f, g, h)

# bar 함수 호출
bar(1, 2, 3, 4, 5, h = 100) # 1 2 3 4 5 70 80 100 -> 1 2 3 4 5는 positional, 나머지는 keyword
bar(1, 2, 3, 4, 5, f = 100) # 1 2 3 4 5 100 80 90 -> 1 2 3 4 5는 positional, 나머지는 keyword
bar(1, 2, 3, h = 200) # 1 2 3 50 60 70 80 200 -> 1 2 3은 positional, 나머지는 keyword

def foo(a, b, c = 40, d = 50, e = 60):
    print(a, b, c, d, e)

foo(b = 10, a = 20, e = 100)
# foo(b = 20) -> 에러 -> 반드시 입력되어야 하는 a가 입력되지 않음음