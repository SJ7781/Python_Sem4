'''
17.b. Write a function in python
that returns the sum of first 'n' natural numbers.
'''

def sum_n(n):
    return ((n)*(n+1))//2

n=int(input("Enter a number: "))
Sum=sum_n(n)
print(f"Sum of first {n} natural numbers is {Sum}.")
