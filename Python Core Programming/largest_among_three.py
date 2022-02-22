"""
--> taking three integer input from the user and printing which one is largest
    among them.
"""
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3

if __name__ == '__main__':
    print(f"The largest number among {num1} {num2} {num3} is", greatest)
