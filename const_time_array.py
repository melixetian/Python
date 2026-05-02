"""
Реализовать класс ConstTimeArray и его методы таким образом,
чтобы все методы имели константную сложность - O(1).
"""


class ConstTimeArray:
    def __init__(self, length):
        self._data = [None] * length
        self._version = [0] * length
        self._current_version = 1

        self._all_value = None
        self._all_version = 0

    def get(self, i):
        if self._version[i] >= self._all_version:
            return self._data[i]
        return self._all_value

    def set(self, i, value):
        self._data[i] = value
        self._version[i] = self._current_version
        self._current_version += 1

    def set_all(self, value):
        self._all_value = value
        self._all_version = self._current_version
        self._current_version += 1
