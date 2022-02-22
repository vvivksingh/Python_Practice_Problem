"""
-->taking integer input from the user and checking provided number
   is even or odd
"""


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")




