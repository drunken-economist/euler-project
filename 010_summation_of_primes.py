# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import time

start = time.time()

def prime_sum(limit):
	prime_sum = 2
	for k in xrange(3, limit, 2): #build a primes array until it reaches the requested length
		if is_prime(k):
			prime_sum += k
	return prime_sum

def is_prime(numToTest): #only works for odd numbers, but it should only be passed odd numbers
	for i in xrange(3, int(math.sqrt(numToTest))+1, 2):
		if numToTest % i == 0:
			return False
	return True

print prime_sum(2000000)
print time.time() - start

#It takes 6.21 seconds. I should rewrite this in a sieve manner instead of checking all odd numbers