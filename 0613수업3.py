bar = {"std1":10, "std2":20, "std3":30}

# Create
print(bar.setdefault("std4", 200))
print(bar.setdefault("std1", 100))
print(bar)

# Read
print(bar.get("std4"))
print(bar.get("std1"))
print(bar.get("std5", False))

# Update
bar["std2"] = 100
print(bar)

# Delete
bar = {"std1":10, "std2":20, "std3":30}

del bar["std2"] 
print(bar.pop("std3")) # 30 -> 값을 삭제 후 반환
print(bar.pop("std4", False)) # False
print(bar) # {'std1': 10}