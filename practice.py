class Human:
    c = 4

    def __init__(self, a, b):
        self.a = a
        self.b = b


h1 = Human('aaa', 'bbb')

print(h1.a)
print(h1.c)

print(Human.c)
print(h1.__dict__)
print()
