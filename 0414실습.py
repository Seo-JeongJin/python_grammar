
# 프로그래밍(1) 실습문제 : 4월 14일(월)
# #1 별다방 주문 처리 시스템
# 1. 문제 개요
# - 별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램을 작성하시오. - 이 실습문제를 통해 선택문 흐름 제어의 다양한 구조를 이해하고, 실제 서비스 로직
# 설계에 가까운 조건문 분기를 실습해 본다
# 2. 문제 설명
#  - 고객에게 다음 정보를 입력받고, 이에 따라 최종 주문 정보와 혜택을 출력하시오
#  - 모든 입력은 정확한 값이 들어온다고 가정(Happy scenario)하며, 입력값에 대한 오류
# 예외 처리는 하지 않는다.
#  ‣ 입력 항목
#  ① 음료 종류 (coffee, latte, juice 중 하나)
#  ② 크기 (small, medium, large)
#  ③ 멤버십 여부 (yes, no)
#  ‣ 입력 항목
#  1) 가격 계산
#  ‣ coffee: 3000원
#  ‣ latte: 4000원
#  ‣ juice: 3500원
#  2) 크기 추가 요금
#  ‣ small: 추가 없음
#  ‣ medium: 500원 추가
#  ‣ large: 1000원 추가
#  3) 멤버십 혜택
#  ‣ 멤버십 고객에게는 총 금액의 10% 할인 적용
#  4) 무료 샷 제공 조건
#  ‣ 멤버십 고객 중, coffee 또는 latte 주문이면서 크기가 large인 경우
#  → "무료 샷이 제공됩니다!" 문구 출력(중첩 조건 사용)


beverage = input("음료를 선택하세요 (coffee/latte/juice): ").lower()
size = input("크기를 선택하세요 (small/medium/large): ").lower()
membership = input("멤버십이신가요? (yes/no): ").lower()

# 기본 가격
if beverage == "coffee":
    base_price = 3000
elif beverage == "latte":
    base_price = 4000
elif beverage == "juice":
    base_price = 3500

# 크기 추가 요금
if size == "medium":
    add_price = 500
elif size == "large":
    add_price = 1000

total_price = base_price + add_price
free_shot = False

# 멤버십 할인 및 무료 샷 출력
if membership == "yes":
    discount = int(total_price * 0.1)
    final_price = total_price - discount

    # 이 안에서만 무료 샷 메시지 출력
    if beverage in ("coffee", "latte") and size == "large":
        free_shot = True
    discount_display = str(discount) + "원"
else:
    discount = "할인 없음"
    final_price = total_price
    discount_display = discount
    
result = f"""
기본가격: {base_price}원
크기 추가 요금: {add_price}원
할인 적용: {discount_display}
최종 결제 금액: {final_price}원
"""
print(result)

if free_shot == True:
    print("무료 샷이 제공됩니다!")