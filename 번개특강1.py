
# # 키보드로부터 정수를 입력받아 짝수이면 "짝수", 홀수이면 "홀수"를 화면에 출력하시오.

# # 키보드로부터 정수 입력

# # 입력 값 % 2 == 0 ->"짝수" 출력
# if input_value % 2 == 0:
# # else -> "홀수" 출력

# for val in range(1, 11):
#     print(f"{val % 3}", end = "")
    
    
    
    
    
# 키보드로부터 두 개의 정수를 입력 받아 저장 후 아래 메뉴를 출력하시오

# 1. 더하기
# 2. 빼기
# 3. 곱하기
# 4. 나누기

# 메뉴 출력 후 다시 키보드로부터 메뉴 선택값을 입력받고 선택한 연산자에 따라 이전 입력 받은 두 수의 연산값을 출력하시오.

input_value1 = int(input("첫 번째 입력 값: "))
input_value2 = int(input("두 번째 입력 값: "))

menu = """
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
"""
print(menu)

# Test 1
# print(f"{input_value1} + {input_value2} = {input_value1 + input_value2}")

# 메뉴 선택
sel_menu = int(input("메뉴를 선택하세요: "))

# 선택된 메뉴에 따른 연산 실시

result = ""

if sel_menu == 1:
    result = input_value1 + input_value2
elif sel_menu == 2:
    result = input_value1 - input_value2
elif sel_menu == 3:
    result = input_value1 * input_value2
elif sel_menu == 4:
    result = input_value1 / input_value2
else:
    result = "잘못된 입력입니다."

# 결과 값 출력
print()
print(f"결과 값: {result}")