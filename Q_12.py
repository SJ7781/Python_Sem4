'''
12. WAP to print Fibonacci Series upto 'n' terms.
'''

n=int(input("Enter a number: "))
if n<=0:
    fib_series = []
elif n==1:
    fib_series = [0]
else:
    fib_series = [0,1]
    for i in range(2,n):
        fib_series.append(fib_series[-1]+fib_series[-2])
print("Required Fibonacci Series :",fib_series)
