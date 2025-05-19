
num_list = []

count = 0

while count < 5:
    option = int(input("""
작업을 선택하세요: 
1. 추가 (Create)
2. 조회 (Read)
3. 수정 (Update)
4. 삭제 (Delete)
5. 종료 (Exit)
입력: """))

    print()

    if option == 1:
        add = int(input("추가할 값을 입력하세요: "))
        num_list.append(add)
        print("추가 완료.")

    elif option == 2:
        print("[현재 리스트 내용]")
        for i in range(len(num_list)):
            print(f"{i}: {num_list[i]}")

    elif option == 3:
        modify_index = int(input("수정할 인덱스를 입력하세요: "))

        if 0 <= modify_index < len(num_list):
            new_value = int(input("새로운 값을 입력하세요: "))
            num_list[modify_index] = new_value
            print("수정 완료.")
        else:
            print("유효하지 않은 인덱스입니다.")

    elif option == 4:
        remove_index = int(input("삭제할 인덱스를 입력하세요: "))

        if 0 <= remove_index < len(num_list):
            del num_list[remove_index]
            print("삭제 완료.")
        else:
            print("유효하지 않은 인덱스입니다.")

    elif option == 5:
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 번호를 입력하세요.")
    
    count += 1