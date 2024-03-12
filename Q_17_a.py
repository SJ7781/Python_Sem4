'''
17.a. Write a function in python
that checks whether a given number is palindrome or not.
'''

def is_Palindrome(num):
    n=str(num)
    return n==n[::-1]

n=int(input("Enter a number to check: "))
if is_Palindrome(n):
    print(n,"is a Palindrome number.")
else:
    print(n,"is not a Palindrome number.")
    
