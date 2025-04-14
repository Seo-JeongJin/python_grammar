
# 논리 연산자
    # 좌항과 우항의 값이 "참"일 때만 참이고 그 이외에는 모두 거짓이다.
    # and는 조건식이 둘 다 만족할 때 True, 이항 연산자 (피연산자는 결과 값이 불린 값으로 출력이 되면 어떤 것이든 넣을 수 있음)
    # or은 조건식이 둘 중 하나만 만족해도 True, 이항 연산자
    # not은 조건식의 피연산자의 값을 반전시킨다, 단항 연산자

if 3 < 2 and 3 < 3:
    print("T 1")
if 3 > 2 and 3 < 3:
    print("T 2")
if 3 < 2 and 3 >= 3:
    print("T 3")
if 3 > 2 and 3 >= 3:
    print("T 4")
    

if 3 < 2 or 3 < 3:
    print("T 1")
if 3 > 2 or 3 < 3:
    print("T 2")
if 3 < 2 or 3 >= 3:
    print("T 3")
if 3 > 2 or 3 >= 3:
    print("T 4")
    

if not (2 > 3):
    print("T 1")
else:
    print("F 1")

if not (2 > 3):
    print("T 1")
else:
    print("F 2")