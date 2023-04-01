def calcTip (total, numPeople, tip):
    percent = tip/100
    totalWTip = total * (1+percent)
    return totalWTip/numPeople

print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? "))
numPeople = input("How many people to split the bill ")
tip = int(input("What percentage tip do you want to give? "))
amountPerPerson = calcTip(total, numPeople, tip)
print(f"Each person should pay: {amountPerPerson}")
