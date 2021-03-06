"""
Vowel Counter
Created: 06/15/2015
"""
from collections import Counter

VOWELS = 'AEIOU'

def main():
	# Prompt the user for a string
	input_string = raw_input('Please enter a string and hit enter:\n')
	
	# Place all the characters into a dictionary
	# Convert to lower case (so that 'A' is counted as 'a')
	char_dict = Counter(input_string.lower())
	print "\nThe numbers of vowels in your string:"
	
	total = 0
	for vowel in VOWELS:
		total += char_dict[vowel.lower()]
		print vowel + ':', char_dict[vowel.lower()]

	print 'Total number of vowels in your string:', total

if __name__ == '__main__':
	main()