"""
LC 146. LRU Cache
https://leetcode.com/problems/lru-cache/

Реализовать структуру данных LRU-кеша (Least Recently Used — вытеснение
наименее недавно использованного элемента) фиксированной вместимости capacity.

Методы:
    LRUCache(capacity) — инициализировать кеш положительного размера capacity.
    get(key) — вернуть значение по ключу key, если он есть в кеше, иначе -1.
    put(key, value) — обновить значение ключа key, если он уже есть, иначе
        добавить пару (key, value). Если после добавления число ключей превышает
        capacity, удалить ключ, к которому дольше всего не обращались.

Методы get и put должны работать за O(1) в среднем по времени.

Пример:
    cache = LRUCache(2)
    cache.put(1, 1)  # кеш: {1=1}
    cache.put(2, 2)  # кеш: {1=1, 2=2}
    cache.get(1)     # 1, теперь ключ 1 самый «свежий»: {2=2, 1=1}
    cache.put(3, 3)  # вытесняется ключ 2, кеш: {1=1, 3=3}
    cache.get(2)     # -1 (не найден)
    cache.put(4, 4)  # вытесняется ключ 1, кеш: {3=3, 4=4}
    cache.get(1)     # -1 (не найден)
    cache.get(3)     # 3
    cache.get(4)     # 4

Ограничения:
    1 <= capacity <= 3000
    0 <= key <= 10**4
    0 <= value <= 10**5
    Не более 2 * 10**5 вызовов get и put суммарно.
"""


class Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.oldest = Node()
        self.latest = Node()
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def insert(self, node: Node) -> None:
        prev_node = self.latest.prev
        assert prev_node is not None
        prev_node.next = node
        node.prev = prev_node
        node.next = self.latest
        self.latest.prev = node

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        assert prev_node is not None and next_node is not None
        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_end(self, node: Node) -> None:
        self.remove(node)
        self.insert(node)

    def pop_oldest(self) -> Node:
        lru_node = self.oldest.next
        assert lru_node is not None
        self.remove(lru_node)
        return lru_node


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = dict[int, Node]()
        self.history = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.history.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.history.move_to_end(node)
            return

        if len(self.cache) >= self.capacity:
            lru_node = self.history.pop_oldest()
            self.cache.pop(lru_node.key)

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.history.insert(new_node)
