import math


def quadraticEqnRoots(a, b, c):
    """

    :param a: a is the coefficient of x^2
    :param b: b is the coefficient of x
    :param c: c is the constant of the quadratic equation
    :return: this function return the roots of quadratic eqaaution using discriminant formula
    """
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Root1 is :", root1)
        print("Root2 is :", root2)
    if discriminant == 0:
        root1 = -b / (2 * a)
        root2 = -b / (2 * a)
        print("Root1 is :", root1)
        print("Root2 is :", root2)
    if discriminant < 0:
        print("Roots are imaginary")


a = int(input("Enter value for a :"))
b = int(input("Enter value for b :"))
c = int(input("Enter value for c :"))

if __name__ == '__main__':
    quadraticEqnRoots(a, b, c)
