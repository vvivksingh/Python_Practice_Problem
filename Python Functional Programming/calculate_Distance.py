import math
def findDistance():
    x = int(input("Enter the x-value :"))
    y = int(input("Enter the y-value :"))
    distance =math.sqrt(math.pow(x, x)+math.pow(y, y))
    print("Euclidean Distance :", distance)
findDistance()