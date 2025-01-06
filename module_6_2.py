

class Vehicle:  # класс это любой транспорт

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black','white']  # в который записан список допуст-х цветов для окраш-ия

    def __init__(self, owner: str, __model: str,__engine_power: int, __color:str):
        # Атрибуты класса:
        self.owner = owner # владелец транспорта. (владелец может меняться)
        self.__model = __model # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power # мощность двигателя. (мы не можем менять мощность двигателя самост-но)
        self.__color = __color # название цвета. (мы не можем менять цвет автомобиля своими руками)

# Каждый объект Vehicle должен содержать следующий методы:
    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def  print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
           self.__color = new_color
        else:
           print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle): # наследник класса Vehicle
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()