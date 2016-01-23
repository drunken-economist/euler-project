#https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sum_3_5(x):
	sum = 0
	for i in range(1, x):
		if check_mod_3_5(i):
			sum += i
	return sum

def check_mod_3_5(num):
	if num%3 == 0 or num%5 == 0:
		return True
	else:
		return False

print sum_3_5(1000)