
# 산술 연산자
    # 산술 연산자의 결과 값은 숫자

result_1 = 1 + 2 # 연산자의 개수 2개(대입 연산자(이항 연산), 산술 연산자(이항 연산)), 연산 우선 순위에서 가장 높은것이 ()이고 가장 낮은 것이 =(대입 연산자)이다
result_2 = 2 - 1.5 # 2.0 - 1.5 가 된다. interpreter가 형 변환 시킴 -> 묵시적 형 변환
result_3 = 3 * 2
result_4 = 4 / 2 # 결과 값이 실수로 나온다. 나눗셈을 하면 보통 몫과 나머지 둘 다 필요로 하니까 내부에서 자동으로 float으로 바꿔버림. 파이썬은 사용자 친화적 언어라 그렇다.

print(result_1, result_2, result_3, result_4)
print(type(result_1), type(result_2), type(result_3), type(result_4))

print(3 / 2) # 자바는 결과 값이 1이 나옴