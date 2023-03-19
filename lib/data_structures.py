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
    food_names = [food.get("name") for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    i = 0
    while i < len(spicy_foods):
        name = spicy_foods[i].get("name")
        cuisine = spicy_foods[i].get("cuisine")
        spice = "🌶" * spicy_foods[i].get("heat_level")
        print(f"{name} ({cuisine}) | Heat Level: {spice}")
        i += 1

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    filter_foods = [food for food in spicy_foods if food.get("cuisine").lower() == cuisine.lower()]
    return filter_foods[0]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get("heat_level") > 5]
    i = 0
    while i < len(spiciest_foods):
        name = spiciest_foods[i].get("name")
        cuisine = spiciest_foods[i].get("cuisine")
        spice = "🌶" * spiciest_foods[i].get("heat_level")
        print(f"{name} ({cuisine}) | Heat Level: {spice}")
        i += 1

def get_average_heat_level(spicy_foods):
    i = 0
    for item in spicy_foods:
        i += item.get("heat_level")
    average = i/len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
