
# bar = "h1rr2t"

# for char in bar:
#     print(f"[{char}, {char.isdigit()}]", end=" ")


str_int = input("문자와 숫자가 섞인 문자열을 입력하세요: ")

num_list = []
converted_list = []
for val in str_int:
    if val.isdigit():
        num_list.append(val)
        if int(val) % 2 == 0:
            converted_list.append(1)
        else:
            converted_list.append(-1)
    
subarray_list = []
for i in range(len(converted_list)):
    for j in range(i + 1, len(converted_list) + 1):
        if sum(converted_list[i:j]) == 0:
            subarray_list.append(converted_list[i:j])
            
print(f"""
입력 문자열: {str_int}
숫자 추출: {num_list}
변환된 리스트 (+1/-1): {converted_list}""")

print("\n합이 0인 연속 부분 수열 목록:")
for element in subarray_list:
    print(f"- {element}")