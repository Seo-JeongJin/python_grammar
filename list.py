#[] = list

food = [100,["피자","햄버거"],"감자튀김","김치"]
food.append("고구마") 
# list에서만 사용할 수 있는 함수, food변수에 고구마가 뒤에 추가된다
food.insert(1, "감자") 
# 넣고 싶은 열에 넣을 수 있음, 100과 [피자, 햄버거] 사이에 들어감
food.remove("김치") 
# 말 그대로 제거, 단, 첫 번째 것만 제거됨
print(food.count("김치")) 
# 김치가 몇 갠지 출력된다. print함수를 사용해야함
print(food.index("김치")) 
# 몇 번째에 김치가 있는지 출력된다
food.sort() 
# 가나다라 순서대로 표기된다, 영어는 대문자가 먼저 출력되고 소문자 abc순서대로 출력된다, 숫자형과 문자열이 섞여있으면 오류가 난다.
food.sort(reverse=True) 
# food.sort()의 정반대로 출력
food[0] = "토마토" 
# food 0번을 토마토로 바꿈
print(food)

food2 = ["치킨","스시"]

food3 = food + food2

food4 = food * 3


print(food[0])
print(food[-1])
print(food[0:2])

print(type(food[0]))

print(food[1]) # 피자, 햄버거가 묶여서 출력된다, 2번은 감자튀김, 3번은 김치
print(food[1][0]) # 리스트 안의 리스트인 피자가 출력되게 된다

print(food2)
print(food + food2)
print(food3)
print(food4)