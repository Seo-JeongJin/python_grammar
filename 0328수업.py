
a = 10
b = "5"
c = 3.0
d = True

print(type(a + int(b))) # 15
print(type(str(a) + b)) # 105
print(type(c + a)) # 13.0
print(type(a * d)) # 10


# Truthy, Falsy 예제
temp_1 = 1 # 정수형 변수
temp_2 = -1 # 정수형 변수
temp_3 = 0 # 정수형 변수
temp_4 = -0 # 정수형 변수

if temp_1: # 1 -> Truthy 값
    print("참") # 출력값
else:
    print("거짓")
    
if temp_2: # -1 -> Truthy 값
    print("참") # 출력값
else:
    print("거짓")

if temp_3: # 0 -> Falsy 값
    print("참")
else:
    print("거짓") # 출력값
    
if temp_4: # -0 -> Falsy 값
    print("참")
else:
    print("거짓") # 출력값

# False
# - 숫자: 0, 0.0 
# - 문자: ""    
# True
# False의 반대되는 모든 값
    
# if 조건식:
     # 조건식이 참인경우 실행되는 코드들, 조건식에 올 수 있는 연산자는 비교 연산, ** 조건식이 반환할 수 있는 값은 두 가지 뿐이다(True, False)
# else:
     # 조건식이 거짓 인경우 실행되는 코드들
     
bar = True

# 실습
input_value = input("값을 입력하세요: ")

input_value = int(input_value)

# 입력 값이 0 이면 "0 입니다."
# 입력 값이 0 이 아니면 "0이 아니에요"

if input_value == 0:
    print("0 입니다.")
else:
    print("0이 아니에요")
    
# 실습
input_value = int(input("입력 값: "))

# 입력 값이 양수이면 "양수" 출력
# 입력 값이 음수이면 "음수" 출력
# 입력 값이 0이면 "0" 출력

if input_value > 0:
    print("양수")
elif input_value < 0:
    print("음수")
else:
    print("0")
    

# 실습
# 입력 값이 짝수이면 "짝수" 출력
# 입력 값이 홀수이면 "홀수" 출력
# 조건식 : input_value % 2 == 0 -> 짝수를 판별하는 조건식

if input_value % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
# 실습
# 암호를 입력하세요 : "0539405442"
# 암호가 일치 할 경우 "로그인 성공"
# 암호가 일치 하지 않을 경우 "로그인 실패"

input_value = input("입력 값: ")

if input_value == "0539405442":
    print("로그인 성공")
else:
    print("로그인 실패")
    
# 실습
# 사용자로부터 문자 1개를 입력 받습니다.
# 그 다음, 사용자로부터 정수 1개를 입력 받습니다.
# 입력 받은 문자를 입력 받은 정수만큼 반복 출력합니다.

# 실행 예)
# 문자 하나를 입력하세요 : $
# 문자를 반복 출력할 정수를 입력 하세요

input_value = input("문자 하나를 입력하세요: ")
num = int(input("문자를 반복 출력할 정수를 입력하세요: "))

print(input_value * num)

# 정사각형의 면적을 구하시오
# 가로 또는 세로 길이를 입력

size_of_rec = int(input("가로 또는 세로의 길이를 입력하세요: "))

print(f"정사각형의 넓이는 {size_of_rec ** 2}입니다.")


# 정사각형의 면적을 구하시오
# 가로 또는세로의 길이가 0 또는 음수일 경우 -> "양수를 입력하세요"

size_of_rec = int(input("가로 또는 세로의 길이를 입력하세요: "))

if size_of_rec <= 0:
    print("양수를 입력하세요")
else:
    print(f"정사각형의 넓이는 {size_of_rec ** 2}입니다.")


# 입력 값이 3의 배수이면 3의 배수입니다.
# 입력 값이 4의 배수이면 4의 배수입니다.
# 그 이외에는 아무것도 출력하지 않음

num = int(input("숫자를 입력하세요: "))

if num % 3 == 0 and num % 4 == 0:
    print("3의 배수이면서 4의 배수입니다.")
    exit()
if num % 3 == 0:
    print("3의 배수입니다.")
if num % 4 == 0:
    print("4의 배수입니다.")
    
    
# 변의 길이를 입력 하세요
# 도형을 선택하세요 : 1번 사각형 2번 삼각형
# 만약 1번을 선택하면 정사각형의 면적을 출력
# 2번을 선택하면 정삼각형의 면적을 출력
# 1, 2번 이외의 값이 입력될 경우 "잘못된 입력 입니다."

length = int(input("변의 길이를 입력 하세요: "))

choice = int(input("도형을 번호로 선택하세요\n1. 사각형\n2. 삼각형\n: "))

if choice == 1:
    print(f"정사각형의 면적은 {length ** 2}입니다.")

elif choice == 2:
    print(f"정삼각형의 넓이는 {(length ** 2) / 2}입니다.")
    
else:
    print("잘못된 입력입니다.")
    