"""
Palindrome Checker
Created: 06/15/2015
"""

import string

def main():
	# Prompt user for input string
	input_string = raw_input("Please enter a string and hit enter:\n")
	# strip all punctuation from the string
	cleaned_string = input_string.translate(string.maketrans("",""), string.punctuation)
	# remove whitespaces
	cleaned_string = cleaned_string.replace(' ', '')
	
	# check if the string is a palindrome
	if cleaned_string == cleaned_string[::-1]:
		print 'You entered a Palindrome!!!'
	else:
		print 'This is not a Palindrome...'

if __name__ == '__main__':
	main()
