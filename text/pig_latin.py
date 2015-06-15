"""
Pig Latin Translator
Created: 6/15/2015
"""

SUFFIX = 'ay'

def main():
	# Prompt the user for English words
	words_to_translate = raw_input("Please enter words you would like to translate to Pig Latin then hit enter:\n").split()
	translated_words = []
	for word in words_to_translate:
		punctuation = ''
		if not word[-1].isalpha(): #check for punctuation
			# if there is punction, move to the end of the word
			punctuation = word[-1]
			word = word[:-1]
			
		translated_words.append(word[1:]+word[0]+SUFFIX+punctuation)

	print ' '.join(translated_words)

if __name__ == '__main__':
	main()