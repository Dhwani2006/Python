#A program that converts a given number from one base to another.
def deci(val,ch):
    if ch==1:
        return val
    elif ch==2:
        return '{0:b}'.format(val)
    elif ch==3:
        return '{0:o}'.format(val)
    elif ch==4:
        return '{0:x}'.format(val)
    else:
        return "Invalid Choice"

def binary(val,ch):
    if ch == 1:
        return val
    elif ch == 2:
        return int(val,2)
    elif ch == 3:
        return '{0:o}'.format(int(val,2))
    elif ch == 4:
        return '{0:x}'.format(int(val,2))
    else:
        return "Invalid Choice"

def octal(val,ch):
    if ch == 1:
        return val
    elif ch == 2:
        return int(val,8)
    elif ch == 3:
        return '{0:b}'.format(int(val,8))
    elif ch == 4:
        return '{0:x}'.format(int(val,8))
    else:
        return "Invalid Choice"

def hex(val,ch):
    if ch == 1:
        return val
    elif ch == 2:
        return int(val,16)
    elif ch == 3:
        return '{0:0}'.format(int(val,16))
    elif ch == 4:
        return '{0:b}'.format(int(val,16))
    else:
        return "Invalid Choice"

print("1.Decimal \n2.Binary \n3.Octal \n4.Hexadecimal")
in_ch=int(input("Enter the choice"))
if in_ch==1:
    decinum=int(input("Enter decimal number"))
    print("Convert to:\n1.Decimal \n2.Binary \n3.Octal \n4.Hexadecimal")
    ch=int(input("Enter target conversion:\n"))
    print("Converted Value:",deci(decinum,ch))
elif in_ch==2:
    binarynum=int(input("Enter decimal number"))
    print("Convert to:\n1.Decimal \n2.Binary \n3.Octal \n4.Hexadecimal")
    ch = int(input("Enter target conversion:\n"))
    print("Converted Value:", binary(binarynum,ch))
elif in_ch==3:
    octnum=int(input("Enter decimal number"))
    print("Convert to:\n1.Decimal \n2.Binary \n3.Octal \n4.Hexadecimal")
    ch = int(input("Enter target conversion:\n"))
    print("Converted Value:", octal(octnum,ch))
elif in_ch==4:
    hexnum = int(input("Enter decimal number"))
    print("Convert to:\n1.Decimal \n2.Binary \n3.Octal \n4.Hexadecimal")
    ch = int(input("Enter target conversion:\n"))
    print("Converted Value:", hex(hexnum,ch))