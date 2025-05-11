#Write a progrm which contains one function that accept one number from user and return true if number is divisible by 5 otherwise return false.

def Div(no):
    if no % 5 == 0:
        print("Number is divisible by 5.")
        return True

    else:
        print("Number is not divisible by 5.")
        return False

print("Enter a number: ")
val = int(input())
Div(val)