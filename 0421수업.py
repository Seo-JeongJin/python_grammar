
# for _ in range(5): # 반복변수는 사용하지 않고 5번 반복하는 용도
#     print(f"{num}, ", end="")
 
for num in "abc": # 문자: 1글자, 문자열: 2글자 이상 나열
    print(f"{num}, ", end="")
    
for t in range(3):
    for i in range(4):
        for j in range(3):     
            for k in range(2): # j, k문 봤을 때 두 개의 벡터가 3줄 -> k가 열, j가 행 -> 3 * 2의 매트릭스 형성
                print(f"{j, k}")
                

matrix = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(i * j)
    matrix.append(row)