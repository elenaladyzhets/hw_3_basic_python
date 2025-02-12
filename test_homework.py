
def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():

    a = 10
    b = 20

    perimeter = 2*(a+b)
    # периметр прямоугольника
    assert perimeter == 60
    # площадь прямоугольника
    area = a*b

    assert area == 200
    print("Периметр прямоугольника = ", perimeter, "Площадь прямоугольника = ", area)

def test_circle():
    import math
    r = 23
    # площадь круга
    area = math.pi * r**2

    assert area == 1661.9025137490005

    # длина окружности
    length = 2*math.pi*r
    print("Площадь круга = ", area, "Длина круга = ", length)
    assert length == 144.51326206513048


def test_random_list():
    import random

    # список из 10 рандомных чисел
    l = [random.randint(1, 100), random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100) ]
    l.sort()
    print(l)

    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements():

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # Удаление повторяющихся элементов (приведение списка во множество и обратно в список)
    l=list(set(l))
    print(l)


    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # создание словаря
    d = dict(zip(first,second))
    print(d)

    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second