n = int(input("Enter dividend :"))
m = int(input("Enter divisor :"))

def find(n, m):
    # for quotient
    q = n // m
    print("The quotient is:", q)

    # for remainder
    r = n % m
    print("The remainder is:", r)


# Driver Code
find(n, m)