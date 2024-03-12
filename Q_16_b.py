'''
16.b. WAP to print the following pattern :

* * * *
* * *
* 
* 
'''

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=' ')
    print()
