
bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Delete
del bar[3] # 3번째 index 삭제
print(bar)

bar.pop() # 마지막 요소 삭제
print(bar)

bar.remove(8) # remove의 삭제 조건 : index가 아닌 value 값을 삭제
print(bar)

# bar.remove(10) -> pop()으로 10을 삭제했기 때문에 error




foo = [10, 20, 30, 40]
# 예외 처리
try:
    foo.remove(50)
except Exception:
    print("찾는 값이 없습니다.")