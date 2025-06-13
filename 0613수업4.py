
bar = {"a" : 10, "b" : 20, "c" : 30}

def prt(**kwargs):
    for key in kwargs.keys():
        print(f"Key: {key}")

prt(**bar)

# for item in bar: # key 값만
#     print(item)

# for key in bar.keys(): # key 값만
#     print(f"Key: {key}")
    
# for item in bar.values(): # value만
#     print(f"Item: {item}")
    
# for key, item in bar.items(): # items() -> 키와 값 둘 다 가져옴
#     print(f"Key: {key}, Item: {item}")