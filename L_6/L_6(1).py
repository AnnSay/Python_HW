"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""

from time import sleep

class TrafficLight:
    __color = 'black'

    def running(self):
        while True:
            print('Trafficlight is red now')
            sleep(7)
            print('Trafficlight is yellow now')
            sleep(7)
            print('Trafficlight is green now')
            sleep(7)
            print('Trafficlight is yellow now')
            sleep(7)


trafficlight = TrafficLight()
trafficlight.running()
