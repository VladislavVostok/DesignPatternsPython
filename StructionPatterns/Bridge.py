from __future__ import annotations
from abc import ABC, abstractmethod

# Абстракция
class Abstraction:
    """
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Базовая операция с:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Расширенная работа с:\n"
                f"{self.implementation.operation_implementation()}")


# Реализация
class Implementation(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Каждая Конкретная Реализация соответствует определённой платформе и реализует
интерфейс Реализации с использованием API этой платформы.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Вот результат на платформе А."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Вот результат на платформе B."


def client_code(abstraction: Abstraction) -> None:
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определённым объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """
    
    interface_var = "nt"
    if "nt" == interface_var:
        implementation = ConcreteImplementationA()
        abstraction = Abstraction(implementation)
        client_code(abstraction)
    elif "linux" == interface_var:
        print("\n")

        implementation = ConcreteImplementationB()
        abstraction = ExtendedAbstraction(implementation)
        client_code(abstraction)