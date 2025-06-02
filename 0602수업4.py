
def prt_elements(*args):
	last_index = len(args) - 1
	msg = "["
	
	for idx, val in enumerate(args):
		msg += str(val) + ", " if idx != last_index else str(val)
	msg += "]"
	
	print(msg) 

prt_elements()
prt_elements(1)
prt_elements(1, 100)
prt_elements(1, 100, 2, 300)



def prt_elements(a, b, c, d, *e):
	print(a, b, c, d, e)

prt_elements(1, 2, 3, 4, 5, 6, 7)



def prt_elements(a, b, c, *d, e = 1000):
	print(a, b, c, d, e)

prt_elements(1, 2, 3, 4, 5, 6, 7)