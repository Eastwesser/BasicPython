from flask import (
    Flask,
)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# Переменные
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


# Типы данных
@app.route('/datatypes')
def datatypes_example():
    chef_age = 35  # int
    recipe_name = "Chocolate Cake"  # str
    is_available = True  # bool
    # list example [list]
    ingredients = [
        "flour",
        "eggs",
        "sugar",
    ]
    return (
        f"Возраст шефа: {chef_age}, "
        f"Рецепт: {recipe_name}, "
        f"Доступен: {is_available}, "
        f"Ингредиенты: {ingredients}",
    )


# Операции над типами данных
@app.route('/operations')
def operations_example():
    dough_weight = 3.5  # float
    number_of_donuts = 12  # int
    total_weight = dough_weight * number_of_donuts  # умножение
    return f"Общий вес теста: {total_weight} кг"


# Операторы
@app.route('/operators')
def operators_example():
    a = 10
    b = 5
    result = a + b  # арифметический оператор
    return f"Результат сложения: {result}"


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
