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
    name_list = []
    for food in spicy_foods:
        name_list.append(food["name"])
    return name_list

def get_spiciest_foods(spicy_foods):
    spiciest_list = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    pepper = '🌶'
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * pepper}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if(food["cuisine"] == cuisine):
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_list)

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat = total_heat + food["heat_level"]
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

