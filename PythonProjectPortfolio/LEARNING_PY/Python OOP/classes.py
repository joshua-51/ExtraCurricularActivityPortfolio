from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

def car1_stuff():
    print(car1.model) 
    print(car1.year)
    print(car1.color)
    print(car1.for_sale)

def car2_stuff():
    print(car2.model)
    print(car2.year)
    print(car2.color)
    print(car2.for_sale)

def car3_stuff():
    print(car3.model)
    print(car3.year)
    print(car3.color)
    print(car3.for_sale)
