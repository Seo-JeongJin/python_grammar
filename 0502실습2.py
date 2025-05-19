
# + 문제
# 1. random값 중복 안되게
# 2.  추가 옵션을 선택하세요
#     테두리
#     왼쪽 -> 오른쪽 대각선
#     오른쪽 -> 왼쪽 대각선
#     양방향 대각선
#     옵션 선택(1~4): 

import random

table = int(input("테이블 개수 입력: "))
row = int(input("행 수 입력: "))
col = int(input("열 수 입력: "))

option_choice = int(input("""
출력 옵션을 선택하세요: 
1. 1부터 시작하여 열 방향으로 증가
2. 1~100 사이 랜덤 값 출력
옵션 (1 또는 2): """))


for i in range(table):
    print(f"테이블 {i + 1}")
    
    if option_choice == 1:
        count = 1
        for _ in range(row):
            for _ in range(col):
                print(count, end="\t")
                count += 1
            print()
    
    elif option_choice == 2:
        used_num = []
        
        for _ in range(row):
            for _ in range(col):
                while True:
                    num = random.randint(1, 100)
                    if num not in used_num:
                        used_num.append(num)
                        print(num, end=" ")
                        break
            print()
    print()
    
    
"""
추가 옵션을 선택하세요
1. 테두리
2. 왼쪽 -> 오른쪽 대각선
3. 오른쪽 -> 왼쪽 대각선
4. 양방향 대각선
옵션 선택(1~4): 
"""