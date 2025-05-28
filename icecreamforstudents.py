def get_valid_input(prompt, options):
    while True:
        answer = input(prompt).strip().title()
        if answer in options:
            return answer
        else:
            print("Invalid option. Try again.")

vacations = {
    "Italy": {
        "Cuisine": ["Pasta", "Tiramisu"],
        "Hotel": "Roma Grand Hotel",
        "Flight": 850
    },
    "China": {
        "Cuisine": ["Dumplings", "Fried Rice"],
        "Hotel": "Beijing Palace",
        "Flight": 950
    },
    "Mexico": {
        "Cuisine": ["Tacos", "Fajitas"],
        "Hotel": "Cancun Beach Resort",
        "Flight": 720
    },
    "France": {
        "Cuisine": ["Croissant", "Quiche"],
        "Hotel": "Paris Luxury Inn",
        "Flight": 890
    }
}

ice_cream = {
    "Vanilla": 2.5,
    "Chocolate": 3.0
}

print("🌞 You are on summer vacation! 🌴")

travel = get_valid_input("Do you want to travel? (Yes/No): ", ["Yes", "No"])

if travel == "Yes":
    print("\nWhere would you like to go?")
    for place in vacations:
        print("- " + place)
    
    choice = get_valid_input("Choose your destination: ", vacations.keys())
    info = vacations[choice]
    print("\n🏖️ Vacation Plan for " + choice + ":")
    print("Hotel: " + info["Hotel"])
    print("Flight Cost: $" + str(info["Flight"]))
    print("Cuisine: " + info["Cuisine"][0] + ", " + info["Cuisine"][1])
else:
    print("\nNo problem! Enjoy some ice cream instead:")
    for flavor in ice_cream:
        print("- " + flavor + ": $" + str(ice_cream[flavor]))
    
    pick = get_valid_input("Which one would you like?: ", ice_cream.keys())
    print("You chose " + pick + " - $" + str(ice_cream[pick]))


