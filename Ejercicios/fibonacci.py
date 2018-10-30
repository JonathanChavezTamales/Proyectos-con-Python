""" Fibonacci recursivo (1+ 2 + 4 + 7 + 11) = (1 + n + n+1 + n+2) """


def fib(n):
	if n <=0:
		return 0
	else: 
		return n + fib(n-1)

print(fib(10)) 

