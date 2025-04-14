
# bar = 2
# foo = 3

# if bar > 5:
#     print(True)
    
# while foo > 1:
#     print(True)
    
# for val in range(10):
#     print(val)        

# 예약어, 명령어는 변수로 지정할 수 없다. 



# 1. 함수 정의/선언
# say_something : 입력 값 -> 알고리즘["안녕하세요"] -> 출력 값 화면에 문자열 출력

# def 명령어는 새로운 함수 정의를 의미한다.
def say_something():
    print("안녕하세요")
    
# 2. 함수 호출
say_something()
say_something()

def add(x,y): # x와 y는 매개변수(parameter) -> 함수과 정의될 떄 입력 값을 받기 위해 설정한 변수
    result = x + y
    return result # **함수를 호출하면 함수가 정의되어 있는 곳으로 점프한다 -> 그 함수를 실행 -> 다시 호출한 지점으로 되돌아온다**

result1 = add(2,3) # 여기서 2와 3을 인자값(argument)라고 한다. -> 함수가 호출될 때 실제로 전달되는 값
result2 = add(5,6)
print(f"result1: {result1}, result2: {result2}")
# 함수명(입력값, ...)

def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

def input():
    print("x")
    
input() # 메모리에는 function(내가 정의한 곳), system(내장된 함수)이 있는데, 함수를 정의했을 때 메모리에서 function에 있는 것을 먼저 찾고 system에 있는 것을 찾는다, 우선 순위가 내가 정의한 곳이 먼저임.