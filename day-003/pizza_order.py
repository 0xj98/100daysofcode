print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
cost = 0
if size == "S":
  if add_pepperoni == "Y":
    cost += 2
  cost += 15
elif size == "M":
  if add_pepperoni == "Y":
    cost += 3
  cost += 20
else:
  if add_pepperoni == "Y":
    cost += 3
  cost += 25

if extra_cheese == "Y":
  cost += 1

print(f"Your final bill is: ${cost}.")
