class Try:
    def __enter__(self):
        pass
    def __exit__(self, exct, exc, tb):
        print(25/0)
        return True

class Except:
    def __enter__(self):
        pass
    def __exit__(self, exct, exc, tb):
        if exct and issubclass(exct, ZeroDivisionError):
            print("Dividing by 0 is impossible")
            return True

with Except():
    with Try():
        pass

import contextlib

with contextlib.ExitStack() as except_context:
    except_context.enter_context(Except())
    except_context.enter_context(Try())