items = [123,63,3225,564,3,235,6,4,435]


def discount(x, percentage=.10):
	return x-(x*percentage)

print(list(map(discount, items)))
