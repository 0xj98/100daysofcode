import requests

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def convert_currency(amount, from_currency, to_currency):
    api_key = "" # from https://app.exchangerate-api.com/dashboard
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url + "?apikey=" + api_key)
        if response.status_code != 200:
            print("Error fetching currency data:", response.status_code)
            return amount

        data = response.json()
        rates = data.get('rates', {})
        converted_amount = amount * rates.get(to_currency, 0)
        if converted_amount == 0:
            print(f"Conversion rate not found for {to_currency}. Returning original amount.")
            return amount
        return converted_amount
    except Exception as e:
        print(f"An error occurred: {e}")
        return amount
    
def main():
    print("Tip Calculator")

    bill = get_float_input("What is the bill? ")
    tip_percentage = get_int_input("How much % would you like to tip? ")
    people = get_int_input("How many people would you be splitting the bill with? Type 1 if just yourself. ")

    total_bill_with_tip = bill + (bill * (tip_percentage / 100))

    is_converted = False
    if input("Do you want to convert the bill to another currency? (yes/no) ").lower() == 'yes':
        from_currency = input("Enter the current currency (e.g., USD): ").upper()
        to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
        converted_amount = convert_currency(total_bill_with_tip, from_currency, to_currency)
        if converted_amount != 0:
            print(f"Converted amount: {converted_amount} {to_currency}")
            total_bill_with_tip = converted_amount
            is_converted = True
        else:
            print("Conversion failed. Continuing with the original amount.")

    payment_per_person = total_bill_with_tip / people
    rounded_payment = round(payment_per_person, 2)

    currency = to_currency if is_converted else from_currency
    print(f"Each person should pay: {rounded_payment} {currency}")

if __name__ == "__main__":
    main()
