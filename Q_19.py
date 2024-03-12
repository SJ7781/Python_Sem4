'''
19. WAP to add all the items of a numeric list.
'''
L1=list(map(int,input("Enter a comma-separated list of numbers: ").split(",")))
Sum=0
for i in L1:
    Sum+=i
print("Sum of all the items in the given list is:",Sum)
