
count = 5

while count > 0:
    ID = input("ID를 입력하세요: ")
    PW = input("PW를 입력하세요: ")
    
    if ID == "admin" and PW == "1234":
        print("로그인 성공!")
        break

    elif ID != "admin":
        count -= 1
        result = f"등록되지 않은 ID입니다. 남은 시도: {count}회"
    
    elif PW != "1234":
        count -= 1
        result = f"등록되지 않은 PW입니다. 남은 시도: {count}회"
        
        if count == 2:
            print(f"등록되지 않은 PW입니다. 남은 시도: {count}회\n비밀번호를 재설정하세요.")
            break
    
    else:
        count -= 1
        
        if count > 0:
            result = f"ID 또는 PW가 잘못되었습니다. 남은 시도 {count}회"
            
    if count == 0:
        result = "계정이 잠금되었습니다."
        
    print(result)
    print()