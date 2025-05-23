
import random

num_of_random = int(input("난수 개수를 입력하세요: "))
range_of_start = int(input("시작 범위를 입력하세요: "))
range_of_end = int(input("끝 범위를 입력하세요: "))

num_list = []
for i in range(num_of_random):
    num_list.append(random.randint(range_of_start, range_of_end))

unique_list = []
for i in range(len(num_list)):
    if num_list[i] not in unique_list:
        unique_list.append(num_list[i])

frequency = []
for i in range(len(unique_list)):
    count = 0
    for j in range(len(num_list)):
        if unique_list[i] == num_list[j]:
            count += 1
    frequency.append(count)
    
top_count_frequency = []
for i in range(len(frequency)):
    count = frequency[i]
    if count not in top_count_frequency:
        if len(top_count_frequency) < 3:
            top_count_frequency.append(count)
        else:
            min_idx = 0
            for j in range(1, 3):
                if top_count_frequency[j] < top_count_frequency[min_idx]:
                    min_idx = j
            if top_count_frequency[min_idx] < count:
                top_count_frequency[min_idx] = count
    
print(f"""
고유 숫자 리스트: {unique_list}
빈도 수 리스트: {frequency}
""")

print("\n가장 많이 등장한 숫자 Top 3 (동점 포함)")
for i in range(len(unique_list)):
    if frequency[i] in top_count_frequency:
        print(f"{unique_list[i]} -> {frequency[i]}회")
