

row = 5
col = 3

for num_row in range(row, 0, -1):
    for _ in range(num_row):
        print("* ", end="")
    
    print()
    
    
# row 반복
for num_row in range(1, row + 1):
    # " " 반복
    for _ in range(row - num_row):
        # " " 출력
        print(" ", end="")
    
    # "*" 반복
    for _ in range(num_row):
        # "*" 출력
        print("*", end="")
    
    print()
    

# row 반복
for num_row in range(1, row + 1):
    # " " 반복
    
    # if num_row % 2 == 0:
    #     print()
    #     continue  -> num_row가 짝수일 때 밑 알고리즘 건너뜀
    
    for _ in range(row - num_row):
        # " " 출력
        print(" ", end="")
    
    # "*" 반복
    for _ in range(num_row * 2 - 1):
        # "*" 출력
        print("*", end="")
    
    print()