eye = "👁️"
mouth = "👄"
tongue = "👅"

def tell_a_joke(person):
    def tell_a_joke_wrapper(*args, **kwargs):
        return person(*args, **kwargs).replace(mouth, tongue)
    return tell_a_joke_wrapper

@tell_a_joke
def sabrina():
    return f"{eye}{mouth}{eye}"

def back_to_normal(person):
    return person.__closure__[0].cell_contents

print(sabrina())
sabrina = back_to_normal(sabrina)
print(sabrina())