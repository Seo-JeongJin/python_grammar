
# List Comprehension
bar = [val for val in range(10, 21, 2)]

# pop(index) or pop() -> 특정 index 값을 읽고 제거
print(bar.pop(0)) # 10
print(bar) # [12, 14, 16, 18, 20]
print(bar.pop(2)) # 16
print(bar) # [12, 14, 18, 20]
print(bar.pop()) # 20, pop() -> list의 가장 마지막 요소 삭제
print(bar) # [12, 14, 18]