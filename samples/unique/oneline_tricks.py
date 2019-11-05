def multiply_by_2(x):
    return x * 2

print(multiply_by_2(25))

multiply_by_2 = lambda x: x * 2; print(multiply_by_2(25))

table_dict = {
    "1": 6,
    "2": 6,
    "3": 6,
    "4": 6,
    "5": 6,
}

new_dict = {}
for item, value in table_dict.items():
    new_dict[f"{value} x {item}"] = value * int(item)
print(new_dict)

print({f"{key} x {value}": value * int(key) for key, value in table_dict.items()})

my_age = 19

if my_age > 18:
    print("Wow you can drive")
else:
    print("No car for you yet")

print("Wow you can drive" if my_age > 18 else "No car for you yet")