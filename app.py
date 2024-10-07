import asyncio
import re
from abc import (
    ABC,
    abstractmethod,
)
from functools import reduce

from flask import (
    Flask,
)

app = Flask(__name__)


# 1. Переменные и константы ============================================================================================
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


# 2. Типы данных =======================================================================================================
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


# 3. Операции над типами данных ========================================================================================
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


# 4. Операторы =========================================================================================================
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


# 5. Управляющие структуры =============================================================================================
@app.route('/control_structures')
def control_structures_example():
    chef_experience = 5  # годы опыта

    # Условные операторы
    if chef_experience > 10:
        promotion_status = "Шеф назначен шеф-поваром ресторана!"
    elif chef_experience > 5:
        promotion_status = "Шеф получил повышение до главного шефа."
    else:
        promotion_status = "Шефу нужно еще подучиться."

    # Цикл for
    donut_names = [
        "Glazed Donut",
        "Chocolate Donut",
        "Strawberry Donut",
    ]
    donut_list = []
    for donut in donut_names:
        donut_list.append(f"{donut} приготовлен.")

    # Цикл while
    donut_count = 0
    while donut_count < len(donut_names):
        donut_count += 1

    return (
        f"{promotion_status} "
        f"Количество пончиков, приготовленных с использованием цикла while: {donut_count}. "
        f"Список пончиков: {', '.join(donut_list)}"
    )


# 6. Функции и методы ==================================================================================================
@app.route('/functions')
def functions_example():
    # Функция, принимающая аргумент
    def cook_donut(quantity):
        return f"Повар приготовил {quantity} пончиков."

    # Функция без аргументов
    def chef_greeting():
        return "Добро пожаловать на кухню!"

    # Функция с несколькими аргументами
    def calculate_total_cost(quantity, price_per_donut):
        return quantity * price_per_donut

    # Использование map для преобразования списка
    donut_prices = [1.5, 2.0, 3.0]
    total_prices = list(map(lambda price: price * 12, donut_prices))

    # Методы строк
    chef_name = "gordon ramsay"
    uppercase_name = chef_name.upper()  # Преобразование к верхнему регистру
    name_length = len(chef_name)  # Количество символов в строке

    # Методы списков
    donuts = ["Glazed", "Chocolate", "Strawberry"]
    donuts.append("Vanilla")  # Добавление элемента в список
    removed_donut = donuts.pop(1)  # Удаление элемента по индексу

    return (
        f"{cook_donut(12)} "
        f"{chef_greeting()} "
        f"Стоимость за дюжину пончиков: {total_prices}. "
        f"Имя шефа в верхнем регистре: {uppercase_name}, длина имени: {name_length}. "
        f"Пончики: {donuts}, удалённый пончик: {removed_donut}."
    )


# ======================================================================================================================
# Here are the tasks for testing backenders
# ======================================================================================================================
# TASK 1: PALINDROME
# ======================================================================================================================
def is_palindrome(word):
    prepared_word = word.lower()
    return prepared_word == prepared_word[::-1]


checking_palindrome = is_palindrome("radar")
print(checking_palindrome)


# ======================================================================================================================
# TASK 2: REGULARS FOR E-MAIL VALIDATION
# ======================================================================================================================
def validate_inputs(email, phone, username):
    # Регулярное выражение для email
    email_reg = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Регулярное выражение для телефона (формат +7 (xxx) xxx-xx-xx или подобные)
    phone_reg = r'^\+?\d{1,4}?[-.\s]?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}$'

    # Регулярное выражение для имени пользователя (допустим, от 3 до 16 символов, буквы, цифры, _ и .)
    username_reg = r'^[a-zA-Z0-9_.]{3,16}$'

    # Проверка email
    valid_email = bool(re.match(email_reg, email))

    # Проверка телефона
    valid_phone = bool(re.match(phone_reg, phone))

    # Проверка имени пользователя
    valid_username = bool(re.match(username_reg, username))

    return valid_email, valid_phone, valid_username


# Пример использования:
email = input("Введите email: ")
phone = input("Введите телефон: ")
username = input("Введите имя пользователя: ")

result = validate_inputs(email, phone, username)
print(f"Email: {result[0]}, Телефон: {result[1]}, Имя пользователя: {result[2]}")


# ======================================================================================================================
# TASK 3: REPLACE WORDS IN TEXT
# ======================================================================================================================
def replace_words(main_string, find_words, replace_with):
    new_string = main_string.replace(find_words, replace_with)
    return new_string


# Пример с вводом данных
a = input("Введите строку: ")
b = input("Введите слово для поиска: ")
c = input("Введите слово для замены: ")

