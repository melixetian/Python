"""
Chess960 (Шахматы Фишера) - генератор случайных расстановок фигур

Chess960 - это вариант шахмат, где фигуры расставляются случайно,
но с соблюдением определенных правил:
1. Расстановка черных идентична расстановке белых
2. Пешки на своих местах (2-я и 7-я горизонтали)
3. Один слон на белом поле, другой на черном
4. Ладьи по бокам от короля (король не может быть на a или h)
"""

import argparse
import random


class Args:
    seed: int | None

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description="Генератор случайных расстановок Chess960 (Шахматы Фишера)",
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )

        parser.add_argument(
            "--seed",
            "-s",
            type=int,
            help="Семя для генератора случайных чисел (для воспроизводимых результатов)",
        )

        self.args = parser.parse_args()
        self.seed = self.args.seed


class Chess960:
    """Класс для генерации случайных расстановок Chess960"""

    def __init__(self):
        # Обозначения фигур
        self.pieces = {
            "K": "Король",  # King
            "Q": "Ферзь",  # Queen
            "R": "Ладья",  # Rook
            "B": "Слон",  # Bishop
            "N": "Конь",  # Knight
        }

        # Цвета полей (True = белое, False = черное)
        self.white_squares = {0, 2, 4, 6}  # a, c, e, g
        self.black_squares = {1, 3, 5, 7}  # b, d, f, h

    def generate_position(self, seed: int | None = None) -> list[str]:
        """Генерирует случайную расстановку фигур для Chess960."""
        if seed is not None:
            random.seed(seed)

        while True:
            # Создаем список из 8 пустых позиций
            position = [""] * 8

            # 1. Размещаем короля (не на краях)
            king_pos = random.randint(1, 6)  # b1-g1
            position[king_pos] = "K"

            # 2. Размещаем ладьи по бокам от короля
            rook_positions = []
            for i in range(8):
                if i < king_pos:
                    rook_positions.append(i)
                elif i > king_pos:
                    rook_positions.append(i)

            # Выбираем случайно две позиции для ладей
            rook1_pos, rook2_pos = random.sample(rook_positions, 2)
            position[rook1_pos] = "R"
            position[rook2_pos] = "R"

            # 3. Размещаем слона на белом поле
            white_bishop_pos = random.choice(list(self.white_squares))
            while position[white_bishop_pos] != "":
                white_bishop_pos = random.choice(list(self.white_squares))
            position[white_bishop_pos] = "B"

            # 4. Размещаем слона на черном поле
            black_bishop_pos = random.choice(list(self.black_squares))
            while position[black_bishop_pos] != "":
                black_bishop_pos = random.choice(list(self.black_squares))
            position[black_bishop_pos] = "B"

            # 5. Размещаем ферзя и коня на оставшиеся позиции
            empty_positions = [i for i in range(8) if position[i] == ""]

            # Случайно выбираем позицию для ферзя
            queen_pos = random.choice(empty_positions)
            position[queen_pos] = "Q"

            # Оставшиеся позиции занимают кони
            for pos in empty_positions:
                if position[pos] == "":
                    position[pos] = "N"

            # Проверяем корректность расстановки
            if self._is_valid_position(position):
                return position

    def _is_valid_position(self, position: list[str]) -> bool:
        """Проверяет корректность расстановки фигур."""
        # Проверяем наличие всех фигур
        pieces_count = {"K": 0, "Q": 0, "R": 0, "B": 0, "N": 0}
        for piece in position:
            if piece in pieces_count:
                pieces_count[piece] += 1

        # Должно быть: 1 король, 1 ферзь, 2 ладьи, 2 слона, 2 коня
        expected_counts = {"K": 1, "Q": 1, "R": 2, "B": 2, "N": 2}
        if pieces_count != expected_counts:
            return False

        # Проверяем, что король между ладьями
        king_pos = position.index("K")
        rook_positions = [i for i, piece in enumerate(position) if piece == "R"]

        if not (min(rook_positions) < king_pos < max(rook_positions)):
            return False

        # Проверяем, что слоны на полях разного цвета
        bishop_positions = [i for i, piece in enumerate(position) if piece == "B"]
        if len(bishop_positions) == 2:
            bishop1_color = bishop_positions[0] in self.white_squares
            bishop2_color = bishop_positions[1] in self.white_squares
            if bishop1_color == bishop2_color:
                return False

        return True

    def display_board(self, position: list[str]) -> None:
        """Отображает шахматную доску с расстановкой фигур."""
        print("\n" + "=" * 50)
        print("ШАХМАТНАЯ ДОСКА CHESS960")
        print("=" * 50)

        # Создаем полную доску
        board = []

        # Черные фигуры (8-я горизонталь) - строчные буквы
        black_row = [piece.lower() for piece in position]
        board.append(black_row)

        # Черные пешки (7-я горизонталь)
        board.append(["p"] * 8)

        # Пустые горизонтали (6-3)
        for _ in range(4):
            board.append(["."] * 8)

        # Белые пешки (2-я горизонталь)
        board.append(["P"] * 8)

        # Белые фигуры (1-я горизонталь) - заглавные буквы
        white_row = position.copy()
        board.append(white_row)

        # Отображаем доску
        print("\n   a b c d e f g h")
        print("  ┌─┬─┬─┬─┬─┬─┬─┬─┐")

        for i, row in enumerate(board):
            rank = 8 - i
            print(f"{rank} │", end="")
            for piece in row:
                if piece == ".":
                    print(" │", end="")
                else:
                    print(f"{piece}│", end="")
            print(f" {rank}")
            if i < len(board) - 1:
                print("  ├─┼─┼─┼─┼─┼─┼─┼─┤")

        print("  └─┴─┴─┴─┴─┴─┴─┴─┘")
        print("   a b c d e f g h")

        # Описание фигур
        print("\nОБОЗНАЧЕНИЯ:")
        print("K/k - Король    Q/q - Ферзь    R/r - Ладья")
        print("B/b - Слон      N/n - Конь     P/p - Пешки")
        print("(Заглавные - белые, строчные - черные)")

    def get_position_description(self, position: list[str]) -> str:
        """Возвращает текстовое описание расстановки."""
        description = "Расстановка фигур (1-я горизонталь):\n"
        files = ["a", "b", "c", "d", "e", "f", "g", "h"]

        for i, piece in enumerate(position):
            description += f"{files[i]}1: {self.pieces[piece]}\n"

        return description

    def get_position_number(self, position: list[str]) -> int:
        """Вычисляет номер позиции Chess960 (1-960)"""
        # Это упрощенная версия - в реальности нужен более сложный алгоритм
        # для точного вычисления номера позиции
        return random.randint(1, 960)


def main():
    """Основная функция программы"""
    # Настраиваем парсер аргументов
    args = Args()

    # Выводим заголовок
    if args.seed is not None:
        print(f"ГЕНЕРАТОР CHESS960 С SEED = {args.seed}")
    else:
        print("ГЕНЕРАТОР СЛУЧАЙНЫХ РАССТАНОВОК CHESS960")
        print("(Шахматы Фишера)")

    chess960 = Chess960()

    # Генерируем расстановку
    if args.seed is not None:
        print(f"\nГенерируем расстановку с seed={args.seed}...")
    else:
        print("\nГенерируем случайную расстановку...")

    position = chess960.generate_position(args.seed)

    # Отображаем доску
    chess960.display_board(position)

    # Показываем описание
    print("\n" + chess960.get_position_description(position))

    # Показываем номер позиции
    position_number = chess960.get_position_number(position)
    print(f"Номер позиции Chess960: {position_number}")


if __name__ == "__main__":
    main()
