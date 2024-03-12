'''
10. WAP to find the reverse of a given number.
'''

n=int(input("Enter a number: "))
num=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(f"Reverse of {num} is {rev}.")
