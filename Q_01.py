'''
1. WAP to illustrate all arithmetic operators.
'''

print("PROGRAM TO ILLUSTRATE ARITHMETIC OPERATORS : \n")

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=float(input("Enter a decimal number: "))

print()

print("Sum:")
print(f"{a}+{b}={a+b}")
print(f"{a}+{c}={a+c}")
print()

print("Difference:")
print(f"{a}-{b}={a-b}")
print(f"{a}-{c}={a-c}")
print()

print("Product:")
print(f"{a}*{b}={a*b}")
print(f"{a}*{c}={a*c}")
print()

print("Quotient:")
print(f"{a}/{b}={a / b}")
print(f"{a}/{c}={a / c}")
print()

print("Floor Division:")
print(f"{a}//{b}={a // b}")
print(f"{a}//{c}={a // c}")
print()

print("Remainder/Modulo(%):")
print(f"{a}%{b}={a % b}")
print(f"{b}%{a}={b % a}")

