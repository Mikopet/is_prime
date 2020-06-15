import math
#proba teszt
def is_prime(n):
	if n == 1: 
		return False
	elif n < 4:
		return True
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		r = math.isqrt(n)
		f = 5
		while f <= r:
			if n % f == 0: 
				return False
			if n % (f+2) == 0:
				return False
			f += 6
		return True

print(is_prime(1234567))
print(is_prime(1234657))
print(is_prime(123465763859374657))