print("Tip Calculator")

bill = float(input("What is the bill? $"))
tip_percentage = int(input("How much % would you like to tip?"))
people = int(input("How many people would you be splitting the bill with? Type 1 if just yourself."))

payment = (bill + (bill * (tip_percentage/100)))/people
rounded_payment = round(payment, 2)

print(f"Each person should pay ${rounded_payment}")