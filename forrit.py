from math import factorial

def C(n,k):
	return factorial(n)//(factorial(k)*factorial(n-k))

