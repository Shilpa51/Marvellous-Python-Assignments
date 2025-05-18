import Arithmetic

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", Arithmetic.Add(x, y))
    print("Subtraction:", Arithmetic.Sub(x, y))
    print("Multiplication:", Arithmetic.Mult(x, y))
    print("Division:", Arithmetic.Div(x, y))

if __name__ == "__main__":
    main()
