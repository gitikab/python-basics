class Car:

    def __init__(self, model, year):
        self.model = model
        self.make = year
        self.odometer = 0

    def odometer_reading(self):
        return self.odometer

    def update_odometer(self, reading):
        if self.odometer < reading:
            self.odometer = reading
        else:
            print("Cannot rollback odometer reading")

    def increment_odometer(self, increment_value):
        if increment_value <= 0:
            print("Cannot decrease odometer reading")
        else:
            self.odometer += increment_value


my_car = Car("Maruti Suzuki Baleno", 2016)
# Changing an attribute directly
my_car.odometer = 100
# Changing an attribute using a function
my_car.update_odometer(150)
# Incrementing an attribute using a function
my_car.increment_odometer(75)


class ElectricCar(Car):

    def __init__(self, model, year, battery_size):
        super().__init__(model, year)
        self.battery_size = battery_size

    def display_battery(self):
        print(str(self.battery_size) + " kWh")

# Override method from Parent class
    def odometer_reading(self):
        print("Not Supported")


my_tesla = ElectricCar("Tesla", 2021, 70)
print(my_tesla.model)
my_tesla.display_battery()
my_tesla.odometer_reading()

# All module importing applies to importing classes as well
