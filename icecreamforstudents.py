ice_cream = {"Vanilla": 2.5, "Chocolate": 3.0}
cuisines = {
    "Latin": ["Pasta", "Tiramisu"],
    "Chinese": ["Dumplings", "Fried Rice"],
    "Spanish": ["Tacos", "Fajitas"],
    "French": ["Croissant", "Quiche"]
}

students = {
    "Alice": ["Math", "Latin"],
    "Bob": ["French", "History"],
    "Charlie": ["Art", "Chinese"]
}

for name in students:
    print(name + ":")
    for course in students[name]:
        if course in cuisines:
            print("  " + course + ": " + cuisines[course][0] + ", " + cuisines[course][1])
        else:
            print("  " + course + ": Vanilla $" + str(ice_cream["Vanilla"]) + ", Chocolate $" + str(ice_cream["Chocolate"]))

