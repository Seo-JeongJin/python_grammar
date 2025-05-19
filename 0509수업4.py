
foo = [10, 20, 30, 50]

foo.append(300) # Create [10, 20, 30, 50] -> [10, 20, 30, 50, 300]
 
print(foo[0]) # Read

foo[2] = 200 # Update

del foo[1] # Delete [10, 20, 30, 50, 300] -> [10, 30, 50, 300]