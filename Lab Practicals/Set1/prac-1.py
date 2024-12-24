#A program that converts temperatures from Fahrenheit to Celsius and vice versa.
while True:
    ch = int(input("\nEnter your choice: \n 1. Celsius to Fahrenheit\n 2. Fahrenheit to Celsius\n 3. Exit\n"))
    if ch == 1:
        cel = float(input("Enter temperature in Celsius: "))
        far = (cel * 9/5) + 32
        print("\nTemperature in Fahrenheit is: {:.2f} degree F".format(far))
    elif ch == 2:
        far = float(input("Enter temperature in Fahrenheit: "))
        cel = (far - 32) * (5/9)
        print("\nTemperature in Celsius is: {:.2f} degree C".format(cel))
    elif ch == 3:
        break
    else:
        print("\nInvalid choice")
