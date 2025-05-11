#Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even it should display "Even number" otherwise it should display "Odd number" on the console.

def ChkNum(no):
    if no%2 == 0:
        print("It is an even number.")
    else:
        print("It is an Odd number.")

print("Enter a number: ")
val = int(input())
ChkNum(val)