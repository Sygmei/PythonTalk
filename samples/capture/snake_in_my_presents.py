# better_make_cell accepts one parameter: the value we want to put in a cell
def better_make_cell(value):
    # The function inside will need a closure to store "value"
    def function_with_closure():
        return value
    # We return the unique item inside "function_with_closure" closure
    return function_with_closure.__closure__[0]

def function_closure_patcher(function, **replacements):
    # Names of the cells of the function's closure
    freevars = function.__code__.co_freevars
    # Rebuilding a dict associating the cell's name to the cell
    closure_dict = dict(
        zip(
            freevars,
            (c.cell_contents for c in function.__closure__),
        )
    )
    # Patching the elements of the closure as needed
    new_closure = {
        **closure_dict,
        **{
            key: replacements[key](value) 
            for key, value in closure_dict.items()
        }
    }

    # Small tool to create cells
    make_cell = lambda value: ((lambda x: lambda: x)(value).__closure__[0])

    # Returning a copy of the function with a patched closure
    return type(lambda: 0)(
        function.__code__,
        function.__globals__,
        function.__name__,
        closure=tuple(
            better_make_cell(new_closure[freevar_name])
            for freevar_name in freevars
        )
    )

import time

def wrap_the_presents(presents):
    def open_the_present():
        child_name = presents.__name__.split('_')[-1].capitalize()
        print(f"Time to open {child_name}'s presents !")
        print("🎁")
        time.sleep(1)
        print(" ".join([present for present in presents()]))
        time.sleep(1)
    return open_the_present

@wrap_the_presents
def presents_for_billy():
    return ["🚀", "🔭", "🪐"]

@wrap_the_presents
def presents_for_bob():
    return ["🩰", "🎀", "🐍"]

@wrap_the_presents
def presents_for_mike():
    return ["🏓", "🐍", "🥋"]

@wrap_the_presents
def presents_for_doug():
    return ["🐍", "🎻", "🥁", "🎺"]

def snake_repellant(presents):
    snake_repellant_lambda = lambda: [
        x for x in presents() if x != "🐍"
    ]
    return type(lambda: 0)(
        snake_repellant_lambda.__code__,
        snake_repellant_lambda.__globals__,
        presents.__name__,
        closure=snake_repellant_lambda.__closure__
    )

class ChristmasTree:
    def __init__(self):
        self.presents = []
    def add_presents(self, presents):
        self.presents.append(presents)
    def open_all(self):
        for present in self.presents:
            present()

christmas_tree = ChristmasTree()

christmas_tree.add_presents(presents_for_billy)
christmas_tree.add_presents(presents_for_bob)
christmas_tree.add_presents(presents_for_mike)
christmas_tree.add_presents(presents_for_doug)

christmas_tree.presents = map(
    lambda element: function_closure_patcher(
        element, 
        presents=snake_repellant
    ),
    christmas_tree.presents
)

christmas_tree.open_all()