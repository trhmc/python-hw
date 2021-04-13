import os
import random
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

#I figured out that if I sorted both the word and the 'letter' in words, I could compare them easier
#first I have to define the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'
def first_step(word):
  stuffs = []
  for char in alphabet:
    neww = sorted((word) + char) #I add a char into the word to compare with each word in  words
    for letter in words:
      if len(letter) == (len(word) + 1):
        new = sorted(letter)
        if neww == new:
          stuffs.append(letter)
  return stuffs
#this function is very long because I have to compare each new word (neww) with all the words in the list

#This is my second way
#The function compares each word in the list to the targetted word instead of creating new combination for the targetted word
def step(word):
  stuffs = []
  count = 0
  for letter in words:
    if len(letter) == (len(word) + 1):
      new = letter
      for ch in word:
        if ch in new:
          new = letter.replace(ch,"",1) #letter needs to be omitted to avoid same characters
          count += 1
      if count == len(word):
        stuffs.append(letter)
      count = 0
  return stuffs
#This function is faster because it only needs to loop through the whole list one time

def kladders(word):
  if len(step(word)) == 0:
    return []
  else:
    many = step(word)
    return [word] + kladders(many[random.randint(0,len(many)-1)])

def longestladders(word):
  compare = 2
  for n in range(0,20):
    b = kladders(word)
    a = len(b)
    if a > compare:
      compare = a
      result = b
  return result

# import timeit
# print('first_step("APPLE") = ', end='')
# start = timeit.default_timer()
# print(first_step('APPLE'))
# print(f'First Step time: {(timeit.default_timer() - start):.5f} seconds')
# print('step("APPLE") = ', end='')
# start = timeit.default_timer()
# print(step('APPLE'))
# print(f'Step time: {(timeit.default_timer() - start):.5f} seconds')
# print('kladders("APPLE") = ', end='')
# start = timeit.default_timer()
# print(kladders('APPLE'))
# print(f'K Ladders time: {(timeit.default_timer() - start):.5f} seconds')
# print('longestladders("APPLE") = ', end='')
# start = timeit.default_timer()
# print(longestladders('APPLE'))
# print(f'Longest Ladders time: {(timeit.default_timer() - start):.5f} seconds')