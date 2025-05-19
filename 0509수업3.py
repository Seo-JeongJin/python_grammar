
foo = [10, 20, 30, 50] # 요소(index(순서) and value(값))의 개수 -> 특정 리스트의 사이즈

pos = foo # foo, pos 둘 다 참조변수(주소값을 저장하기 위함) -> 둘 다 동일한 리스트를 가리킴
pos[3] = 200                

print(foo[3])

# 메모리 안에서 일어나는 일들
    # foo -- 0xfa 를 생성
    # pos가 존재하지 않으니 생성 후 foo를 pos에 대입 -> pos -- 0xfa