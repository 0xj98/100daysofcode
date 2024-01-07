import random

def get_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input.capitalize()
        else:
            print("Invalid input, please enter only letters.")

def generate_band_name(city, pet):
    adjectives = ["Groovy", "Electric", "Mystic", "Wild", "Jazzy"]
    adjective = random.choice(adjectives)
    return f"{adjective} {city} {pet}"

def main():
    print("Welcome to the Band Name Generator!")
    city = get_input("⦾ What city did you grow up in?\n")
    pet = get_input("⦾ What is the name of your pet?\n")
    
    name = generate_band_name(city, pet)
    print(f"⦾ Band name generated: {name}")

    with open("band_names.txt", "a") as file:
        file.write(name + "\n")
    print("Band name saved to 'band_names.txt'.")

if __name__ == "__main__":
    main()
