#!/usr/bin/python
def factorial(n):
    """
    @returns: factorial of n
    """
    acc = 1
    for i in range(1, n+1):
        acc *= i
    return acc


if __name__ == "__main__":
    result = factorial(12)
    print("result = " + str(result)) 

