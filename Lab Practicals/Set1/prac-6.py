#A program that calculates the factorial of a number.
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)

def main():
    num=int(input("Enter a number: "))
    if num<0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = fact(num)
        print(f"The factorial of {num} is {result}")


main()