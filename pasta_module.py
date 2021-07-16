def make_pasta(pasta_type, *toppings, sauce_type="white"):
    topping_string = " ".join(toppings)
    print("I want a " + pasta_type + " pasta in " + sauce_type + " sauce with " + topping_string)


def make_pesto_pasta(pasta_type, *toppings):
    make_pasta(pasta_type, sauce_type="pesto", *toppings)


def make_arabiatta_pasta(pasta_type, *toppings):
    make_pasta(pasta_type, sauce_type="white", *toppings)

