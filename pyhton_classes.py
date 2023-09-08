# Define a Vehicle class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, mph):
        self.speed += mph
        return f"The {self.year} {self.make} {self.model} accelerates to {self.speed} mph."

    def brake(self, mph):
        self.speed -= mph
        return f"The {self.year} {self.make} {self.model} slows down to {self.speed} mph."

    def honk(self):
        return "Honk! Honk!"

# Define a Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def honk(self):
        return "Beep! Beep!"  # Car-specific honk method

    def info(self):
        return f"This car is a {self.year} {self.make} {self.model} running on {self.fuel_type}."

# Define a Bicycle class that inherits from Vehicle
class Bicycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def pedal(self):
        return "Pedaling the bicycle."

    def info(self):
        return f"This bicycle is a {self.year} {self.make} {self.model}."

# Create instances of Car and Bicycle
my_car = Car("Toyota", "Camry", 2022, "gasoline")
my_bicycle = Bicycle("Trek", "FX 2", 2021)

# Demonstrate vehicle actions
print(my_car.accelerate(30))  # Accelerate the car
print(my_car.brake(10))  # Apply brakes to the car
print(my_car.honk())  # Honk the car horn (Car-specific honk)
print(my_car.info())  # Display car information

print(my_bicycle.accelerate(10))  # Accelerate the bicycle
print(my_bicycle.brake(5))  # Apply brakes to the bicycle
print(my_bicycle.pedal())  # Pedal the bicycle
print(my_bicycle.info())  # Display bicycle information
