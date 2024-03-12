'''
21. WAP to remove duplicates from a given list.
'''

#USING SET
'''
L1=list(map(str,input("Enter a comma-separated list of numbers: ").split(",")))
L1=list(set(L1))
print("List after removing duplicates: ",L1)
'''

L1=list(map(str,input("Enter a comma-separated list of numbers: ").split(",")))
new_List=[]
for i in L1:
    if i not in new_List:
        new_List.append(i)
L1=new_List
print("List after removing duplicates:",L1)



