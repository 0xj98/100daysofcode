# nested if -else
height = int(input("enter your height"))
if height >= 120:
    print("welcome to the ride")
    age = int(input("your age?"))
    if age < 12:
        print("pay $5")
    elif age <= 18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("need to grow taller to ride")