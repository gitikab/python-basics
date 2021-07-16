class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def open_restaurant(self):
        print(self.name + " is open now")

    def describe_restaurant(self):
        print(self.name + " serves " + self.cuisine + " cuisine")


mc_d = Restaurant("McDonald's", "Burgers")
dominoes = Restaurant("Dominoes", "Pizza")
sos = Restaurant("Slice of Soul", "Italian")
mc_d.describe_restaurant()
dominoes.describe_restaurant()
sos.describe_restaurant()