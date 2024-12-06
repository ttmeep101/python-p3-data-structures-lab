spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    foods = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            foods.append(food)
    return foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = food["heat_level"]
        heat_str = "🌶" * heat
        print(f"{name} ({cuisine}) | Heat Level: {heat_str}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat = food["heat_level"]
            heat_str = "🌶" * heat
            print(f"{name} ({cuisine}) | Heat Level: {heat_str}")

def get_average_heat_level(spicy_foods):
    avg = 0
    count = 0
    for food in spicy_foods:
        heat = food["heat_level"]
        avg += heat
        count += 1
    return avg / count

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
