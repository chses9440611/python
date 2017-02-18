cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven
#even outside the string, we also can print format using space!!!
print "There are", cars, "cars avaible."
print "There are only", drivers, "drivers avaible."
print "There will be", cars_not_driven, "people today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today!"
print "We need to put about", average_passengers_per_car, "in each car."
