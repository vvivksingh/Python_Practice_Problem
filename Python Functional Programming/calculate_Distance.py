import math


def findDistance():
    """
    taking input as coordinates of x and y axis and based on that using
    Euclidean formula calculate the distance
    :return: the Euclidean distance
    """
    x = int(input("Enter the x-value :"))
    y = int(input("Enter the y-value :"))
    distance = math.sqrt(math.pow(x, x) + math.pow(y, y))
    print("Euclidean Distance :", distance)


findDistance()
