# module_6_2
Доступ к свойствам родителя. Переопределение свойств

## Задача "Изменять нельзя получать"

В данной задаче мы разработаем классы, представляющие транспортные средства, в которых будет невозможно без специального разрешения изменить цвет, мощность двигателя и другие важные параметры. Это связано с тем, что в реальной жизни такие изменения обычно производятся не владельцами, а специальными сервисами. Тем не менее, мы сможем получить доступ к этим значениям, но изменить их самостоятельно не получится.

Вам предстоит создать два класса: Vehicle и Sedan. Первый представляет собой любой транспорт, а второй — седан, который является наследником класса Vehicle.

### I. Каждый объект Vehicle должен обладать следующими атрибутами:

* Атрибут owner(str) — имя владельца (может изменяться)
* Атрибут __model(str) — модель (марка) автомобиля (нельзя изменить название)
* Атрибут __engine_power(int) — мощность двигателя (недоступна для изменения)
* Атрибут __color(str) — название цвета (нельзя изменить вручную)

Кроме того, класс Vehicle должен включать в себя атрибут класса __COLOR_VARIANTS, который содержит список допустимых цветов для окрашивания. Этот список можно создать самостоятельно.

### II. Каждый объект Vehicle должен обладать следующими методами:

* Метод get_model — возвращает строку с названием модели автомобиля
* Метод get_horsepower — возвращает строку с мощностью двигателя
* Метод get_color — возвращает строку с текущим цветом автомобиля
* Метод print_info — печатает результаты предыдущих методов, а также имя владельца в формате "Владелец: <имя>"
* Метод set_color — принимает аргумент new_color (строка), изменяет текущий цвет на новый, если он присутствует в списке __COLOR_VARIANTS, в противном случае выводит на экран сообщение "Нельзя сменить цвет на <новый цвет>"

### Взаимосвязь методов и скрытых атрибутов:

* Методы get_model, get_horsepower и get_color расположены в одном классе с соответствующими им атрибутами __model, __engine_power и __color, что делает их доступными для использования.
* Атрибут класса __COLOR_VARIANTS можно получить, обращаясь к нему через объект (self).
* Проверка в списке __COLOR_VARIANTS осуществляется без учета регистра, то есть 'BLACK' == 'black'.

### II. Класс Sedan наследуется от класса Vehicle и включает в себя следующие атрибуты:

* Атрибут __PASSENGERS_LIMIT = 5 — ограничение на количество пассажиров (в седане может поместиться только 5 человек)

### Пункты задачи:

- Создайте классы Vehicle и Sedan.
- Реализуйте соответствующие свойства в обоих классах.
- Не забудьте сделать Sedan наследником класса Vehicle.
- Создайте объект класса Sedan и проверьте, как работают все его методы, унаследованные от класса Vehicle.

### Пример результата выполнения программы:

Исходный код:

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в том числе вызывая методы)

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем изменения

vehicle1.print_info()

Вывод на консоль:

Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos

Нельзя сменить цвет на Pink

Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok

### Примечания:

* Обратите особое внимание на условия задачи: различайте, что является атрибутом класса, а что — атрибутом объекта.
* Методы, описывающие получение или перезапись атрибутов, рекомендуется начинать со слов get и set соответственно. Такие методы часто используются для доступа к скрытым атрибутам и позволяют писать дополнительную логику при их получении или изменении.
* Не забывайте использовать self при обращении к атрибутам объекта.
* Константные (постоянные) значения в Python принято писать полностью в верхнем регистре (капсом), как в случае списка цветов или количества пассажиров.
