
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

travel = input("Do you want to travel? (yes/no): ").strip().lower()

if travel == "yes":
    print("\nWhere would you like to go?")
    for place in vacations:
        print("- " + place)

    choice = input("Choose your destination: ").strip().title()

    if choice in vacations:
        info = vacations[choice]
        print("\n🏖️ Vacation Plan for " + choice + ":")
        print("Hotel: " + info["Hotel"])
        print("Flight Cost: $" + str(info["Flight"]))
        print("Cuisine: " + info["Cuisine"][0] + ", " + info["Cuisine"][1])
    else:
        print("Sorry, we don't have that destination.")
else:
    print("\nNo problem! Enjoy some ice cream instead:")
    for flavor in ice_cream:
        print("- " + flavor + ": $" + str(ice_cream[flavor]))

    pick = input("Which one would you like?: ").strip().title()
    if pick in ice_cream:
        print("You chose " + pick + " - $" + str(ice_cream[pick]))
    else:
        print("That flavor isn't available.")


