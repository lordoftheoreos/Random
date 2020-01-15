# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:50:51 2020

Inspired by the movie 'A Twelve Year Night' where the prisoners are in solitary 
confinement and are not allowed to talk to anyone. They discover that their cells 
are next to each other so they communicate via knocking, each number of knocks in 
a given interval representing an alphabet. In this way, you can form any message.

Constraints: other forms of punctuation than periods and capitalization
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("How many consecutive knocks in a long interval? i.e. # of sentences")
no_of_sentences = int(input())
n = 0
message = []

while n < no_of_sentences:
    print("Repeat for each sentence:")
    print("How many chains of consecutive knocks in a medium interval i.e. # of words?")
    no_of_words = int(input())
    j = 0
    sentence = []

    while j < no_of_words:
        print("Repeat for each word:")
  
        print("How many chains of consecutive knocks in a short interval? i.e. # of letters")
        no_of_letters = int(input())
        i = 0
        word = []
        while i < no_of_letters:
            print("What are the number of consecutive knocks? i.e. alphabet")
            knocks = int(input())
            letters = alphabet[knocks - 1]
            word.insert(i, letters)
            i = i + 1

        word = ''.join(word)
        sentence.insert(j, word)
        j = j + 1
    
    sentence = ' '.join(sentence)
    message.insert(n, sentence)
    n = n + 1
    
message = '. '.join(message)
print(message + '.')
