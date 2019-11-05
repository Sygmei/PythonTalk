def check(x):
    if x + 1 is 1 + x:
        return False
    elif x + 2 is not 2 + x:
        return False
    return True

assert check(-7) is True

import time
class ChallengeBreaker:
    def __init__(self):
        pass
    def __add__(self, x):
        return time.time() if x == 1 else 1
    __radd__ = __add__

assert check(ChallengeBreaker()) is True