"""
File: anagram.py
Name: Eric Liu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dictionary_words = set()      # set, It has all the words in dictionary.txt
permutation_words = set()     # set, It has all the words that you input and be permuted


def main():
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit) ')
    while True:
        print('-----------------------')
        word = input('Find anagram for: ').lower()   # can input uppers too.
        read_dictionary(word)
        if word == EXIT:
            break
        find_anagrams(word)

        # take the intersection with words in dict and words we permute
        print_words = sorted(dictionary_words.intersection(permutation_words))

        if len(print_words) == 0:
            print('No anagrams!')
        else:
            for w in print_words:
                print(f'\"{w}\"', end=', ')
            print(f'{len(print_words)} anagram(s) in total')


def read_dictionary(w):

    print('Searching...')  # avoid that users think the computer is crash
    with open('dictionary.txt', 'r') as f:
        global dictionary_words
        dictionary_words = set()
        l = []
        for ele in w:
            # if ele not in l:
            l.append(ele)
        for word in f:
            l2 = []
            word = word.strip('\n')
            for e in word:
                # if e not in l2:
                l2.append(e)
            if sorted(l) == sorted(l2):
                dictionary_words.add(word)
    ###########################
    # can do the assignment by only this
    ###########################


def find_anagrams(s):
    """
    :param s: str, the word you input
    :return: None
    """
    global permutation_words
    lst = []          # new word that permuted from letter_list
    letter_list = []  # stop ---> ['s', 't', 'o', 'p']
    permutation_words.clear()  # clear permutation words from previous run

    for letter in s:
        letter_list.append(letter)

    find_anagrams_helper(letter_list, lst)


def find_anagrams_helper(letters, lst):

    # Base case
    if len(lst) == len(letters):
        if sorted(letters) == sorted(lst):  # True--> means the the numbers of each litters in a word is the same
            w = ''                          # str will be add from element in lst
            for i in range(len(lst)):
                w += lst[i]
            if w not in permutation_words:
                permutation_words.add(w)
    else:
        # Recursion
        if has_prefix(lst, letters):
            for ele in letters:
                # choose
                lst.append(ele)

                # explore

                find_anagrams_helper(letters, lst)

                # un-choose
                lst.pop()


def has_prefix(lst, letters):
    s = ''
    if len(lst) < len(letters) / 2 + 1:

        for ltr in lst:
            s += ltr
    for ele in dictionary_words:
        if ele.startswith(s):
            return True
    return False


if __name__ == '__main__':
    main()
