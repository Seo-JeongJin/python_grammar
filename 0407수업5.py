
# 비교 연산자의 결과 값은 항상 boolean형이다.

print(3 > 4) # False
print(2 > 2) # False
print(2.0 >= 2) # True
print(3 < 4) # True
print(4 <= 4) # True
print(1 == 1) # True
print(1 != 2) # True
print(True != False) # True
print("a" > "c") # False

print(2 < 3.0) # 2가 float로 형 변환 발생
print("2" == 2) # 문자형과 다른 형을 비교하면 무조건 False
print(3.0 != 4) 