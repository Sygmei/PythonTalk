class WaitASecondYouAreTotallyNotMyFriendError(Exception):
    def __init__(self, ninja):
        super().__init__(f"Hey ! Wait a second, you're not my friend ! You're {ninja} !")

class Ninja:
    def __init__(self, name):
        self.name = name
        self.friends = set()
    def introduce_to(self, ninja):
        print(f"Hello {ninja}, my name is {self}")
        self.friends.add(ninja); ninja.friends.add(self)
    def date_with_a_ninja(self, ninja):
        if ninja in self.friends:
            print(f"Long time no see {ninja} !")
        else:
            raise WaitASecondYouAreTotallyNotMyFriendError(ninja)
    def __repr__(self):
        return self.name

# Hey Bob, nice Katana you've got there
bob_the_ninja = Ninja("Bob")
# Wow Mike, that's a dope Shuriken
mike_the_ninja = Ninja("Mike")

bob_the_ninja.introduce_to(mike_the_ninja)
bob_the_ninja.date_with_a_ninja(mike_the_ninja)
# Later that day...
mike_the_ninja.date_with_a_ninja(bob_the_ninja)

# Dave is only there for trouble, don't be like Dave
dave_the_ninja = Ninja("Dave")

def dave_trying_to_date_bob():
    try: # Dave pretending to be Bob's friend
        bob_the_ninja.date_with_a_ninja(dave_the_ninja)
    except WaitASecondYouAreTotallyNotMyFriendError as e:
        # Of course, Bob is not gullible and see through Dave's masquerade
        print(e)

dave_trying_to_date_bob()

# Dave is not done, he'll try impersonating Mike
dave_the_ninja.name = "Mike" 
# Will it work this time ?
dave_trying_to_date_bob()

class SneakyNinja(Ninja):
    def __init__(self, name: str, usurpation_target: Ninja):
        self.name = name
        self.usurpation_target = usurpation_target
    def __eq__(self, other_ninja):
        result = self.usurpation_target == other_ninja
        print(f"Am I ({self}) equal to {other_ninja} ? Answer is {result}")
        return result
    def __hash__(self):
        result = self.usurpation_target.__hash__()
        print(f"Hey, I'm {self} and my hash is {result}")
        return result
    def __repr__(self):
        return f"{self.usurpation_target} (But it's {self.name} under the hood hehehe)"

# Dave is now trying harder to look like Mike
dave_the_ninja = SneakyNinja("Dave", mike_the_ninja)

# Will it work this time ?
dave_trying_to_date_bob()

print(dave_the_ninja is mike_the_ninja)
