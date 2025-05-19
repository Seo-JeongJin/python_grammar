
bar = [] # 요소가 0개인 list

# bar[0] = 1 -> 0번째 인덱스의 요소 값을 1로 저장
# 현재 리스트 내 요소가 0개
# 리스트에 요소를 추가하기 위해서는 함수를 이용한다.
# .append, .insert

bar.append(100)
bar.append(200)
print(bar)
print(bar[0], "\t" ,bar[1])
# print(bar[2]) -> error : out of index