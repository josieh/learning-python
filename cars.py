cars = 100
space_in_car = 4
drivers = 30
passengers = 90

cars_driven = drivers
cars_not_driven = cars - drivers

carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
#comma means cancatanate

print "There are only", drivers, "drivers available."
print "We can transport", carpool_capacity, "people today"
print "We hav %d to carbool today." % passengers
print "We have", passengers, "to carpool today."
print "We need to put %d in each car.", (average_passengers_per_car, cars_driven)

