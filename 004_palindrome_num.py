

def palindrome():
	num1 = 100
	while num1 <= 999:
		num2 = 100
		while num2 <= 999:
			numToCheck = num1 * num2
			if numToCheck < 100000:
				if numToCheck % 10000 == numToCheck and numToCheck % 1000 == numToCheck % 10:
					largestPalindrome = numToCheck
			elif numToCheck % 100000 == numToCheck and numToCheck % 10000 == numToCheck % 10 and numToCheck % 1000 == numToCheck % 100:
				largestPalindrome = numToCheck
	return largestPalindrome
print palindrome()