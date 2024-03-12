'''
14. WAP to find whether a given number is an Armstrong number or not.
'''

n=int(input("Enter a number to check: "))

num=str(n)
num_digits=len(num)

ams_sum=0
for i in num:
    ams_sum+=int(i)**num_digits

if ams_sum==n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
    
