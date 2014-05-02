"""
Interview whiteboard questions from the following page:
http://meetupresources.herokuapp.com/whiteboard.html
"""

def int_to_roman(n):
    pass

def pig_latin(s):
    if not s:
        print 'Input cannot be an empty string'
        return s

    VOWELS = ['a','e','i','o','u','A','E','I','O','U']
    l = s[0]
    if l.alpha() == False:
        print 'The string does not start with a letter.'
        return
    if l in VOWELS:
        return s
    else: 
        return s[1:] + s[0] + 'ay'

def shuffle(arr):
    import random

    original_arr = arr
    shuffled_arr = []
    while len(original_arr) > 0:
        c = random.choice(original_arr)
        shuffled_arr.append(c)
        original_arr.remove(c) # removes only first occurance of c 
    return shuffled_arr


def anagrams_for(w,arr_w):
    """An anagram is a word formed by rearranging the letters of another word, e.g., iceman is an anagram of cinema. We're going to write a method called anagrams_for that takes as its input a word and an array of words, representing a dictionary, and returns an array consisting of all the anagrams of the input word. anagrams_for should return an empty array ([]) if no anagrams are found in the dictionary. You don't have to worry about the order of the returned Array. """
    anagrams = []

    word_dict = {}
    for l in w:
        if l in word_dict:
            word_dict[l] += 1
        else:
            word_dict[l] = 1
 
    for word in arr_w:
        current_dict = {}
        # build a dictionary for each word
        for l in word:
            if l in current_dict:
                current_dict[l] += 1
            else:
                current_dict[l] = 1

        # if two dicts are the same, then they are anagrams
        if word_dict == current_dict:
            anagrams.append(word)

    return anagrams

def factorial_recursive(n):
    if n < 0:
        return -1

    if n <= 1: 
        return 1

    return n*factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    
    while n > 0:
        result = result * n
        n -= 1
    return result


def linear_search(l,n):
    for i in rane(len(l)):
        if l[i] == n:
            return i
    return -1

def binary_search(l,n):
    lo = 0       # lo inclusive
    hi = len(l)  # hi exclusive

    while lo < hi:
        mid = (lo + hi)/2

        if n < l[mid]:
            hi = mid   
        elif n > l[mid]:
            lo = mid+1
        else:
            return mid
    
    return -1

def fibonacci_iterative(n):
    """return the nth Fibonacci number"""


def fibonacci_recursive(n):
    """return the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    if n > 1:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def apple_stock(stockPriceYesterday):
    """
    I have an array stockPricesYesterday where the keys are the number of minutes into the day (starting with midnight) 
    and the values are the price of Apple stock at that time. 
    For example, the stock cost $500 at 1am, so stockPricesYesterday[60] = 500. 
    Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of an Apple stock yesterday.
    """



    

