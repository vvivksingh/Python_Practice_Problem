def swap_numbers(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp

    print("After swaping: num1 = {0} and num2 = {1}".format(number1, number2))


num1 = int(input(" Please Enter the First Value : "))
num2 = int(input(" Please Enter the Second Value : "))

print("Before swaping: num1 = {0} and num2 = {1}".format(num1, num2))

if __name__ == '__main__':
    swap_numbers(num1, num2)