# Method Chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine!")
        return self
    
    def drive(self):
        print("You drive the car!")
        return self
    
    def brake(self):
        print("You hit the brakes!")
        return self
    
    def turn_off(self):
        print("You turn off the engine!")
        return self
    
car = Car()

# Ini yang biasa
car.turn_on()
car.drive()

print()
print("=======================")
print()

# Dengan method chaining, bisa seperti ini:
car.turn_on().drive()

print()
print("=======================")
print()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

print()
print("=======================")
print()

car.turn_on().drive().brake().turn_off()