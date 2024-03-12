'''
15. WAP to print all PALINDROMES in the range of 500-1000.
'''

def is_Palindrome(num):
    n = str(num)
    return n == n[::-1]

print("Palindromes in the range of 500-1000 are as follows:")
for i in range(500,1001):
    if is_Palindrome(i):
        print(i,end=',')
