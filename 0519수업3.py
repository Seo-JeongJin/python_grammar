
bar = [val for val in range(1, 11, 2)] # [1, 3, 5, 7, 9]

for val in range(2, 11, 2):
    print(val, end="\t")  # 2, 4, 6, 8, 10

# slicing은 새로운 list를 만들어 냄 -> 지정한 요소들을 복사해 list 생성
print(bar[2 : 11 : 2]) # 2번째 index부터 10번째 index까지 2칸씩 띄어가면서 -> [5, 9]
print(bar[0 : 5 : 1]) # [1, 3, 5, 7, 9]
print(bar[0 :]) # [1, 3, 5, 7, 9]
print(bar[2 :]) # [5, 7, 9]
print(bar[2 : 4]) # [5, 7]
print(bar[2 : 3]) # [5]
print(bar[2 : -1]) # 2번째 index부터 -1의 -1번째 index까지(-2) -> [5, 7]

# bar[start(생략시 0) :(생략 불가) stop(생략시 -1) :(생략 가능) step(생략시 1)]