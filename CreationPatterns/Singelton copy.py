class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self): 
        """
        Должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """
        # ...


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Работает Singleton, обе переменные \
              содержат один и тот же экземпляр.")
    else:
        print("Ошибка Singleton, переменные содержат \
              разные экземпляры.")