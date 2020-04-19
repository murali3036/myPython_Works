#Write a program to print the:
#a.Number of lowercase “a” and “o” in the following sentence.
#b.Number of uppercase “L” and “N” in the following sentence.

#‘Discover, Learning, with, Edureka’

def noOfLetters(text,*args):
    for i in args:
        print("Number of lowercase “{}” in the following sentence: {}".format((i),text.count(i)))

noOfLetters("‘Discover, Learning, with, Edureka’",'a','o')

