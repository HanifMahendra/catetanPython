# Animal <- parent class
# data1
# data2

# Move() <- overridden method
# Eat() <- inherited method

# => Dog <- subclass
#    data3
#    data4

#   move() <- overridden method
#   bark()

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): #Rabbit is the child/sub class, Animal is the parent/super class
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()