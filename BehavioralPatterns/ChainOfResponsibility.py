from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Банан":
            return f"Обезъяна: я съем  {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Орех":
            return f"Белка: я съем  {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Фрикадельку":
            return f"Собака: я съем {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    Обычно клиентский код приспособлен для работы с единственным обработчиком. В
    большинстве случаев клиенту даже неизвестно, что этот обработчик является
    частью цепочки.
    """

    for food in ["Орех", "Банан", "Кружка кофе"]:
        print(f"\nClient: Кто хочет {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} остался нетронутым.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
    # только первому в цепочке.
    print("Chain: Обезьяна > Белка > Собака")
    client_code(monkey)
    print("\n")

    print("Subchain: Белка > Собака")
    client_code(squirrel)