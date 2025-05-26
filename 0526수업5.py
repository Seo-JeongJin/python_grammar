
bar = [1, 2, 3]
foo = (4, 5, 6)

print(bar, type(bar), bar[1])
print(foo, type(foo), foo[1])

bar.append(100)
foo.append(200) # Error

# Type of tuple cannot update and delete