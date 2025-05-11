#Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkNum(no):
    if no > 0:
        print("It is a positive number.")
    elif no < 0:
        print("It is a negative number.")
    else:
        print("It is zero.")

print("Enter a number: ")
val = int(input())
ChkNum(val)