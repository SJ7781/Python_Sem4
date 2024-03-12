'''
22. Write a Python program to create a list
    by concatenating a given list with a range from 1 to n. 
    Sample list : ['p', 'q'] 
    n =5 
    Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''

L1=[char.strip() for char in input("Enter a comma-separated list: ").split(",")]

n = int(input("Enter the value of n: "))
final_list = [f'{char}{i}' for i in range(1, n + 1) for char in L1]
print("Required List: ",final_list)
