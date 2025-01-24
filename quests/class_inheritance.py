

# class Brand() :
#     def get_info():
#         pass

# class Model():
#     pass

class Vehicle():

    def __init__(self, brand = "Null", model = "Null"):
        self.brand = brand
        self.model = model
        pass

    def get_info(self):
        return f'brand : {self.brand}, model : {self.model}'


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.wheels = ''

    def get_info(self):
        return super().get_info()
    
    def ride_info(self, wheels):
        self.wheels = wheels
        return f' Car | {self.brand} | {self.model} | {self.wheels} '

    

class Truck(Vehicle):
    def __init__(self, brand="Null", model="Null"):
        super().__init__(brand, model)

    def get_info(self):
        return f"truck brand  {self.brand}: , truck model : {self.model}"
    
    def more_info(self, wheels):
        return f" truck | {self.brand} | {self.model} | {wheels} "
         
'''
output
brand : kia, model : K5
 Car | kia | K5 | 4 
truck brand  hyundai: , truck model : Poter
 truck | hyundai | Poter | 8 

'''

if __name__ == "__main__":
    newCar = Car('kia', 'K5')
    print('output')
    print(newCar.get_info())

    print(newCar.ride_info('4'))

    newTruck = Truck('hyundai', 'Poter')
    print(newTruck.get_info())

    print(newTruck.more_info('8'))

