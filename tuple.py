# 리스트와 마찬가지로 여러 개의 데이터를 담을 수 있음
food = ("피자","햄버거","치킨")
food2 = ["피자","햄버거","치킨"]
food3 = food + food2

print(type(food)) # tuple
print(type(food2)) # list

print(food[-1]) # tuple도 index를 사용하면 그대로 출력된다.

food[0] = "김치"
print(food) 
# 출력 되지 않는다! 튜플과 리스트의 가장 큰 차이점은 튜플은 값 수정이 안된다는 것

print(food3 * 3)