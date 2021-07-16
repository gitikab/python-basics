from restaurant import Restaurant


class Flavour:

    def __init__(self, name):
        self.name = name

    def describe(self):
        print("It is " + self.name + " flavour")


class IceCreamStand(Restaurant):

    def __init__(self, name, *flavours):
        super().__init__(name, "Ice Creams")
        self.flavours = [Flavour(flavour) for flavour in flavours]

    def show_flavours(self):
        count = 1
        for flavour in self.flavours:
            print(str(count) + ". " + flavour.name)
            count += 1

    def describe(self, flavour_number):
        self.flavours[flavour_number - 1].describe()


naturals = IceCreamStand("Naturals", "chocolate", "vanilla", "tutti frutti", "strawberry")
naturals.show_flavours()
naturals.describe(4)
