class Car:
    def __init__(self, model, name, color):
        self.model = model
        self.name = name
        self.color = color

    def get_model(self):
        return self.model

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

# Example usage
car = Car("2022", "Toyota", "Red")
print("Model:", car.get_model())  # Output: Model: 2022
print("Name:", car.get_name())    # Output: Name: Toyota
print("Color:", car.get_color())  # Output: Color: Red
