from flask import (
    Flask,
)

app = Flask(__name__)


# 1. Переменные и константы
@app.route('/variables')
def show_variables_example():
    name = "Gordon Ramsay"
    age = 57
    net_worth = 400000
    cool = True
    PI = 3.14

    return (
        f"Name of our chief: {name},"
        f"Age: {age},"
        f"Salary: {net_worth}$ per show,"
        f"Cool? {cool},"
        f"PI: {PI}."
    )


# 2. Типы данных
@app.route('/datatypes')
def datatypes_example():
    # IMMUTABLE
    chef_age = 35  # int
    rating = 4.8  # float
    recipe_name = "Chocolate Cake"  # str
    is_available = True  # bool
    # MUTABLE
    ingredients = ["flour", "eggs", "sugar"]  # list
    ingredients_set = {"flour", "eggs", "sugar"}  # set
    chef_details = {"name": "Gordon Ramsay", "age": 57}  # dict

    return (
        f"Возраст шефа: {chef_age}, "
        f"Рецепт: {recipe_name}, "
        f"Доступен: {is_available}, "
        f"Ингредиенты (list): {ingredients}, "
        f"Ингредиенты (set): {ingredients_set}, "
        f"Детали шефа: {chef_details}, "
        f"Рейтинг: {rating}"
    )


# 3. Операции над типами данных
@app.route('/operations')
def operations_example():
    # Операции над числами
    dough_weight = 3.5  # float
    number_of_donuts = 12  # int
    total_weight = dough_weight * number_of_donuts  # умножение
    avg_weight = total_weight / number_of_donuts  # деление
    remainder = number_of_donuts % 5  # остаток от деления
    power = number_of_donuts ** 2  # возведение в степень

    # Операции над строками
    donut_name = "Glazed Donut"
    full_name = donut_name + " with Chocolate"  # конкатенация
    repeated_name = donut_name * 3  # повторение строки

    # Операции над списками
    ingredients = ["flour", "eggs", "sugar"]
    ingredients.append("chocolate")  # добавление элемента
    ingredients.pop()  # удаление последнего элемента

    return (
        f"Общий вес теста: {total_weight} кг, "
        f"Средний вес одного пончика: {avg_weight} кг, "
        f"Остаток при делении: {remainder}, "
        f"Возведение в степень: {power}, "
        f"Полное имя пончика: {full_name}, "
        f"Повторенное имя пончика: {repeated_name}, "
        f"Ингредиенты после изменений: {ingredients}"
    )


# Операторы
@app.route('/operators')
def operators_example():
    # Арифметические операторы
    a = 10
    b = 5
    addition = a + b  # сложение
    subtraction = a - b  # вычитание
    multiplication = a * b  # умножение
    division = a / b  # деление
    integer_division = a // b  # целочисленное деление
    modulus = a % b  # остаток от деления
    exponentiation = a ** b  # возведение в степень

    # Операторы сравнения
    is_equal = a == b  # равно
    is_not_equal = a != b  # не равно
    greater_than = a > b  # больше
    less_than = a < b  # меньше
    greater_or_equal = a >= b  # больше или равно
    less_or_equal = a <= b  # меньше или равно

    # Логические операторы
    logic_and = (a > 5) and (b < 10)  # и
    logic_or = (a > 5) or (b > 10)  # или
    logic_not = not (a == b)  # не

    # Операторы присваивания
    c = a  # присваивание
    c += b  # присваивание с добавлением
    c -= b  # присваивание с вычитанием
    c *= b  # присваивание с умножением
    c /= b  # присваивание с делением

    return (
        f"Сложение: {addition}, "
        f"Вычитание: {subtraction}, "
        f"Умножение: {multiplication}, "
        f"Деление: {division}, "
        f"Целочисленное деление: {integer_division}, "
        f"Остаток от деления: {modulus}, "
        f"Возведение в степень: {exponentiation}, "
        f"Равно: {is_equal}, "
        f"Не равно: {is_not_equal}, "
        f"Больше: {greater_than}, "
        f"Меньше: {less_than}, "
        f"Больше или равно: {greater_or_equal}, "
        f"Меньше или равно: {less_or_equal}, "
        f"Логическое И: {logic_and}, "
        f"Логическое ИЛИ: {logic_or}, "
        f"Логическое НЕ: {logic_not}, "
        f"Присваивание с добавлением: {c}"
    )


# Управляющие структуры
@app.route('/control_structures')
def control_structures_example():
    chef_experience = 5  # годы опыта
    if chef_experience > 3:
        return "Шеф получил повышение!"
    else:
        return "Шефу нужно еще подучиться."


# Функции и методы
@app.route('/functions')
def functions_example():
    def cook_donut(quantity):
        return f"Повар приготовил {quantity} пончиков."

    return cook_donut(12)


# Асинхронное программирование
@app.route('/async')
def async_example():
    return "Тут будет пример асинхронного кода для повара"


# Классы и объекты
@app.route('/classes')
def classes_example():
    class Chef:
        def __init__(self, name):
            self.name = name

        def cook(self):
            return f"{self.name} готовит пирожное."

    pastry_chef = Chef("Гарри")
    return pastry_chef.cook()


if __name__ == '__main__':
    app.run(debug=True)
