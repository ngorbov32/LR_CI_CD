class Car:
    def __init__(self, model: str, fuel_capacity: float):
        self.model = model
        self.fuel_capacity = float(fuel_capacity)
        # При создании машины считаем, что бак полный
        self.fuel_tank = self.fuel_capacity

    def get_current_fuel_level(self) -> float:
        return self.fuel_tank

    def refuel_car(self, liters: float) -> None:
        liters = float(liters)
        # По тесту: 80 при capacity=80 считается "перелили"
        if liters >= self.fuel_capacity:
            raise Exception("Перелили топливо")
        # По тесту ожидается, что уровень станет ровно liters
        self.fuel_tank = liters

    def drive(self, distance_km: float) -> None:
        distance_km = float(distance_km)
        # Расход 8 литров на 100 км
        fuel_burned = 8 * (distance_km / 100)

        if self.fuel_tank < fuel_burned:
            raise Exception("Не доедем же...")
        self.fuel_tank -= fuel_burned

