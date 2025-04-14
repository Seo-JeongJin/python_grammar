
# 상품 가격을 입력받아 할인율, 할인 금액, 최종 결제 금액을 계산 및 출력하는 함수 정의
def calculate_discount(price):
    # 조건에 따라 할인율 결정
    if price >= 100000:
        discount_rate = 0.1 # 10만원 이상이면 10% 할인
    elif price >= 50000:
        discount_rate = 0.05 # 5만원 이상 10만원 미만이면 5% 할인
    else:
        discount_rate = 0 # 5만원 미만이면 할인 없음
    
    # 할인 금액 계산    
    discount_price = price * discount_rate
    # 최종 결제 금액 계산
    final_price = price - discount_price
    
    # 할인율이 0보다 크면 할인율과 할인 금액 출력
    if discount_rate > 0:
        print(f"할인율: {int(discount_rate * 100)}%") # 어차피 할인율은 10% 아니면 5%이기 때문에 가독성을 위해 소수점으로 출력되는 할인율을 정수로 변환
        print(f"할인 금액: {discount_price}") # 할인 금액 출력
    else:
        print("할인 없음") # 할인율이 0일 때 메시지 출력
    
    # 최종 결제 금액 출력
    print(f"최종 결제 금액: {final_price}")
        
# 사용자에게 상품 가격을 입력받아 정수형으로 변환
price = int(input("상품 가격을 입력하세요: "))
# 입력한 가격을 기반으로 할인 계산 함수 호출
calculate_discount(price)