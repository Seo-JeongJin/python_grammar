
# (if), (if, else), (if, elif), (if, elif, else)
    # -> 결국 최대 선택은 1개만 한다.
# 최소 선택의 개수는 else에 의존한다. else가 있으면 무조건 1개는 선택한다.


for count in range(2):
    print(f"{count}번째 실행")
    

input_msg = ""
while input_msg != "yes":
    input_msg = input("입력 값: ")