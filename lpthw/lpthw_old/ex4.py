cars = 100 #amount of cars
space_in_a_car = 4 # space in a car
drivers = 30 #amount of drivers
passengers = 90 #amount of passengers
cars_not_driven = cars - drivers #free cars
cars_driven = drivers # 1 driver per car
carpool_capacity = cars_driven * space_in_a_car # space in a car - driver(3)
average_passenger_per_car = passengers / cars_driven #driven cars need
# statements below will print results of statements above
# let's wish them a luck
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passenger_per_car, "in each car."
