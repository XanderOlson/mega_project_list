"""
Reverse a String
Created 6/15/2015
"""

def main():
	#Prompt user for a string
	input_string = raw_input("Please enter a string then hit 'Enter':\n")

	print "\nReversing the string...\n" # Short status bar with spacing

	print "Your reversed string:\n" + input_string[::-1] # Print reversed string

if __name__ == '__main__':
	main()