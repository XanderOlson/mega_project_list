"""
Regex Query Tool
Creeated: 06/16/2015
"""

import re

def main():
	# Query the user for text string input
	input_string = raw_input("Please type in a string and hit enter:\n")
	
	# print a line break to help with readability
	print ''
	
	# Prompt the user for regex pattern
	pattern = raw_input("Please type in a regex pattern and hit enter:\n")

	find_obj = re.findall(pattern, input_string)

	if find_obj:
		print 'The following matches were found:'
		for match in find_obj:
			print match
	else:
		print "The Regex pattern was not found in the string."

if __name__ == '__main__':
	main()