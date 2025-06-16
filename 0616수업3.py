bar = {"a" : 1, "b" : 2, "c" : 3}
foo = {"b" : 2, "a" : 5, "c" : 3, "d" : 10}

keys = ["a", "b"]

result = {k : v for k, v in bar.items()}
print(result)

result = {k : v for k, v in bar.items() if k not in keys}
print(result)