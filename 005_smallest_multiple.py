# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_no_rem(limitNum):
	numToTest = limitNum #has to be larger than our limit
	for i in (range(2, limitNum)):
		if numToTest % i > 0:
			for j in range(2, limitNum):
				if (numToTest*j) % i == 0:
					numToTest *= j #iterate by the next number which mods to 0
					break
	return numToTest

print smallest_no_rem(20)