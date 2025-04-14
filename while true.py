# 기본 구조
# while True:
    # 반복할 코드 작성
    # if 조건:
        # break = 조건 만족하면 반복 종료
        
while True:
    text = input("입력하세요. (종료하려면 'exit' 입력): ")      
    if text == 'exit':
        print("프로그램이 종료 되었습니다.")
        break
    else:
        print(f"입력한 값: {text}")
        
# 1~10 사이의 숫자 입력 시 종료
while True:
    num = int(input("1부터 10까지의 숫자를 입력하세요: "))
    if 1 <= num <= 10:
        print(f"입력한 값 {num}은(는) 유효한 값입니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")