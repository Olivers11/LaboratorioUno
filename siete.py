def getIMC(w, h):
    return w/(pow(h, 2))





weight = float(input("Enter your weight(Kg): "))
height = float(input("Enter your height(cm): "))
imc =getIMC(weight, height) 
print(f"Your IMC is: {round(imc, 2)}")
