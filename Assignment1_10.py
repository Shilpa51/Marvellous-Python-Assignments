#Write a program which accepts name from user and display length of its name

def Display(data):
    print("Length of the name is: ",len(data))

print("Enter your name: ")
name = str(input())
Display(name)