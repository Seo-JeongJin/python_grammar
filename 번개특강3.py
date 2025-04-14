
# 정수 한 개를 입력받아 홀수이면 "홀수 입니다.", 짝수이면 "짝수 입니다."를 출력하는 함수를 작성하시오

# 함수 정의
def prt_even_odd(arg_input):
    msg = ""
    if arg_input % 2 == 0:
        msg = "짝수"
    else:
        msg = "홀수"

    print(f"{msg} 입니다.")
    
prt_even_odd(4)
prt_even_odd(3)


# 정수 4 개를 입력 받아 합계를 반환하는 함수를 출력

def sum(input1, input2, input3, input4):
    sum = input1 + input2 + input3 + input4
    return sum


# 정수 4개를 입력받아 평균을 반환하는 함수를 작성하시오

def avg(input1, input2, input3, input4):
    return sum(input1, input2, input3, input4) / 4
    


print(sum(2, 2, 1, 3))
print(avg(3, 5, 6, 8))



bar = 3 # 전역 변수

def test():
    bar = 2 # 지역 변수, 함수 내에서 변수가 선언됐을 때 birth, 함수가 종료됐을 때 dead -> 지역 변수의 생명 주기
    
    print(bar)

test()
print(bar)