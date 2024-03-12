'''
30. WAP to check whether a list is sorted or not.
'''

#Using Built-in Function
'''
L1=list(map(int,input("Enter a comma-separated list of numbers: ").split(",")))
if L1==sorted(L1):
    print(f"{L1} is a sorted List.")
else:
    print(f"{L1} is not a sorted List.")
'''

L1=list(map(int,input("Enter a comma-separated list of numbers: ").split(",")))
n=len(L1)
s=1
for i in range(1,n):
    if L1[i-1]>L1[i]:
        print(f"{L1} is not a sorted List.")
        s=0
        break
if s!=0:
    print(f"{L1} is a sorted List.")
