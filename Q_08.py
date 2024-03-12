'''
8. WAP to find the factorial of a given number.
'''

n=int(input("Enter a non-negative number: "))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"Factorial of {n} is {factorial}.")
