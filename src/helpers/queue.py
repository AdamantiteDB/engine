from typing import TypeVar, Generic, List

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self.__items: List[T] = []

    def push(self, item: T):
        self.__items.push(item)

    def pull(self):
        return self.__items.pop(0)

    def clear(self):
        self.__items = []

    def __repr__(self):
        return self.__items
