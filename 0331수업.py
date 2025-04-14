
# 키보드로부터 3개의 정수를 입력받아 평균을 계산하는 프로그램

# 사용자로부터 정수 3개를 입력받는다.
# 입력받은 3개의 정수의 평균을계산하여 출력한다.

# 1. 세 개의 정수를 입력 받는다.
# 2. 입력받은 문자열을 정수로 변환한다.
a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))
c = int(input("세 번째 정수를 입력하세요: "))
# 3. 세 정수의 합을 구하고 3으로 나누어 평균을 계산한다.
average = (a + b + c) / 3
# 4. 평균값을 출력한다.
print(f"입력하신 세 정수의 평균은 {round(average, 2)}입니다.")



# 정수와 실수를 각각 하나씩 입력받아 두 수의 차를 계산하고 결과값과 그 자료형을 출력

# 정수, 실수를 사용자로부터 입력받는다.
a = int(input("정수를 입력하세요: "))
b = float(input("실수를 입력하세요: "))
# 두 수의 차를 계산한다.
sub = a - b
# 결과값과 결과값의 자료형을 출력한다.
print(f"정수와 실수의 차는 {sub}, 차의 자료형은 {type(sub)} 입니다.")




# 변수의 scope와 lifetime

bar = "hello"
print(bar)

del bar
print(bar)


# 변수의 scope 관점
# 1) global variable (전역변수)
#   -> 함수 밖에서 선언된 변수
#   -> birth : 변수 선언
#   -> death : 프로그램 종료 시

# 2) local variable (지역변수)
#   -> 함수 내 선언된 변수

def prt_show(arg_name):
    msg = arg_name + "님 안녕하세요" # msg는 지역 변수, msg의 생명 주기: birth -> 변수가 함수 내에서 선언됐을 때, death -> 함수가 종료됐을 때
    print(msg)

prt_show("홍길동")

print(msg) # msg는 prt_show 함수에서 선언된 지역 변수이기 때문에 당연히 에러가 발생



def get_name(arg_name):
    return arg_name + "님"

def get_greeting(arg_name):
    greeting = arg_name + "안녕하세요"
    return greeting

def prt_show(arg_name):
    name = get_name(arg_name)
    msg = get_greeting(name)
    print(f"name: {name} -> msg: {msg}")
    
prt_show("홍길동")

