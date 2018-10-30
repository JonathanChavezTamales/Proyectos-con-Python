def ten(x):
	return x-x*.10

def st(func, x):
	return x-func(x)*.05

print(st(ten, 100))

