

# 정수 두 개를 입력 받고 합계를 출력하는 함수를 정의하시오.

def add(input1, input2): # input1, input2 == 매개변수
    total = input1 + input2
    return total # return == 값을 반환 or 함수 실행 종료

result1 = add(1, 2)
result2 = add(3, 4)
result3 = add(5, 6)


# 정수 3개를 입력 받고 평균을 반환하는 함수를 정의하시오.

def avg(input1, input2, input3):
    avg = (input1 + input2 + input3) / 3
    return avg

result = avg(44, 55, 77)
print(result)


def b():
    print("b 함수 호출")
    print("b 함수 종료")

def a():
    print("a 함수 호출")
    b()
    print("a 함수 종료")
    
a()
