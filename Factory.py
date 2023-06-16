class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Автомобиль едет по дороге")

class Ship(Vehicle):
    def move(self):
        print("Корабль плывет по воде")

class Aircraft(Vehicle):
    def move(self):
        print("Самолет летит в воздухе")

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "ship":
            return Ship()
        elif vehicle_type == "aircraft":
            return Aircraft()
        else:
            raise ValueError("Неподдерживаемый тип транспортного средства")

# Использование фабрики для создания объектов
factory = VehicleFactory()
car = factory.create_vehicle("car")
car.move()  # Вывод: Автомобиль едет по дороге

ship = factory.create_vehicle("ship")
ship.move()  # Вывод: Корабль плывет по воде

aircraft = factory.create_vehicle("aircraft")
aircraft.move()  # Вывод: Самолет летит в воздухе
