
bar = [val for val in range(1, 11, 2)] # [1, 3, 5, 7, 9]

# list를 복사하는 방법 3가지
foo = list(bar) 
pos = bar.copy()
kin = bar[:] # Slicing -> 실무에서 주로 활용됨

bar[0] = 100
print(foo) # [1, 3, 5, 7, 9]
print(pos) # [1, 3, 5, 7, 9]
print(kin) # [1, 3, 5, 7, 9]