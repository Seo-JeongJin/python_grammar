
for val in range(10, 20, 4):
    print(val, end="\t")
    
# List Comprehensin : 리스트 안의 요소 값을 특정 알고리즘으로 만들고 싶을 때
# for문의 반복변수 값을 앞의 변수에 넣어줌
bar = [val for val in range(10, 20, 4)]
print(bar)

foo = [val for val in range(1, 11)]
print(foo)