#A program that generates a multiplication table for a given number.
n=int(input("Enter the number to print it's table:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)