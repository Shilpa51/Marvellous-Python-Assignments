class Numbers:
    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.Value == self.SumFactors()

    def Factors(self):
        print(f"Factors of {self.Value}: ", end="")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum


# Using the class
num = Numbers()
print("Is Prime?" , num.ChkPrime())
print("Is Perfect?" , num.ChkPerfect())
num.Factors()
print(f"Sum of Factors: {num.SumFactors()}")
