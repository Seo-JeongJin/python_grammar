
count = 0
while count < 3:
    for value in range(1, 3):
        if count == 1:
            continue # continue가 선언된 블록의 반복문으로 이동한다(반복에서 특정 알고리즘을 실행하고 싶지 않을 때)
        
        print("count: ", count, "value: ", value)
    
    count += 1