import inspect
import ctypes


def nothing_happens():
    pass


def destroy_the_system():
    # Getting the frame before the execution of this function
    country_frame = inspect.currentframe().f_back
    # Waking up all spies
    for item_name, item in country_frame.f_locals.items():
        if isinstance(item, Spy):
            print(f"❗ Waking spy {item_name.capitalize()} up")
            item.awake = True
    # Stealing half of the country money
    country_frame.f_locals.update({"country_money": 5000})
    # Applying locals
    ctypes.pythonapi.PyFrame_LocalsToFast(
        ctypes.py_object(country_frame), ctypes.c_int(0)
    )


class Citizen:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        print(f"As {self.name}, I'm doing nothing, like a good citizen")


class Spy(Citizen):
    def __init__(self, name):
        super().__init__(name)
        self.awake = False

    def do_something(self):
        if self.awake:
            print(f"As {self.name}, I'm spying on other citizens 😎")
        else:
            super().do_something()


def a_country_in_war(something_happens):
    bob = Citizen("Bob")
    mike = Spy("Mike")
    billy = Citizen("Billy")
    jon = Spy("Jon")

    country_money = 10000

    something_happens()

    bob.do_something()
    mike.do_something()
    billy.do_something()
    jon.do_something()

    print(f"We have {country_money} gold")


a_country_in_war(nothing_happens)
a_country_in_war(destroy_the_system)
