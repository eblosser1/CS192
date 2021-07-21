def GetHeight():
    Height = input("Please enter student's height in inches: ")
    return int(Height)


def GetWeight():
    Weight = input("Please enter student's weight in pounds: ")
    return int(Weight)


def CalculateBMI(Weight, Height):
    BMI = round(Weight * 703 / Height ** 2, 1)
    return BMI


def PrintInfo(Weight, Height, BMI):
    print("Height: ", Height, "\"")
    print("Weight: ", Weight, "lbs.")
    print("BMI Index: ", BMI)


print("Welcome to the BMI Index Calculator.")
Name = input("Please begin by entering the student's name or 0 to quit: ")
while Name != "0":
    Height = GetHeight()
    Weight = GetWeight()
    BMI = CalculateBMI(Weight, Height)
    print(Name, "'s BMI profile:")
    print("-----------------")
    PrintInfo(Weight, Height, BMI)
    Name = input("Enter the next student's name or 0 to quit:")
    if Name == "0":
        print("Exiting program...")
        break



