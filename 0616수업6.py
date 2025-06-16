bar = [10, 20, 30]

print(bar)

def foo(arg_list):
	arg_list[0] = 100

foo(bar)

print(bar) # [100, 20, 30]



kin = 3
def pos(arg):
    arg = 10
    
pos(kin)

print(kin) # 3