
#**매우 중요한 개념
assci_code = 65
my_char = chr(assci_code + 2)
print(f"assci_code: {assci_code}, \ my char: {my_char}")

# 65는 literal constant,literal constant는 자료형을 가진다. 
# 메모리 상에 저장된다는 것은 2가지 특징을 가진다. 이름(그 공간의 주소값 = address)과 자료형(data type)
# assci_code와 65 둘 다 저장 공간이다. assci_code는 변수이므로 이름과 자료형(int형) 둘 다 가지고 65는 자료형(숫자형(정수, 실수), 문자형, 불린형)만 가진다, literal constant는 이름을 가지지 않는다, 컴퓨터 내부에 65라는 값이 무엇인지 저장되어 있기 때문.

bar = 2
foo = 3.0

result = bar + foo
print(f"type: {type(result)}, result: {result}") # 출력 값 : float, 5.0
# 정수와 실수를 함께 연산할 때는 정수가 실수로 변환되어서 계산 된다.



# 프로그램이 동작하면서 들어오는 변수에 따라서 자료형이 바뀔수 있는 프로그래밍 언어의 특성 -> dynamic typing 대표적으로 파이썬
x = 10
x = "hello" # 처음에는 int타입이었는데, 다음 줄에서는 str 타입으로 자료형이 바뀌었다.

# 한 번 정해진 타입은 바꿀 수 없는 프로그래밍 언어 -> static typing(java)
# int x = 10;
# x = "hello";     변수 x는 int로 선언되었기 때문에 정수만 저장할 수 있다. 23번 열에서 에러 발생



#input은 사용자로부터 받은 값을 문자열로 반환, 문자열 + 문자열이 되면 그냥 문자끼리 붙여버린다, 숫자로서 연산을 하고 싶을 때는 int(input())으로, str -> int로 바꿔줘야 한다. 



# 형 변화 -> type calling
# 형 변화 종류
# - 명시적 형 변화 -> 사람이 직접
# - 묵시적 형 변화 -> interpreter

# 명시적 형 변환 2 + 3.0 -> float(2) + 3.0
# 묵시적 형 변환 2 + 3.0 -> 2.0 + 3.0
bar = 3.45
foo = int(bar)
print(foo) # 결과값? = 3

# 파이썬에서 명시적 형변환을 위한 방법으로 함수 제공
# int() -> 정수로 변환
print(type(int("333"))) # 333 int
# float() -> 실술 변환
print(type(float("333"))) # 333.0 float
# str() -> 문자열로 변환
print(type(str(22.01))) # "22.01" string
