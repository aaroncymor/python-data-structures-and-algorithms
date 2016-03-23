def fib_rec(n):
	if n == 0:
		return 0
	elif n < 3:
		return 1
	return fib_rec(n - 1) + fib_rec(n - 2)

n = 10
cache = [None] * (n + 1)

def fib_dyn(n):
	if n == 0:
		return 0
	elif n < 3:
		return 1

	if cache[n - 3]:
		print "HAHA"
		return cache[n - 3]

	x = fib_rec(n - 1) + fib_rec(n - 2)
	cache[n - 3] = x
	return x


def fib_iter(n):
	fib = [0,1,1]
	if n < 3:
		return fib[n]
	elif n == 3:
		return fib[n - 2] + fib[n - 1]

	for i in range(3,n + 1):
		fib.append(fib[i - 2] + fib[i - 1])

	return fib[-1]

print fib_iter(10)