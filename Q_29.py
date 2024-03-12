'''
29. WAP to print table of 10 upto user's choice
    using list comprehension and lambda function
'''

n=int(input("Enter a number: "))
table_of_10=list(map(lambda x:f"10 * {x} = {10*x}",range(1,n+1)))

print("\n".join(table_of_10))
