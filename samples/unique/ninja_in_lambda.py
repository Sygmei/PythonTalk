# Basic class we saw earlier
class Ninja:
    def __init__(self, name):
        self.name = name
        self.friends = set()

    def introduce_to(self, ninja):
        print(f"Hello {ninja}, my name is {self}")
        self.friends.add(ninja)
        ninja.friends.add(self)

    def date_with_a_ninja(self, ninja):
        if ninja in self.friends:
            print(f"Long time no see {ninja} !")
        else:
            raise RuntimeError(ninja)

    def __repr__(self):
        return self.name


Ninja = (
    lambda: type(  # Lambda wrapper for our new Ninja class
        "Ninja",
        (object,),
        dict(  # Returns a class object.
            __init__=(
                lambda self, name: self.__dict__.update(  # Init for our class
                    dict(  # We need to set our attributes using self's dict
                        name=name, friends=set()
                    )
                )
            ),
            # Each method is an attribute of a dict passed to the type function
            introduce_to=lambda self, ninja: (
                print(f"Hello {ninja}, my name is {self}"),
                self.friends.add(ninja),
                ninja.friends.add(self),
            ),
            date_with_a_ninja=lambda self, ninja: (
                # We use a ternary condition because traditional conditions are a syntax error
                print(f"Long time no see {ninja} !")
                if ninja in self.friends
                # Raising exception in a lambda is forbidden, we have to cheat
                else (lambda: (yield 0))().throw(
                    RuntimeError(ninja)
                )
            ),
            __repr__=(lambda self: self.name),
        ),
    )
)()