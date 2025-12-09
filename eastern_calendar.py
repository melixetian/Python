"""
Программа выводит символьное изображение года по китайскому календарю.
"""

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


def main() -> None:
    try:
        year_str = input("Введите год: ").strip()
        year = int(year_str)
    except ValueError:
        print("Ошибка: нужно ввести целое число года, например 1991.")
        return

    animal, element, energy = get_eastern_year_symbol(year)

    print(f"Год {year}:")
    print(f"Животное: {animal}")
    print(f"Стихия:   {element}")
    print(f"Энергия:  {energy}")


if __name__ == "__main__":
    main()
