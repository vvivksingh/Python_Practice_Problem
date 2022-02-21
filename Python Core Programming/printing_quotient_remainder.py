dividend = int(input("Enter dividend :"))
divisor = int(input("Enter divisor :"))


def find(dividend, divisor):
    """

    :param divisor: integer type
    :type dividend: integer parameter
    """
    # for quotient
    q = dividend // divisor
    print("The quotient is:", q)

    # for remainder
    r = dividend % divisor
    print("The remainder is:", r)


# Driver Code
find(dividend, divisor)
