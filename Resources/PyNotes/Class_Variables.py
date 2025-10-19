class Car:

    wheels = 4                      #Class Variable

    def __init__(self,make,model,year,color):
        self.make = make            #instance variable
        self.model = model          #instance variable
        self.year = year            #instance variable
        self.color = color          #instance variable

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2020,"red")

car_1.wheels = 2 #Ganti jumlah wheels untuk variable "car_1"
Car.wheels = 2 #Ganti jumlah wheels untuk class "Car"

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)