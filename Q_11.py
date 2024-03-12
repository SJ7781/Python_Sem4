'''
11. WAP to find whether a given number is PALINDROME or not.
'''

n=int(input("Enter a number to check: "))
num=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
if num==rev:
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")


