#A program that calculates the area and perimeter of a rectangle.
while True:
    print("\n 1.Area \n 2.Perimeter \n 3.Exit")
    op=int(input("\nEnter the choice:"))
    if op==1:
        A=L*W
        L=float(input("Enter the length:"))
        W=float(input("Enter the Width:"))
        print("\nArea of rectangle is:", A,"square units")
    elif op==2:
        P=2*(L+W)
        L=float(input("Enter the length:"))
        W=float(input("Enter the Width:"))
        print("\nPerimeter of rectangle is:", P," units")
    elif op==3:
        break
    else:
        print("\nInvalid Input!!!!")