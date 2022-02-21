"""
--> taking input from the user and printing its prime factor
"""
x = int(input("Enter any number to get its prime factor"))
i = 2
while x != 1:
    if x % i == 0:
        print(i, end=" ")
        x = x//i
    else:
        i = i+1


