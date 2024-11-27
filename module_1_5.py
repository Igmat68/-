immutable_var = 1, 2, "apple", True
print("Immutable tuple:", immutable_var)
#immutable_var[0] = 50 #нельзя изменить значения элементов кортежа потому, что он не измкняем и не поддерживает обращение по элементам
mutable_list = [5, 6, 7, "banana", False]
mutable_list[3] = 10
mutable_list[0] = 35
print("Mutable list:", mutable_list)