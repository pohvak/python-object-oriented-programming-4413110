# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def printProps(self):
        print(self.prop1, self.prop2, self.name)

c = C()
c.printProps()
print(C.__mro__)
