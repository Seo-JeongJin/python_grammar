name = "jeongjin"
job = "student"
age = 24


print(f"안녕하세요. 내 이름은 {name}입니다. 직업은 {job}입니다. 나이는 {age}입니다.") # 이것을 주로 사용하도록 하자


# print("안녕하세요. 내 이름은 " + name + "입니다." + "직업은" + job + "입니다." + "나이는" + age + "입니다")(x)
# 숫자랑 문자열이랑은 더할 수 없기 때문에 age에는 str을 붙여줘야 함
print("안녕하세요. 내 이름은 " + name + "입니다." + "직업은" + job + "입니다." + "나이는" + str(age) + "입니다")
print("안녕하세요. 내 이름은 %s입니다. 직업은 %s입니다. 나이는 %s입니다." %(name, job, age))
print("안녕하세요. 내 이름은 {0}입니다. 직업은 {1}입니다. 나이는 {2}입니다.".format(name, job, age))
