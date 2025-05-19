
# 입력 값이 양수가 아닐 경우,
# 에러 메시지 출력 후 재입력
# 양수를 입력 받을 때 까지

is_valid = False
while not is_valid:
    input_value = int(input("정수 입력: "))
    
    # 조건식이 거짓인 경우
    if input_value > 0:
        is_valid = True
    else:
        print("양의 정수를 입력하세요.")
        
# break, continue는 독립적으로 사용되는 것이 아니라 기본적으로 반복문과 같이 사용된다
# 다른 언어에서 선택문에서 쓰이기도 한다
    # 양의 정수인 경우, 반복 종료
    if input_value > 0:
        break # 특정 조건에서 해당 반복을 멈추고 싶을 때