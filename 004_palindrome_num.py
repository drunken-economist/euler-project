

def palindrome():
	num1 = 999
	lowerLimitNum = 100
	largestPalindrome = 0
	while num1 >= lowerLimitNum:
		num2 = 999
		while num2 >= lowerLimitNum:
			numToCheck = num1 * num2
			print num1 , " * " , num2 , " = " , numToCheck
			if str(numToCheck) == str(numToCheck)[::-1]: #convert to string, check if the inversion matches
				if numToCheck > largestPalindrome:
					largestPalindrome = numToCheck
				#lowerLimitNum = num2 #we found a palindrome at this factor, so we don't need to checl lower than it anymore
			num2 -= 1
		num1 -= 1
	return largestPalindrome
print palindrome()