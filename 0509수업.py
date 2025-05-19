
bar = [50, 10, 30, 40, 20] # element 5개

for index in range(5): # index == 요소를 선택
    print(bar[index], end=",\t")

bar[0] = 200
bar[4] = 100

print(bar)