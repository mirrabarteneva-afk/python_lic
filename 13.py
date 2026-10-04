class Vehicle:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self, amount):
        self.speed += amount
        
    def brake(self, amount):
            self.speed = max(0, self.speed - amount)
            
    def info(self):
        return f'{self.brand}, {self.model}, {self.year}, {self.speed}'
    
class Car(Vehicle):
    def __init__(self, brand, model, year, speed, fuel_type):
        super().__init__(brand, model, year, speed)
        self.fuel_type = fuel_type
        
    def info(self):
        return super().info() + f', {self.fuel_type}'
    
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, speed, has_sidecar=False):
        super().__init__(brand, model, year, speed)
        self.has_sidecar = has_sidecar
        
    def info(self):
        sider = 'Нет коляски'
        if self.has_sidecar:
            sider = 'Есть коляска'

        return super().info() + f' sider'
    
