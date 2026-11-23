"""
LC 460. LFU Cache
https://leetcode.com/problems/lfu-cache/

Реализовать структуру данных LFU-кеша (Least Frequently Used — вытеснение
наименее часто используемого элемента) фиксированной вместимости capacity.

Для каждого ключа в кеше ведётся счётчик обращений (freq):
    - при первой вставке нового ключа через put его счётчик равен 1;
    - любой вызов get(key) (если ключ найден) или put(key, value)
        по уже существующему ключу увеличивает его счётчик на 1.

Методы:
    LFUCache(capacity) — инициализировать кеш положительного размера capacity.
    get(key) — вернуть значение по ключу key, если он есть в кеше, иначе -1.
    put(key, value) — обновить значение ключа key, если он уже есть, иначе
        добавить пару (key, value). Если кеш уже заполнен (достиг capacity),
        перед вставкой нового элемента нужно удалить ключ с минимальным
        счётчиком обращений. Если таких ключей несколько, среди них удаляется
        наименее недавно использованный (по правилу LRU).

Методы get и put должны работать за O(1) в среднем по времени.

Пример:
    lfu = LFUCache(2)
    lfu.put(1, 1)  # кеш: {1=1}, freq: {1: 1}
    lfu.put(2, 2)  # кеш: {1=1, 2=2}, freq: {1: 1, 2: 1}
    lfu.get(1)     # 1, freq: {1: 2, 2: 1}
    lfu.put(3, 3)  # вытесняется 2 (у него min freq = 1), freq: {1: 2, 3: 1}
    lfu.get(2)     # -1 (не найден)
    lfu.get(3)     # 3, freq: {1: 2, 3: 2}
    lfu.put(4, 4)  # у 1 и 3 одинаковая freq = 2, но 1 старше (LRU) -> удаляем 1
    lfu.get(1)     # -1 (не найден)
    lfu.get(3)     # 3, freq: {3: 3, 4: 1}
    lfu.get(4)     # 4, freq: {3: 3, 4: 2}

Ограничения:
    1 <= capacity <= 10**4
    0 <= key <= 10**5
    0 <= value <= 10**9
    Не более 2 * 10**5 вызовов get и put суммарно.
"""


class Node:
    def __init__(self, key: int = 0, value: int = 0, freq: int = 1) -> None:
        self.key = key
        self.value = value
        self.freq = freq
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.oldest = Node()
        self.latest = Node()
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def is_empty(self) -> bool:
        """Проверяет, пуст ли список."""
        return self.oldest.next is self.latest

    def insert(self, node: Node) -> None:
        """Добавляет узел в конец списка."""
        prev_node = self.latest.prev
        assert prev_node is not None
        prev_node.next = node
        node.prev = prev_node
        node.next = self.latest
        self.latest.prev = node

    def remove(self, node: Node) -> None:
        """Удаляет узел из списка."""
        prev_node = node.prev
        next_node = node.next
        assert prev_node is not None and next_node is not None
        prev_node.next = next_node
        next_node.prev = prev_node

    def pop_oldest(self) -> Node:
        """Удаляет и возвращает узел из начала списка."""
        lru_node = self.oldest.next
        assert lru_node is not None
        self.remove(lru_node)
        return lru_node


class FrequencyHistory:
    def __init__(self) -> None:
        self.freq_to_nodes = dict[int, DoublyLinkedList]()
        self.min_freq = 1

    def insert(self, node: Node) -> None:
        """Добавляет узел в корзину, соответствующую его текущей частоте node.freq."""
        if node.freq not in self.freq_to_nodes:
            self.freq_to_nodes[node.freq] = DoublyLinkedList()

        self.freq_to_nodes[node.freq].insert(node)
        if node.freq == 1:
            self.min_freq = 1

    def log_access(self, node: Node) -> None:
        """Повышает частоту узла и переносит его в следующую корзину."""
        old_freq = node.freq
        node.freq += 1
        self.freq_to_nodes[old_freq].remove(node)
        self.insert(node)

        if self.freq_to_nodes[old_freq].is_empty():
            self.freq_to_nodes.pop(old_freq)
            if old_freq == self.min_freq:
                self.min_freq += 1

    def pop_lfu(self) -> Node:
        """Удаляет и возвращает узел с минимальной частотой (и самый старый при ничьей)."""
        lru_node = self.freq_to_nodes[self.min_freq].pop_oldest()
        if self.freq_to_nodes[self.min_freq].is_empty():
            self.freq_to_nodes.pop(self.min_freq)
        return lru_node


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = dict[int, Node]()
        self.history = FrequencyHistory()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.history.log_access(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.history.log_access(node)
            return

        if len(self.cache) >= self.capacity:
            lfu_node = self.history.pop_lfu()
            self.cache.pop(lfu_node.key)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.history.insert(new_node)
