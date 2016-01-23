# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13
# What is the 10,001st prime number?
import time, math
s = time.time()

def nth_prime(n):
	primes = [2] #easier than writing the exception for 2
	k = 3
	while len(primes) < n: #build a primes array until it reaches the requested length
		if is_prime(k):
			primes.append(k)
		k += 2 #checking all odd numbers
	return primes[n-1]

def is_prime(numToTest): #only works for odd numbers, but it should only be passed odd numbers
	for i in xrange(3, int(math.sqrt(numToTest))+1, 2):
		if numToTest % i == 0:
			return False
	return True

print nth_prime(10001)
print time.time()-s

#So I should probably use a sieve method for this, but this works 