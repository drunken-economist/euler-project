# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_no_rem(limitNum):
	testNum = limitNum
	while testNum > 0:
		if divisible_by_all(testNum, limitNum):
			return testNum
		testNum += limitNum #it has to be multiple of limitNum, obvy

def divisible_by_all(testNum, limitNum): #determines if the testNum is divisible by all ints between 2 and the limitNum
	for i in range(2,limitNum):
		if testNum % i != 0:
			return False
	return True

print smallest_no_rem(20)