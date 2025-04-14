
# 알고리즘 (입력 → 처리 → 출력)

def classify_customer():
    # 입력
    purchase_amount = int(input("총 구매 금액: "))
    num_of_refund = int(input("총 반품 횟수: "))
    num_of_purchase = int(input("총 구매 횟수: "))
    signed_up = int(input("가입 개월 수: "))

    # 예외 처리
    if num_of_purchase == 0:
        print("구매 횟수가 0입니다. 반품률을 계산할 수 없습니다.\n프로그램을 종료합니다.")
        return

    if num_of_refund > num_of_purchase:
        print("반품 횟수가 구매 횟수보다 많을 수 없습니다.\n프로그램을 종료합니다.")
        return

    # 반품률 계산
    refund_rate = (num_of_refund / num_of_purchase) * 100

    # 고객 분류
    if refund_rate >= 50 or (signed_up <= 3 and purchase_amount <= 10000) or num_of_refund >= 10:
        result = "위험 고객"
    elif purchase_amount >= 2000000 and refund_rate <= 10 and num_of_purchase >= 30 and signed_up >= 12:
        result = "우수 고객"
    else:
        result = "일반 고객"

    # 출력
    print(f"반품률: {refund_rate:.2f}%\n결과: {result}")


# 함수 실행
classify_customer()