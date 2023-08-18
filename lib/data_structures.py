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
    }
]


def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names
food_names = get_names(spicy_foods)
print(food_names)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods
spiciest_food_list = get_spiciest_foods(spicy_foods)
print(spiciest_food_list)

def get_spicy_food_by_cuisine(spicy_foods, target_cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == target_cuisine.lower():
            return food
    return None

# Example usage:
cuisine_to_search = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine_to_search)

if spicy_food:
    print(f"A spicy food from {cuisine_to_search} is found.")
else:
    print(f"No spicy food found from {cuisine_to_search}.")

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    
    for food in spiciest_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}.")

# Example usage:
print_spiciest_foods(spicy_foods)


def average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0  # To avoid division by zero
    return total_heat // num_foods

avg_heat = average_heat_level(spicy_foods)
print(avg_heat)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


print_spicy_foods(spicy_foods)


