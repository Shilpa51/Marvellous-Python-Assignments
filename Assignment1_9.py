#Write a program to display first 10 even numbers on screen

def Display(no):
    print("First 10 even numbers are: ")
    for no in range(1, 21):
        if no%2 == 0:
            print(no)
            
val = 0
Display(val)
