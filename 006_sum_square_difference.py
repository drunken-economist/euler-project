# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(limitNum):
	return (limitNum*(limitNum+1)*(2*limitNum+1))/6 #never let me say I didn't learn anything useful in high school

def square_of_sum(limitNum):
	return sum(xrange(1,limitNum+1))**2

def sum_square_diff(inputNum):
	if inputNum <= 0 or inputNum % 1 != 0:
		return "invalid input number"
	return square_of_sum(inputNum) - sum_of_squares(inputNum)

print sum_square_diff(100)