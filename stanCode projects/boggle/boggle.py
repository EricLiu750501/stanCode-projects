"""
File: boggle.py
Name: Eric Liu
----------------------------------------
the program can solve the boggle game!
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
dictionary_words = set()  # set, It has all the words in dictionary.txt
walk_pass_word = set()    # set, It has all the words searched by play_boggle method from the boggle you input


def main():
	"""
	1. demand users input the boggle
	2. let te program play the boggle!
	"""
	can_play_boggle = True
	data = []  # It save the data that you input (format is like line 24~28)

	# data = [['f', 'y', 'c', 'l'],
	# 			['i', 'o', 'm', 'g'],
	# 			['o', 'r', 'i', 'l'],
	# 			['h', 'j', 'h', 'u']]

	for i in range(1, 5):
		s = input(f'{i} row of letters:')
		lst = s.split(' ')
		lst = list(e.lower() for e in lst)
		if len(lst) != 4 or\
			False in list(map(lambda e: len(e) == 1, lst)) or\
			False in list(map(lambda e: e.isalpha(), lst)):
			print('illegal format!')
			can_play_boggle = False
			# line 33 : you have to input 4 ones that be split by ' '
			# line 34, 35 : ones must be a letter
			break
		data.append(lst)
# -----------------------------------------------------------------------
	if can_play_boggle:
		read_dictionary(data)

		for j in range(4):
			for i in range(4):

				# record that the letter if add in the word
				walked = [[False, False, False, False],
					[False, False, False, False],
					[False, False, False, False],
					[False, False, False, False]]

				# play from empty string
				play_boggle(data[j][i], '', data, i, j, walked)

		ans = walk_pass_word.intersection(dictionary_words)

		# print
		for ele in sorted(ans):
			print(f'Found  \"{ele}\"')
		print(f'There are {len(ans)} words in total.')


def play_boggle(letter, s, data, i, j, walked):
	"""
	:param letter: str, the first letter in s (start from it)
	:param s: word be walked
	:param data: nested list, letters you input named boggle
	:param i: int, col
	:param j: int, rows
	:param walked: nested list, record that the letter if add in the word
	:return: None
	"""
	# 1 2 3
	# 4 5 6
	# 7 8 9

	# explore
	if has_prefix(s):
		walked[j][i] = True
		s += data[j][i]
		if len(s) >= 4:
			walk_pass_word.add(s)
		if i-1 >= 0:

			if j-1 >= 0 and walked[j-1][i-1] is False:
				play_boggle(letter, s, data, i-1, j-1, walked)    # go to 1

			if walked[j][i-1] is False:
				play_boggle(letter, s, data, i-1, j, walked)      # go to 4

			if j+1 < 4 and walked[j+1][i-1] is False:
				play_boggle(letter, s, data, i-1, j+1, walked)    # go to 7

		if j-1 >= 0 and walked[j-1][i] is False:
			play_boggle(letter, s, data, i, j-1, walked)          # go to 2

		if j+1 < 4 and walked[j+1][i] is False:
			play_boggle(letter, s, data, i, j+1, walked)          # go to 8

		if i+1 < 4:

			if j-1 >= 0 and walked[j-1][i+1] is False:
				play_boggle(letter, s, data, i+1, j-1, walked)    # go to 3

			if walked[j][i+1] is False:
				play_boggle(letter, s, data, i+1, j, walked)      # go to 6

			if j+1 < 4 and walked[j+1][i+1] is False:
				play_boggle(letter, s, data, i+1, j+1, walked)    # go to 9

		# un_choose
		walked[j][i] = False


def read_dictionary(data):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	set1 = set()   # save letters you input

	# get letters from data
	for j in range(len(data)):
		for i in range(len(data[0])):
			set1.add(data[j][i])

	with open('dictionary.txt', 'r') as f:
		global dictionary_words
		for word in f:
			temp_set = set()   # It save letters from each word from dictionary
			word = word.strip('\n')
			if len(word) >= 4:   # because the program only search length-over-4 letters

				# e.g. 'apple'  --> {'a', 'p', 'p', 'l', 'e'}
				for temp_e in word:
					temp_set.add(temp_e)

				if temp_set <= set1:   # It means that each element in temp_set are all exist in set1
					dictionary_words.add(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ele in dictionary_words:
		if ele.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