result = replace_words(a, b, c)
print(result)


# ======================================================================================================================
# Task 4: FIND UNIQUE ELEMENTS
# ======================================================================================================================
def find_unique_elements(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)

    unique_elements_1 = set_1 - set_2
    unique_elements_2 = set_2 - set_1

    result_unique_elements = list(unique_elements_1.union(unique_elements_2))
    return result_unique_elements


list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
unique_elements_for_lists = find_unique_elements(list_a, list_b)
print(unique_elements_for_lists)


# ======================================================================================================================
# End of the tasks
# ======================================================================================================================

# 7. Асинхронное программирование ======================================================================================
@app.route('/async')
def async_example():
    # Запускаем асинхронную задачу
    result = asyncio.run(fetch_data())
    return f"Полученные данные: {result}"


# Асинхронная функция
async def fetch_data():
    # Имитация асинхронного вызова
    await asyncio.sleep(2)  # Задержка в 2 секунды, имитирующая ожидание данных
    return "Данные успешно получены!"


# 8. Списки, множества и словари (карты) ===============================================================================
@app.route('/collections')
def collections_example():
    # Пример работы со списком
    donut_ingredients = ["мука", "сахар", "дрожжи", "молоко"]
    donut_ingredients.append("яйцо")  # Добавление ингредиента в список

    # Пример работы с множеством
    unique_ingredients = {"мука", "сахар", "яйцо", "молоко"}
    unique_ingredients.add("шоколад")  # Добавляем уникальный ингредиент
    unique_ingredients.add("мука")  # Мука не добавится, так как уже есть

    # Пример работы с картой (словарём)
    donut_recipes = {
        "классический пончик": ["мука", "сахар", "дрожжи", "яйцо"],
        "шоколадный пончик": ["мука", "сахар", "шоколад", "яйцо"],
        "ванильный пончик": ["мука", "сахар", "ваниль", "яйцо"],
    }

    return (
        f"Ингредиенты для пончиков: {donut_ingredients}. "
        f"Уникальные ингредиенты: {unique_ingredients}. "
        f"Рецепты пончиков: {donut_recipes}."
    )


@app.route('/map_example')
def map_example():
    numbers = [1, 2, 3, 4, 5]
    # Применим функцию, которая возводит числа в квадрат ко всем элементам списка
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return f"Квадраты чисел: {squared_numbers}"


# 9. Работа с коллекциями ==============================================================================================
@app.route('/collections_loop')
def collections_loop_example():
    # Список ингредиентов
    donut_ingredients = ["мука", "сахар", "дрожжи", "молоко"]

    # Перебор элементов списка
    ingredients_list = []
    for ingredient in donut_ingredients:
        ingredients_list.append(f"Ингредиент: {ingredient}")

    # Словарь с рецептами
    donut_recipes = {
        "классический пончик": ["мука", "сахар", "дрожжи", "яйцо"],
        "шоколадный пончик": ["мука", "сахар", "шоколад", "яйцо"]
    }

    # Перебор элементов словаря
    recipes_list = []
    for donut, ingredients in donut_recipes.items():
        recipes_list.append(f"{donut}: {', '.join(ingredients)}")

    return (
        f"Ингредиенты: {', '.join(ingredients_list)}. "
        f"Рецепты: {', '.join(recipes_list)}."
    )


# 10.	Исключения, обработка исключений ===============================================================================
@app.route('/exceptions')
def exceptions_example():
    try:
        donuts_made = 12
        hours_worked = 0  # У нас ошибка, деление на ноль!
        donuts_per_hour = donuts_made / hours_worked
    except ZeroDivisionError:
        return "Ошибка: деление на ноль. Нельзя разделить количество пончиков на ноль часов!"

    try:
        ingredients = ["мука", "сахар", "дрожжи"]
        # Попытка доступа к несуществующему элементу списка
        secret_ingredient = ingredients[3]
    except IndexError:
        return "Ошибка: недопустимый индекс. Нет такого ингредиента в списке!"

    return "Все исключения успешно обработаны."


# 11. Классы и объекты =================================================================================================
@app.route('/classes')
def classes_example():
    # Класс Повар
    class Chef:
        def __init__(self, name, specialty):
            self.name = name  # Имя повара
            self.specialty = specialty  # Специализация повара

        def cook(self):
            return f"{self.name}, который специализируется на {self.specialty}, готовит пирожное."

    # Создание объекта повара
    pastry_chef = Chef("Гарри", "десертах")
    return pastry_chef.cook()


