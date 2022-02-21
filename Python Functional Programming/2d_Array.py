def array2D():
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