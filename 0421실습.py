
# 로그인 최대 시도 횟수 설정
count = 5
# 로그인 시도 루프
while count > 0:
    # 사용자로부터 ID, PW 입력 받기
    input_id = input("ID 입력: ")
    input_pw = input("PW 입력: ")
    # ID, PW 일치 확인
    if input_id == "admin" and input_pw == "1234":
        print("로그인 성공!")
        break # ID, PW 일치 시 프로그램 종료료
    else:
        count -= 1 # 실패 시 시도 횟수 감소
        if count > 0:
            print(f"ID 또는 PW가 잘못되었습니다. (남은 시도: {count})")
            print()
        else:
            # 5회 실패 시 계정 잠금 메시지 출력
            print(f"""ID 또는 PW가 잘못되었습니다. (남은 시도: {count})

계정이 잠금되었습니다.""")