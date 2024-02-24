class Target:
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        return "Target: Поведение цели по умолчанию."


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        return ".)eetpadA( огомеуритпадА еинедевоп еобосО"


class Adapter(Target, Adaptee):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: Я прекрасно могу работать с целевыми объектами:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: Класс Adaptee имеет странный интерфейс. "
          "Врядли, я этого не понимаю:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    
    print("Client: Но я могу работать с ним через адаптер:")
    adapter = Adapter()
    client_code(adapter)