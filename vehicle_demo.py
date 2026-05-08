import vehicles

car1 = vehicles.Car("Toyota", "Corrolla", 42000, 18999, 4)

truck1 = vehicles.Truck("Honda", "Ridgeline", 12345, 25999, 4)

suv1 = vehicles.SUV("Lexus", "RX350", 367890, 27999, 4)

print("USED CAR INVENTORY\n")

print("The following car is in inventory:")
print("Make:", car1.get_make())
print("Model:", car1.get_model())
print("Mileage:", car1.get_mileage())
print("Price:", car1.get_price())
print("Number of doors:", car1.get_doors())

print("\nThe following pickup truck is in inventory:")
print("Make:", truck1.get_make())
print("Model:", truck1.get_model())
print("Mileage:", truck1.get_mileage())
print("Price:", truck1.get_price())
print("Drive type:", truck1.get_drive_type())

print("\nThe following SUV is in inventory:")
print("Make:", suv1.get_make())
print("Model:", suv1.get_model())
print("Mileage:", suv1.get_mileage())
print("Price:", suv1.get_price())
print("Passenger capacity:", suv1.get_passenger_capacity())

