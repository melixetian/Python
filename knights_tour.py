#!/usr/bin/env python3

"""
Задача о ходе коня (Knight's Tour)
Проверяет, может ли конь пройти по всем клеткам шахматной доски,
не повторяя позиции. Выводит шахматную доску с номерами ходов.
"""

import random
import sys


def chess_to_coords(chess_notation):
    """Преобразует шахматную нотацию (например, 'a1', 'b6') в координаты (row, col)."""
    if len(chess_notation) != 2:
        raise ValueError("Неверный формат шахматной нотации. Используйте формат, например: a1, b6")

    col_char = chess_notation[0].lower()
    row_char = chess_notation[1]

    if col_char < "a" or col_char > "h":
        raise ValueError("Колонка должна быть от 'a' до 'h'")
    if row_char < "1" or row_char > "8":
        raise ValueError("Строка должна быть от '1' до '8'")

    col = ord(col_char) - ord("a")
    row = 8 - int(row_char)

    return row, col


def coords_to_chess(row, col):
    """Преобразует координаты (row, col) в шахматную нотацию."""
    col_char = chr(ord("a") + col)
    row_char = str(8 - row)
    return col_char + row_char


def is_valid_move(row, col, board):
    """Проверяет, является ли ход валидным (в пределах доски и клетка не посещена)."""
    return 0 <= row < 8 and 0 <= col < 8 and board[row][col] == 0


def get_knight_moves(row, col):
    """Возвращает все возможные ходы коня из данной позиции."""
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    return [(row + dr, col + dc) for dr, dc in moves]


def count_available_moves(row, col, board):
    """Подсчитывает количество доступных ходов из данной позиции (эвристика Варнсдорфа)."""
    count = 0
    for next_row, next_col in get_knight_moves(row, col):
        if is_valid_move(next_row, next_col, board):
            count += 1
    return count


def knights_tour(start_row, start_col, board, move_number):
    """
    Рекурсивная функция для поиска пути коня с использованием эвристики Варнсдорфа.
    """
    # Если все клетки посещены, путь найден
    if move_number == 65:  # 64 клетки + 1 (начальная позиция считается как ход 1)
        return True

    # Получаем все возможные ходы
    possible_moves = get_knight_moves(start_row, start_col)

    # Фильтруем валидные ходы
    valid_moves = [(r, c) for r, c in possible_moves if is_valid_move(r, c, board)]

    # Применяем эвристику Варнсдорфа: сортируем по количеству доступных ходов
    # (выбираем клетки с наименьшим количеством возможных ходов)
    valid_moves.sort(key=lambda move: count_available_moves(move[0], move[1], board))

    # Пробуем каждый ход
    for next_row, next_col in valid_moves:
        # Делаем ход
        board[next_row][next_col] = move_number

        # Рекурсивно ищем следующий ход
        if knights_tour(next_row, next_col, board, move_number + 1):
            return True

        # Если путь не найден, откатываем ход (backtracking)
        board[next_row][next_col] = 0

    return False


def print_board(board):
    """Выводит шахматную доску с номерами ходов."""
    # ANSI escape коды для цветов
    RESET = "\033[0m"
    BLACK_BG = "\033[40m"  # Черный фон
    WHITE_BG = "\033[47m"  # Белый фон
    BLACK_TEXT = "\033[30m"  # Черный текст
    WHITE_TEXT = "\033[37m"  # Белый текст
    GRAY = "\033[90m"  # Серый цвет для сетки

    def is_dark_square(row, col):
        """Определяет, является ли клетка темной (черной)."""
        return (row + col) % 2 == 1

    print("\nШахматная доска с номерами ходов коня:")

    # Верхний заголовок с буквами
    print("   ", end="")
    for col in range(8):
        print(f"  {chr(ord('a') + col)} ", end="")
    print()

    # Верхняя граница
    print(f"{GRAY}   ┌", end="")
    for col in range(8):
        print("───", end="")
        if col < 7:
            print("┬", end="")
    print(f"┐{RESET}")

    # Строки с данными
    for row in range(8):
        print(f"{GRAY}{8 - row:2} │{RESET}", end="")
        for col in range(8):
            value = board[row][col]
            is_dark = is_dark_square(row, col)

            # Выбираем цвет фона и текста в зависимости от цвета клетки
            if is_dark:
                bg_color = BLACK_BG
                text_color = WHITE_TEXT
            else:
                bg_color = WHITE_BG
                text_color = BLACK_TEXT

            # Выводим значение с цветом
            print(f"{bg_color}{text_color}{value:3}{RESET}", end="")
            print(f"{GRAY}│{RESET}", end="")
        print(f"{GRAY} {8 - row}{RESET}")

        # Горизонтальный разделитель (кроме последней строки)
        if row < 7:
            print(f"{GRAY}   ├", end="")
            for col in range(8):
                print("───", end="")
                if col < 7:
                    print("┼", end="")
            print(f"┤{RESET}")

    # Нижняя граница
    print(f"{GRAY}   └", end="")
    for col in range(8):
        print("───", end="")
        if col < 7:
            print("┴", end="")
    print(f"┘{RESET}")

    # Нижний заголовок с буквами
    print("   ", end="")
    for col in range(8):
        print(f"  {chr(ord('a') + col)} ", end="")
    print()


def main():
    """Основная функция программы."""
    # Инициализируем доску (0 означает, что клетка не посещена)
    board = [[0 for _ in range(8)] for _ in range(8)]

    # Определяем начальную позицию
    if len(sys.argv) > 1:
        # Позиция задана аргументом командной строки
        try:
            start_pos = sys.argv[1]
            start_row, start_col = chess_to_coords(start_pos)
            print(f"Начальная позиция задана: {start_pos}")
        except ValueError as exc:
            print(f"Ошибка: {exc}")
            print("Использование: python knights_tour.py [позиция]")
            print("Пример: python knights_tour.py a1")
            sys.exit(1)
    else:
        # Позиция выбирается случайным образом
        start_row = random.randint(0, 7)
        start_col = random.randint(0, 7)
        start_pos = coords_to_chess(start_row, start_col)
        print(f"Начальная позиция выбрана случайно: {start_pos}")

    # Отмечаем начальную позицию как первый ход
    board[start_row][start_col] = 1

    print(f"Координаты: строка {start_row}, колонка {start_col}")
    print("Ищу путь коня...")

    # Ищем путь
    if knights_tour(start_row, start_col, board, 2):
        print("\nПуть найден! Конь может пройти по всем клеткам.")
        print_board(board)
    else:
        print("\nПуть не найден. Конь не может пройти по всем клеткам из данной позиции.")
        print_board(board)


if __name__ == "__main__":
    main()
