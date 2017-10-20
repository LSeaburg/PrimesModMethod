#!/usr/bin/python
from timeit import default_timer
from math import sqrt
start = default_timer()

def isDivisible(dividend, divisor):
	return dividend % divisor == 0

def isPrime(x, primesSoFar):
	for prime in primesSoFar:
		if isDivisible(x, prime):
			return False
		elif prime > sqrt(x):
			break
	return True


primes = [ ]

for x in range(2, 10000000):
	if x % 1000000 == 0: ##just a helpful output to see where the program is
		end = default_timer()
		print '{} in {} seconds'.format(x, end - start)
	if isPrime(x, primes):
		#print x
		primes.append(x)
# for prime in primes:
	# print prime
print('{} numbers were found in {} seconds'.format(len(primes), end - start))
