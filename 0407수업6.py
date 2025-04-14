
record = 70

if record >= 90:
    print("A")
elif record >= 80: # 이미 if 문에서 90이상이 아니라는 것을 알았기 때문에 이 elif 문에서는 record가 90 미만 이라는 것을 자동으로 깔고 감. 90 > record >= 80 이라는 게 필요가 없다.
    print("B")
elif record >= 70:
    print("C")
elif record >= 60:
    print("D")
else:
    print("F")
