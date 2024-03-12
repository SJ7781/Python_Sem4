'''
16.d. WAP to print the following pattern :

1
2 2
3 3 3
4 4 4 4
'''

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=' ')
    print()
