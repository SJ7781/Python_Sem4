'''
4. WAP to find whether a given year is leap year or not.
'''

year=int(input("Enter year to check: "))
if year%100!=0 and year%4==0 or year%400==0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
