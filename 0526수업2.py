
bar = [val for val in range(1, 6)]

# * -> collection -> list -> Packing
a, *b = bar # a에 bar의 첫 번째 요소를 할당, b에 나머지 요소를 묶어서 리스트로 할당
print(a, b) # 1 [2, 3, 4, 5]

a, *b, c = bar # a는 첫값, c는 마지막 값, b는 중간값들 리스트로 묶음
print(a, b, c)

a, b, *c = bar 
print(a, b, c) # 1 2 [3, 4, 5]