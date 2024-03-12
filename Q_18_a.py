'''
18.a. Using recursion , write a program to convert decimal number to a binary number.
'''

def Dec_to_Binary(n):
    if n>1:
        Dec_to_Binary(n//2)
    x=(n%2)
    print(x,end='')

n=int(input("Enter a decimal number to convert: "))
print("Binary representation of",n,"is :",end=' ')
Dec_to_Binary(n)


