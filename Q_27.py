'''
27. WAP to find numbers of a list that are divisible by a particular element.
'''

L1 = list(map(int, input("Enter a comma-separated list of numbers: ").split(',')))
n=int(input("Enter a number: "))

new_List = list(filter(lambda x:x%n==0,L1))
print(f"Numbers in the list divisible by {n}: {new_List}")
