'''
20. WAP to find the smallest and largest element in a numeric list
    without using the built-in functions.
'''

L1=list(map(int,input("Enter a comma-separated list of numbers: ").split(",")))

Min=Max=L1[0]
for i in L1:
    if i<Min:
        Min=i
    if i>Max:
        Max=i

print(f"Smallest element in the given list is: {Min}.")
print(f"Largest element in the given list is: {Max}.")
