import copy


class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    """
    Python предоставляет свой собственный интерфейс прототипа с помощью функций `copy.copy` и
    `copy.deepcopy`. И любой класс, который хочет реализовать пользовательские реализации, 
    должен переопределить функции-члены `__copy__` и `__deepcopy__`.
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Создайте неглубокую копию. Этот метод будет вызываться всякий раз, когда кто-либо вызывает
        `copy.copy` с этим объектом, и возвращаемое значение возвращается как новая неглубокая копия.
        """

        # First, let's create copies of the nested objects.
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        """
        Создайте глубокую копию. Этот метод будет вызываться всякий раз, когда кто-либо вызывает
        `copy.deepcopy` с этим объектом, и возвращаемое значение возвращается как новая глубокая копия.

        Для чего используется аргумент `memo`? Memo - это словарь, который используется библиотекой 
        `deepcopy` для предотвращения бесконечных рекурсивных копий в экземплярах циклических ссылок. 
        Передавайте его всем вызовам `deepcopy`, которые вы выполняете в реализации `__deepcopy__`, 
        чтобы предотвратить бесконечные рекурсии.
        """

        if memo is None:
            memo = {}

        # Сначала давайте создадим копии вложенных объектов.
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Затем давайте клонируем сам объект, используя подготовленные клоны вложенных объектов.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)

    # Давайте изменим список в shallow_copied_component и посмотрим, 
    # изменится ли он при рекурсиях компонентов.
    shallow_copied_component.some_list_of_objects.append("another object")
    if component.some_list_of_objects[-1] == "another object":
        print(
            "Добавление элементов в `shallow_copied_component` "
            "some_list_of_objects добавляет его к `component` "
            "some_list_of_objects."
        )
    else:
        print(
            "Добавление элементов в `shallow_copied_component`'s "
            "some_list_of_objects не добавляет его к `component`'s "
            "some_list_of_objects."
        )

    # Давайте изменим набор в списке объектов.
    component.some_list_of_objects[1].add(4)
    if 4 in shallow_copied_component.some_list_of_objects[1]:
        print(
            "Изменение элементов в `component` some_list_of_objects "
            "изменяет этот объект в `shallow_copied_component`"
            "some_list_of_objects."
        )
    else:
        print(
            "Изменение объектов в `component` some_list_of_objects "
            "не изменяет этот объект в `shallow_copied_component`'s "
            "some_list_of_objects."
        )

    deep_copied_component = copy.deepcopy(component)

    # Давайте изменим список в deep_copied_component и посмотрим, изменится ли он в компоненте.
    deep_copied_component.some_list_of_objects.append("one more object")
    if component.some_list_of_objects[-1] == "one more object":
        print(
            "Добавление элементов в `deep_copied_component` "
            "some_list_of_objects добавляет его к `component`"
            "some_list_of_objects."
        )
    else:
        print(
            "Добавление элементов в `deep_copied_component`"
            "some_list_of_objects добавляет его к  `component` "
            "some_list_of_objects."
        )

    # Давайте изменим набор в списке объектов.
    component.some_list_of_objects[1].add(10)
    if 10 in deep_copied_component.some_list_of_objects[1]:
        print(
            "Изменение элементов в `component` some_list_of_objects "
            "изменяет этот объект в `deep_copied_component`"
            "some_list_of_objects."
        )
    else:
        print(
            "Изменение элементов в `component` some_list_of_objects "
            "не изменяет этот объект в `deep_copied_component`'s "
            "some_list_of_objects."
        )

    print(
        f"id(deep_copied_component.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent)}"
    )
    print(
        f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
        f"{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
    )
    print(
        "^^ Это показывает, что объекты с глубоким копированием содержат одну и ту же ссылку, они не клонируются повторно."
    )