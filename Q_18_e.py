'''
18.e.  Using recursion , calculate the Geometric Sum upto 'n' terms. 
'''
#Taking common ratio as 0.5 and first term as 1.

def geometric_sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return 1+ 0.5*geometric_sum(n-1)

n = int(input("Enter the number of terms:"))
G_sum = geometric_sum(n)
print(f"The geometric sum upto {n} terms is: {G_sum}")
