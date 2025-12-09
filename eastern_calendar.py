"""
Программа выводит знак зодиака по дате рождения
и символьное изображение года по китайскому календарю.
"""

from datetime import datetime

ANIMALS = [
    "Крыса",
    "Бык",
    "Тигр",
    "Кролик",
    "Дракон",
    "Змея",
    "Лошадь",
    "Овца",
    "Обезьяна",
    "Петух",
    "Собака",
    "Свинья",
]

ELEMENTS = [
    "Дерево",
    "Огонь",
    "Земля",
    "Металл",
    "Вода",
]

ENERGIES = [
    "Ян",
    "Инь",
]


def get_eastern_year_symbol(year: int) -> tuple[str, str, str]:
    """
    Вернёт тройку (животное, стихия, энергия) для заданного года.

    Используется 60-летний цикл, где:
    - 1984 год — начало цикла: Дерево, Ян, Крыса.
    """
    # Сдвигаем к началу цикла (1984 — год Деревянной Крысы, Ян)
    offset = year - 1984

    # Животные повторяются каждые 12 лет
    animal = ANIMALS[offset % 12]

    # Небесные стволы (10 вариантов = 5 стихий * 2 энергии)
    stem_index = offset % 10
    element = ELEMENTS[stem_index // 2]  # каждые 2 года одна стихия
    energy = ENERGIES[stem_index % 2]  # чётные — Ян, нечётные — Инь

    return animal, element, energy


def get_western_zodiac_sign(day: int, month: int) -> str:
    """Вернёт знак зодиака по западному календарю для заданной даты."""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Овен"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Телец"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Близнецы"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Рак"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Лев"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Дева"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Весы"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Скорпион"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Стрелец"
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Козерог"
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Водолей"
    # Остаток диапазона: 19.02–20.03
    return "Рыбы"


def main() -> None:
    try:
        date_str = input("Введите дату (ДД.MM.ГГГГ) или год: ").strip()

        if "." in date_str:
            dt = datetime.strptime(date_str, "%d.%m.%Y")
            western_zodiac = get_western_zodiac_sign(dt.day, dt.month)
            animal, element, energy = get_eastern_year_symbol(dt.year)

            print(f"Дата: {dt.strftime('%d.%m.%Y')}")
            print(f"Знак зодиака: {western_zodiac}")
            print("Символ года:")
            print(f"  Животное: {animal}")
            print(f"  Стихия:   {element}")
            print(f"  Энергия:  {energy}")
        else:
            year = int(date_str)
            animal, element, energy = get_eastern_year_symbol(year)

            print(f"Год {year}:")
            print(f"Животное: {animal}")
            print(f"Стихия:   {element}")
            print(f"Энергия:  {energy}")
    except ValueError:
        print(
            "Ошибка: введите либо дату в формате ДД.MM.ГГГГ (например 15.07.1991), " "либо целый год (например 1991)."
        )


if __name__ == "__main__":
    main()
