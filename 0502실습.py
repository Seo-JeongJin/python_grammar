
table = int(input("테이블 개수 입력: "))
row = int(input("행 수 입력: "))
col = int(input("열 수 입력: "))

for _ in range(table):
    for _ in range(row):
        for _ in range(col):
            print("*", end=" ")
        print()
    print()