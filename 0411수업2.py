
# Lazy evaluation
    # 표현식이 필요하지 않을 경우 평가하지 않음
    # 불필요한 계산을 피함으로써 성능을 향상 시킴
    
def return_num(arg_num):
    print("arg_num: ", arg_num, "\treturn_num() is invoked")
    return arg_num

return_num(1)

if True and return_num(2) == 2:
    print("True")
if False and return_num(3) == 2:
    print("True")
if True or return_num(4) == 4:
    print("True")
if False or return_num(5) == 4:
    print("True")