
bar = [10, 20, 30]

# update : 특정 요소의 값을 변경하는 것
bar[0] = 20

foo = bar[0]
foo = 30 # -> primitive variable, bar의 list와 전혀 관련 없는 별도의 변수값 변경일 뿐임
print(bar) # 20, 20, 30