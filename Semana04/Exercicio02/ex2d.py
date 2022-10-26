class dog:

    def __init__(self, name):
        self.name = name
        print(name)

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = dog("Tim")
print(d.name)
d2 = dog("Bill")
print(d2.name)