def array2D():
    """
    --> taking number of rows and number of column as input from the
        user and create a 2d arrow based on input, also taking input as
        element of the array
    :return: the 2d array of specified input
    """
    mrows = int(input("Enter the number of rows"))
    ncolumns = int(input("Enter the number of columns"))
    arr = []
    for i in range(mrows):
        col = []
        for j in range(ncolumns):
            col.append(int(input("Enter the number")))
        arr.append(col)
    print(arr)


array2D()
