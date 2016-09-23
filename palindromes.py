"""
Problem:

    A palindrome is a number or word that reads the same forwards as backwards,
    such as "mum", "racecar" or 12321.

    The function palindromic takes a 3-digit number and should print "Yes"
    if a number is palindromic, and "No" if it isn't.

Tests:

    >>> palindromic(121)
    Yes
    >>> palindromic(575)
    Yes
    >>> palindromic(999)
    Yes
    >>> palindromic(234)
    No
    >>> palindromic(741)
    No

"""

# Use this to test your solution. Don't edit it! 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True) 
 
 
# Edit this function 
def palindromic(n):

    x = n // 100
    y = n % 100
    z = y % 10 

    if x == z:
        print("Yes")

    else:
        print("No")

