
bar = [val for val in range(1, 11, 2)] # [1, 3, 5, 7, 9]

# Reverse
print(bar[::-1]) # start, stop이 생략 -> 전체를 역순으로 출력 -> [9, 7, 5, 3, 1]
print(bar[-1:-4:-1]) # start = 9, stop = 3, step = -1 -> [9, 7, 5]
print(bar[-3:]) # -3번재 index부터 -1번째 index까지 1씩 증가하면서 -> [5, 7, 9]
print(bar[::-1][:3]) # [9, 7, 5, 3, 1]의 [:3] -> [9, 7, 5]