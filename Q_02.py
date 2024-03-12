'''
2. WAP to illustrate all logical and relational operators.
'''

print("PROGRAM TO ILLUSTRATE LOGCIAL AND RELATIONAL OPERATORS : \n")

print("Logical Operators:")
a=True
b=False
c=True
d=False
print(f"a={a} , b={b} , c={c} , d={d}")

print("AND OPERATOR:")
print(f"{a} and {c} = {a and c}")
print(f"{a} and {b} = {a and b}")
print(f"{b} and {d} = {b and d}")
print()

print("OR OPERATOR:")
print(f"OR : {a} or {c} = {a or c}")
print(f"OR : {a} or {b} = {a or b}")
print(f"OR : {b} or {d} = {b or d}")
print()

print("NOT OPERATOR:")
print(f"NOT: not {a} = {not a}")
print(f"NOT: not {b} = {not b}")
print()

print("Relational Operators:\n")
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third nummber: "))
print()

print("Equal to(==):")
print(f"{a}=={b} : {a==b}")
print(f"{b}=={c} : {b==c}")
print()

print("Not Equal to(!=):")
print(f"{a}!={b} : {a!=b}")
print(f"{b}!={c} : {b!=c}")
print()

print("Greater than(>):") 
print(f"{a}>{b} : {a>b}")
print(f"{a}>{c} : {a>c}")
print()

print("Less than(<):")
print(f"{a}<{b} : {a<b}")
print(f"{a}<{c} : {a<c}")
print()

print("Greater than or equal to(>=):")
print(f"{a}>={b} : {a>=b}")
print(f"{a}>={c} : {a>=c}")
print()

print("Less than or equal to(<=):")
print(f"{a}<={b} : {a<=b}")
print(f"{a}<={c} : {a<=c}")
print()

print("USING LOGICAL AND RELATIONAL OPERATORS TOGETHER:")
print(f"{a}>{b} and {a}>{c} : {a>b and a>c}")
print(f"{a}>{b} or {a}>{c} : {a>b or a>c}")
print(f"{a}!={b} and {a}!={c} and {b}!={c} : {a!=b and a!=c and b!=c}") 

