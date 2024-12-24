#A program that generates a random password of a specified length.
import random
import string
size=int(input("Enter the size of password:"))
allchar=string.ascii_letters+string.digits+string.punctuation
password= ''.join(random.choice(allchar) for i in range(size))
print("The password is",password)