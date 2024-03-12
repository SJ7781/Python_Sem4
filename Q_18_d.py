'''
18.d. Using recursion , print the first 'n' terms of Fibonacci Series.
'''

def fib(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_series=fib(n-1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series

n = int(input("Enter the number of terms: "))
fibs = fib(n)
print(f"The first {n} terms of the Fibonacci series are: {fibs}.")
