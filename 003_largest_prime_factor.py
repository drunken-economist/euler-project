# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def largest_prime(num):
	maxPrime = 2
	while num % 2 == 0:  
		num = num/2
		#if 2 is a divisor (or dividend? I can't remember which is which), divide by two until it's not
	prime = 3
	while num != 1:
		while num % prime == 0:
			maxPrime = prime
			num = num/prime
		prime += 2 #try next odd number
	return maxPrime
print largest_prime(600851475143)