

def sum(input1, input2, input3):
    return input1 + input2 + input3

print(sum(1, 2, 3)) # 6
print(sum(5, 5, 6)) # 16



msg = "hello"

def prt_msg(arg_msg):
    msg = "안녕하세요"
    print(arg_msg + msg)
    
prt_msg(msg)

print(msg)


# 지역 변수
    # 함수 내에서 선언된 변수
    # 생명주기 B -> 함수 호출 후 변수 선언 시
    # 생명주기 D -> 함수가 종료되면
    # 접근범위 S -> 변수 선언 후
    # 접근범위 F -> 함수 종료 전까지
# 전역 변수
    # 함수 밖에서 선언된 변수
    # 생명주기 B -> 변수 선언 시
    # 생명주기 D -> 프로그램 종료 시
    # 접근범위 S -> 변수 선언 후
    # 접근범위 F -> 프로그램 종료 전까지
    
    
# scope chaining
# 🧠 그럼 왜 잘 작동할까? 여기서 스코프 체이닝이 등장해!
# 💡 Scope(스코프): 변수에 접근할 수 있는 범위
# 파이썬은 LEGB 규칙을 따라 스코프를 탐색해.
# 이건 무슨 뜻이냐면:
    # L (Local): 현재 함수 내부에서 먼저 찾음
    # E (Enclosing): 함수 안에 함수가 있다면, 그 바깥 함수의 스코프
    # G (Global): 전역 스코프 (파일 전체)
    # B (Built-in): 파이썬이 제공하는 내장 스코프

msg1 = "님 안녕하세요."
msg2 = "반갑습니다."
def prt_something(arg_name):
    # global msg1, msg2 -> global이 없어도 작동, 지역 변수가 선언되어 있지 않으면 내장 변수로 이동, 내장 변수에도 없으면 Error
    # 함수 안에 전역 변수를 사용하고 싶다!!
    print(arg_name + msg1 + " " + msg2)
    
prt_something("홍길동")



bar = 3

def test():
    global bar
    # 전역 변수 bar의 값을 1 증가 시키고 싶어
    bar = 4 # set을 하려면 무조건 global 선언을 해줘야 한다. 즉, global 키워드는 함수 안에서 전역 변수를 "수정"하고 싶을 때 필요하다.

test()
print(bar) 