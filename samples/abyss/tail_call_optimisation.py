import sys

class TailRecurseException(Exception):
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    return func

def most_stupid_print(string):
    if len(string) > 0:
        print(string[0], end="")
        most_stupid_print(string[1::])

most_stupid_print("Hello I'm Billy\n" * 1000)