
# 변수명 작성 규칙
# -> 대소문자 구분
# -> 변수 앞에 숫자부터는 올 수 없다
# -> 특수문자가 첫 글자로 올 수 없다. 단, _는 사용 가능

# 변수명 작성 시 주의 사항
# - 의미 있는 변수명을 작성할 것

value1Input = 3 # Java wordWord 
value2_input = 3 # Python word_word

# 변수 선언 
# -> 메모리 상에 데이터를 저장하는 공간을 할당.
# -> 변수명 = "초기값"
bar = 2
bar = 3
bar = 5
pos = 2
# 여기서 변수 선언은 2, 5번 라인에서 변수 선언이 발생했다(변수의 첫 번째 값이 선언 되는 것임.), 또한 여기서는 set(값을 대입)만 일어났다.

bar = 2 # set
bar = pos # get(값을 읽음)
bar = 5 # set
pos = 2 # set

bar = 3
bAr = 1
print(f"bar: {bar}, bAr: {bAr}") # 변수 선언은 2번 일어났다. 둘 다 메모리 상에 없는 값이기 때문




print(type(4))
print(type(4.0))
print(type("4"))
print(type(True))
print(type(False))  # type는 메모리의 자료형을 나타내준다.