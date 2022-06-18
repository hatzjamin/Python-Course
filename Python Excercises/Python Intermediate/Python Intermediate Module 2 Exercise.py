flavors = ["boots", "chocolate", "strawberry", "coockies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print(ice_cream)

groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "orange": 4}
remove = groceries.pop("orange")
print(groceries)

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}

name = speakers.keys()
print(name)

tryout_result = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed", "Joseph": "passed", "Jone": "failed", "Jorge": "failed", "Goerge": "passed", "Ben": "passed", "Jerome": "passed", "Rick": "failed", "Max G.": "failed", "John P.": "failed", "Vince": "passed"}

print(tryout_result.get("Jorge"))