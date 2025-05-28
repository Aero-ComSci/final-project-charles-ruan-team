ice_cream = {"Vanilla": 2.5, "Chocolate": 3.0}
cuisines = {
    "Latin": ["Pasta", "Tiramisu"],
    "Chinese": ["Dumplings", "Fried Rice"],
    "Spanish": ["Tacos", "Fajitas"],
    "French": ["Croissant", "Quiche"]
}

lang = input("Are you taking a language class? (yes/no): ")

if lang.lower() == "yes":
    which = input("Which language? (Latin/Chinese/Spanish/French): ")
    if which in cuisines:
        print("You get cuisine: " + cuisines[which][0] + ", " + cuisines[which][1])
    else:
        print("Language not found.")
else:
    print("Here are ice cream options:")
    for flavor in ice_cream:
        print("- " + flavor + ": $" + str(ice_cream[flavor]))
    choice = input("Which ice cream would you like?: ")
    if choice in ice_cream:
        print("You chose " + choice + " - $" + str(ice_cream[choice]))
    else:
        print("Not available.")


