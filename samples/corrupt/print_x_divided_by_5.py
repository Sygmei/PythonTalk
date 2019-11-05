def print_x_divided_by_5(x):
    divisor = 3
    return x * divisor

ARGS_ORDER = [
    "argcount", "kwonlyargcount", "nlocals",
    "stacksize", "flags", "code",
    "consts", "names", "varnames",
    "filename", "name", "firstlineno",
    "lnotab", "freevars", "cellvars",
]
def patch_function(func):
    code = func.__code__
    # Building original payload
    payload = [
        getattr(code, f"co_{attr_name}") 
        for attr_name in ARGS_ORDER
    ]

    # Modifying opcode in the function's Python bytecode
    new_code = [opcode for opcode in code.co_code]
    new_code[8] = 0x1B

    # Patching the payload
    payload[ARGS_ORDER.index("code")] = bytes(new_code)
    payload[ARGS_ORDER.index("consts")] = (None, 5)

    # Applying new code object
    func.__code__ = type(code)(
        *payload,
    )

import dis

print(print_x_divided_by_5(15))
assert print_x_divided_by_5(15) != 3
dis.dis(print_x_divided_by_5)
print(print_x_divided_by_5.__code__.co_code)
print([x for x in print_x_divided_by_5.__code__.co_code])
print(print_x_divided_by_5.__code__.co_consts)

patch_function(print_x_divided_by_5)

print(print_x_divided_by_5(15))
assert print_x_divided_by_5(15) == 3
dis.dis(print_x_divided_by_5)
print(print_x_divided_by_5.__code__.co_code)
print([x for x in print_x_divided_by_5.__code__.co_code])
print(print_x_divided_by_5.__code__.co_consts)