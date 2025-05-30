
def bar(value1, value2):
	sum = value1 + value2
	avg = sum / 2
		
	# 반환 값으로 합계와 평균을 선택하고 싶다...근데 어떻게?
	return sum, avg # -> Java, C 는 안되는 문법, Python만 가능함

value = bar(1, 3)
print(value, type(value))



def bar(value1, value2):
	sum = value1 + value2
	avg = sum / 2
		
	return sum, avg
	
value = bar(1, 3)
print(value[0], value[1])

value_sum, value_avg = value # Unpacking
print(value_avg, value_sum)