#Write a program which contains one function named as Add() which accepts two numbers from user and returnsaddition of that two numbers.

def Add(no1, no2):
    ans = 0
    ans = no1 + no2
    print("Addition is: ",ans)

print("Enter first number: ")
val1 = int(input())

print("Enter second number: ")
val2 = int(input())

Add(val1, val2)