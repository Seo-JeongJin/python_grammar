today = "수요일"
if today == "월요일":
    print("출근해야지.")
elif today == "일요일":
    print("오늘은 쉬는 날")
else:
    print("무슨 요일이지?")    
    
    
today = 29
if today < 30:
    print("아직 돈이 없네..")
elif today == 30:
    print("돈 들어오는 날!")    
else:
    print("오늘 무슨 요일이지?")    
    
    
pizza = False # pizza = " " 빈칸도 존재를 하는거임 -> 피자다!!가 출력, 0 이외의 숫자형도 가능
hamburger = True
if pizza:
    print("피자다!!")
elif hamburger:
    print("햄버거다!")
else:
    print("배고파")        
    
pizza = False
hamburger = True
if pizza and hamburger: # 둘 다 true일 때 출력
    print("피자랑 햄버거다")
if pizza or hamburger:
    print("피자랑 햄버거다") # 둘 중 하나만 true여도 출력
if not pizza:
    print("피자다!!") # 피자가 false일 때 출력
    
    
