"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
    '''AUTO'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля {self.speed}'


class TownCar(Car):
    '''городской автомобиль'''

    def show_speed(self):
        return f'{self.name:Скорость автомобиля: {self.speed}. Превышение скорости!}' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    """Грузовой автомобиль"""


    def show_speed(self):
        return f'{self.name:Скорость автомобиля: {self.speed}. Превышение скорости!}' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    '''Спортивный автомобиль'''

class PoliceCar(Car):
    '''Полицейский автомобиль'''

    def __init__(self, neme, color, speed, is_police=True):
        super().__init__(neme, color, speed, is_police)

police_car = PoliceCar ('Полицейская машина', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn()
police_car.stop()
print()

work_car = WorkCar('Грузовик', 'синий', 40)
work_car.go()
work_car.turn()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar('Спорткар', 'красный', 150)
sport_car.go()
sport_car.turn()
print(sport_car.show_speed())
sport_car.turn(0)
sport_car.stop()
print()

town_car = TownCar('Легковая', 'Серый', 80)
town_car.go()
town_car.turn()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()
