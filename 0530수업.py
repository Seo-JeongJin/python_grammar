
# 함수 정의
# -> 자기만의 함수를 만들고 싶을 때

def bar():
    # 실행되는 알고리즘 선언
    for _ in range(5):
        print("hello world")

bar()

def get_input_num():
    msg = "정수를 입력하세요: "
    input_value = int(input(msg))
    
    if input_value < 0:
        print("0과 양의 정수만 입력하세요.")
        return
    
    return input_value

value = get_input_num()
print(value, type(value))