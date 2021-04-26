#cars is assigned the value of 100
cars = 100
#space_in_a_car is assigned the floating point value of 4.0
space_in_a_car = 4.0
#drivers is assigned the value of 30
drivers = 30
#passengers is assigned the value of 90
passengers = 90
#cars(100) minus drivers(30), result (70) and assigned to cars_not_driven
cars_not_driven = cars - drivers
#drivers value (30) is assigned to cars_driven
cars_driven = drivers
#cars_driven(30) multiply by space_in_a_car(4.0),
#result floating point (120.0) ans assigned to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
#passengers(90) divided by cars_driven(30),
#result (3.0 [Python3 division is floating points by default])
#and assigned to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car,
      "in each car.")