# 12. Наследование, полиморфизм, инкапсуляция ==========================================================================

# Наследование
@app.route('/inheritance')
def inheritance_example():
    # Базовый класс Повар
    class Chef:
        def __init__(self, name):
            self.name = name

        def cook(self):
            return f"{self.name} готовит блюдо."

    # Класс кондитера, наследует от класса Повар
    class PastryChef(Chef):
        def cook(self):
            return f"{self.name} готовит десерт."

    # Создаём повара и кондитера
    general_chef = Chef("Алексей")
    pastry_chef = PastryChef("Гарри")

    return f"{general_chef.cook()} <br> {pastry_chef.cook()}"


# Полиморфизм
@app.route('/polymorphism')
def polymorphism_example():
    class Chef:
        def __init__(self, name):
            self.name = name

        def cook(self):
            return f"{self.name} готовит обед."

    class PastryChef(Chef):
        def cook(self):
            return f"{self.name} готовит торт."

    # Полиморфизм: метод cook вызывается для разных объектов
    def chef_cooking(chef):
        return chef.cook()

    chef1 = Chef("Алекс")
    chef2 = PastryChef("Мария")

    return f"{chef_cooking(chef1)} <br> {chef_cooking(chef2)}"


# Инкапсуляция
@app.route('/encapsulation')
def encapsulation_example():
    class Chef:
        def __init__(self, name):
            self.name = name
            self.__secret_ingredient = "ваниль"  # Приватное поле

        def cook(self):
            return f"{self.name} готовит с секретным ингредиентом."

        def get_secret_ingredient(self):
            return self.__secret_ingredient

    chef = Chef("Гарри")
    return f"{chef.cook()} <br> Секретный ингредиент: {chef.get_secret_ingredient()}"


# 13. Интерфейсы и абстрактные классы ==================================================================================
@app.route('/abstract')
def abstract_example():
    # Абстрактный класс Повар
    class Chef(ABC):
        @abstractmethod
        def cook(self):
            pass

    # Конкретный повар, который реализует абстрактный метод
    class PastryChef(Chef):
        def cook(self):
            return "Кондитер готовит пирожное."

    # Создание объекта класса
    pastry_chef = PastryChef()

    return pastry_chef.cook()


# 14. List Comprehension ===============================================================================================
# Создаем список квадратов чисел от 0 до 9
squares = [x ** 2 for x in range(10)]
print(squares)  # Вывод: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 15. Генераторы и итераторы ===========================================================================================
def my_generator():
    for i in range(3):
        yield i  # возвращает одно значение за раз


gen = my_generator()
for dish in gen:
    print(f"Подали блюдо {dish}")


# 16. Decorators =======================================================================================================
def decorator(func):
    def wrapper():
        print("Приятного аппетита!")
        func()
        print("Убираем тарелку.")

    return wrapper


@decorator
def serve_dish():
    print("Подаем блюдо.")


serve_dish()

# 17. Context Managers =================================================================================================
with open('recipe.txt', 'r') as f:
    recipe = f.read()
    print(recipe)

# 18. Функциональное программирование ==================================================================================
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Вывод: 10

# Также есть map() и filter(), которые можно использовать:
# Применяем функцию ко всем элементам
result = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8]
print(result)

# Фильтруем элементы
filtered = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
print(filtered)


# 19. Шаблоны проектирования ===========================================================================================

# Singleton (Одиночка)
class HeadChef:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Создаём несколько "главных поваров"
chef1 = HeadChef()
chef2 = HeadChef()
# Они оба указывают на один и тот же объект
assert chef1 is chef2


# Factory (Фабрика)
class Pizza:
    def prepare(self):
        return "Готовим пиццу!"


class Sushi:
    def prepare(self):
        return "Готовим суши!"


class DishFactory:
    @staticmethod
    def get_dish(dish_type):
        if dish_type == "pizza":
            return Pizza()
        elif dish_type == "sushi":
            return Sushi()


# Клиент заказывает блюдо
dish = DishFactory.get_dish("pizza")
print(dish.prepare())  # Вывод: "Готовим пиццу!"


# Observer (Наблюдатель)
class OrderObservable:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, order):
        for observer in self._observers:
            observer.update(order)


class Waiter:
    def update(self, order):
        print(f"Официант получает заказ: {order}")


# Клиент делает заказ, а официант наблюдает за этим
restaurant = OrderObservable()
waiter = Waiter()
restaurant.subscribe(waiter)
restaurant.notify("Пицца Маргарита")

# END ==================================================================================================================

if __name__ == '__main__':
    app.run(debug=True)
