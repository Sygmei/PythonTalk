# We define an empty dict
my_dict = {}
# Invalid syntax, we can't assign in a Python lambda
# set_to_dict = (lambda dikt, value: dikt["key"] = value)
# Valid using the direct method
set_to_dict = lambda dikt, value: dikt.__setitem__(
    "key", value
)  
set_to_dict(my_dict, 22)
print(my_dict)

# random_from_1_to_100 = lambda: (import random; random.randint(1, 100)) # Invalid syntax
import random

random_from_1_to_100 = lambda: random.randint(
    1, 100
)  # Valid but it's not a one-liner anymore
print(random_from_1_to_100())
random_from_1_to_100 = (lambda random: lambda: random.randint(1, 100))(
    __import__("random")
)
print(random_from_1_to_100())


class WaitASecondYouAreTotallyNotMyFriendError(Exception):
    def __init__(self, ninja):
        super().__init__(
            f"Hey ! Wait a second, you're not my friend ! You're {ninja} !"
        )