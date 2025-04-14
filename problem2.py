
# 국어 점수를 사용자에게 입력받아 정수형으로 변환하는 함수
def get_korean_score():
    return int(input("국어 점수: "))

# 영어 점수를 입력받는 함수
def get_english_score():
    return int(input("영어 점수: "))

# 수학 점수를 입력받는 함수
def get_math_score():
    return int(input("수학 점수: "))

# 세 과목의 평균 점수를 계산하는 함수
# 매개변수로 국어, 영어, 수학 점수를 받아 세 수의 평균을 계산
def calculate_average(korean, english, math):
    return (korean + english + math) / 3

# 판정을 내리는 함수
# 평균 점수와 각 과목 점수를 기준으로 우수 합격, 합격, 불합격 중 하나를 반환
def determine_result(korean, english, math, average):
    # 우수 합격 조건: 평균 90점 이상이고 각 과목이 모두 80점 이상
    if average >= 90 and korean >= 80 and english >= 80 and math >= 80:
        return "우수 합격"
    # 일반 합격 조건: 평균 70점 이상이고 각 과목이 모두 40점 이상
    elif average >= 70 and korean >= 40 and english >= 40 and math >= 40:
        return "합격"
    # 위 두 조건에 해당하지 않으면 불합격 처리
    else:
        return "불합격"

# 프로그램의 전체 흐름을 제어하는 메인 함수
def main():
    # 1. 사용자로부터 국어, 영어, 수학 점수를 각각 입력받음
    korean_score = get_korean_score()
    english_score = get_english_score()
    math_score = get_math_score()
    
    # 2. 세 과목의 점수를 이용해 평균 점수를 계산
    average_score = calculate_average(korean_score, english_score, math_score)
    
    # 3. 평균 점수와 각 과목 점수를 바탕으로 결과를 판정
    result = determine_result(korean_score, english_score, math_score, average_score)
    
    # 4. 평균 점수 출력
    print(f"평균: {average_score:.2f}") # .2f로 소수점 둘째 자리까지 표현
    
    # 5. 판정 결과 출력(우수 합격, 합격, 전체 프로그램 시작)
    print(result)
    
# main() 함수 호출을통해 전체 프로그램 시작
main()