
bar = [1, 2, 3]
foo = [1, 3, 2]

print(bar == foo) # 내부적으로 for문을 돌려서 요소가 같은지 확인함

bar = [1, 2, 3]
foo = [1, 2]

print(bar == foo)

bar = [1, 2, 3]
foo = bar

print(bar == foo) # 비교 연산자는 값을 비교
print(bar is foo) # is 연산자(identity operator)는 객체 자체가 같은지 비교
print(bar is not foo)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # 요소가 서로 같기 때문에 True
print(a is b) # a와 b는 서로 다른 리스트 객체이기 때문에 False