'''
26. WAP to display all the numbers of a list with powers of 2
    using lambda function.
'''

L1=list(map(int,input("Enter a comma-separated list of numbers: ").split(",")))
new_List=list(map(lambda x:2**x,L1))
print("New list with powers of 2: ",new_List)
        
