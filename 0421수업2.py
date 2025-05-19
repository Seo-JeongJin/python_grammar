
flag = True
while flag: # 조건식이 "참"인 동안 무한 실행
    value = int(input("양의 정수를 입력하세요: "))
    
    if value > 0:
        print("입력 값: ", value)
    else:
        flag = False