'''
16.e. WAP to print the Pascal's Triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end='')
    num=str(11**i)
    for k in range(len(num)):
        print(num[k],end=' ')
    print()










                   
