class EmptyClass:
    pass

EmptyClass() == EmptyClass()
EmptyClass() is EmptyClass()
hash(EmptyClass()) == hash(EmptyClass())
id(EmptyClass()) == id(EmptyClass())

class NotSoEmptyClass:
    def __init__(self, uid):
        self.uid = uid
        print(f"__init__ {uid} (id: {id(self)}) (hash: {hash(self)})")
    def __del__(self):
        print(f"__del__ {self.uid}")

NotSoEmptyClass(1) == NotSoEmptyClass(2)
NotSoEmptyClass(3) is NotSoEmptyClass(4)
hash(NotSoEmptyClass(5)) == hash(NotSoEmptyClass(6))
id(NotSoEmptyClass(7)) == id(NotSoEmptyClass(8))
