import pizza_module
from pasta_module import make_pasta, make_pesto_pasta
from pasta_module import make_arabiatta_pasta as white_pasta


pizza_module.make_pizza("Spinach", "Cheese")
make_pasta("Penne", "Olives", "Cheese", sauce_type="pink")
make_pesto_pasta("Spiralli", "Zucchini")
white_pasta("Sphagetti", "sun dried tomato")
