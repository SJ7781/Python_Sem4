'''
9. WAP to find the sum of digits of a given number.
'''

n=int(input("Enter a number:"))
num=n
Sum=0
while n>0:
    Sum+=n%10
    n//=10
print(f"Sum of digits of the number {num} is {Sum}.")
    
