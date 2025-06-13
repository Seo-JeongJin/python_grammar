
# bar = []
# bar[0] = 10
# print(bar) # Error

foo = {}
foo[0] = 10
foo["0"] = 20
foo[0.0] = 30
foo[True] = 40
foo[(1, 2)] = 50

print(foo)