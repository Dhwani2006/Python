#A program that checks if a given string is a palindrome.
def is_palindrome(s):
    s=s.replace(" ", "").lower()
    return s==s[::-1]

def main():
    string = input("Enter a string: ")
    if is_palindrome(string):
        print("{} is a palindrome.".format(string))
    else:
        print("{} is not a palindrome.".format(string))



main()
