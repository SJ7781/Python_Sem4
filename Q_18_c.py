'''
18.c. Using recursion , write a program to print factorial of a given number.
'''

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number: "))
factorial=fact(n)
print(f"Factorial of {n} is {factorial}.")
