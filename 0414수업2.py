
# 점수를 입력 받아 입력 점수가 0보다 작으면 "입력 값 오류" 출력 후 프로그램 종료

score = int(input("점수를 입력하세요: "))

# if문 한 개만 사용 되었다 -> 단일 if문
# 최대 선택 개수 -> 1
# 최소 선택 개수 -> 0 또는 1
if score < 0:
    print("입력 값 오류")
    

# 입력 값이 0 이상일 경우 합격 여부 판단
if score < 0:
    print("입력 값 오류")
else:
    pass # 합격 여부 판단 입력


# 홀수 짝수 구분
bar = 2

if bar % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
    
# 입력 값이 0 이상일 경우 합격 여부 판단, 80점 이상이면 합격
if score < 0:
    print("입력 값 오류")
else:
    if score >= 80:
        print("합격")
    else:
        print("불합격")    
    
    
    # if-elif-else, 점수에 따라 등급 부여(90이상 A, 80이상 B, 70이상 C, 그외 D)
    if score >= 90:
        print("A")
        grade = "A"
    elif score >= 80:
        print("B")
        grade = "B"
    elif score >= 70:
        print("C")
        grade = "C"
    else:
        print("D")
        grade = "D"
    
    # A등급 이면서 95점 이상이면 "우수상" 출력, 점수가 100점이면 "만점 축하!" 출력
    if grade == "A":
        if score >= 95:
            print("우수상")
    
    if score == 100:
        print("만점 축하!")