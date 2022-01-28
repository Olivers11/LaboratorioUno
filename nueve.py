def getCapital(c, a, y):
    return c / (a * y)


cant = int(input("Enter total to invest: "))
anual = float(input("Enter Yearly Interest Rate: "))
years = int(input("Years: "))

print(f"Capital: {getCapital(cant, anual, years)}")
