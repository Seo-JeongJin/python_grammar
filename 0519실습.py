
print("\n정수 10개를 입력하세요.")

num = []

for i in range(10):
    num.append(int(input(f"{i + 1}번째 정수를 입력하세요: ")))
    
print(f"""
[원본 리스트]
{num}

1. 처음 5개 원소:
{num[:5]}

2. 뒤에서 3개 원소
{num[-3:]}

3. 짝수 인덱스 출력
{num[0:11:2]}

4. 거꾸로 뒤집은 리스트
{num[::-1]}""")
