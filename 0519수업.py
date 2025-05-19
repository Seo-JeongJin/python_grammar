
# List Comprehension

bar = [val for val in range(1, 11, 2)]

print(bar) # [1, 3, 5, 7, 9]

# Chaining
pos = foo = bar # bar의 값을 foo에, foo 값을 pos에

pos[0] = 10
print(pos) # [10, 3, 5, 7, 9]
foo[-1] = 100
print(foo) # [10, 3, 5, 7, 100]