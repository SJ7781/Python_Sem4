'''
18.b. Using recursion , write a program to convert decimal number to an octal number.
'''

def Dec_to_Oct(n):
    if n>7:
        Dec_to_Oct(n//8)
    x=(n%8)
    print(x,end='')

n=int(input("Enter a decimal number to convert: "))
print("Octal representation of",n,"is :",end=' ')
Dec_to_Oct(n)
