'''
6. WAP to find whether a given number is prime or compostie.
'''

n=int(input("Enter a number to check: "))
if n<2:
    print(n,"is neither prime nor composite.")
elif n==2:
    print("2 is a prime number.")
else:
    root_n=int(n**0.5)
    for i in range(2,root_n+1):
        if n%i==0:
            print(n,"is a composite number.")
            break
    else:
        print(n,"is a prime number")


    
