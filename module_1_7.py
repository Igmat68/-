my_dict = {"Igor" : 1968, "Oleg" : 1975, "Slava" : 1990}
print("Dict:", my_dict)
print("Not existing value:", my_dict.get("Eva"))
my_dict.update({"Irina" : 2000, "Kamila" : 2005})
print("Deleted value:", my_dict.pop("Oleg"))
print("Modified dictionari:", my_dict)
my_set = {1, 2, 3, "string", 2, 1, 33.8}
print("Set:", my_set)
my_set.add((55.5))
my_set.add((6, 7, 10))
print("Modified set:", my_set)