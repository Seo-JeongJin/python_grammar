
# Create Dictionary

bar = {}
foo = dict()

print(type(bar), type(foo))

sol = {"123":10, "123":20, "456":30, "123":40}

print(sol) # {'123':40, '456':30}
# map에서는 index대신 우리가 임의로 만든 key 값을
# 이용해서 그것들을 index로 활용해서 데이터를 구분하고자 함
# 동일한 index = 동일한 key 값
# 그러므로 동일한 key 값에서는 제일 마지막 key 값이 나옴