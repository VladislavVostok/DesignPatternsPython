if __name__ == "__main__":

    def null_decorator(func):
        return func


    # def greet():
    #     return 'Shalom Shabbat!'

    # greet = null_decorator(greet)

    # @null_decorator
    # def greet():
    #     return 'Shalom Shabbat!'

    # greet()


    # def uppercase(func):
    #     def wrapper():
    #         original_result = func()
    #         modified_result = original_result.upper()
    #         return modified_result
    #     return wrapper

    # @uppercase
    # def greet():
    #     return 'Shalom Shabbat!'


    # def strong(func):
    #     def wrapper():
    #         return '<strong>' + func() + '</strong>'
    #     return wrapper

    # def emphasis(func):
    #     def wrapper():
    #         return '<em>' + func() + '</em>'
    #     return wrapper


    # @strong
    # @emphasis
    # def greet():
    #     return 'Shalom Shabbat!'

    # print(greet())

    def trace(func):
        def wrapper(*args, **kwargs):
            print(f'TRACE: calling {func.__name__}() '
                f'with {args}, {kwargs}')

            original_result = func(*args, **kwargs)

            print(f'TRACE: {func.__name__}() '
                f'returned {original_result!r}')

            return original_result
        return wrapper

    @trace
    def say(name, line):
        return f'{name}: {line}'

    print(say("Изя", "Hava Nagila"))


    from math import factorial

    def multy_factorial(func): 
        def wrapper():
            factor = func(6)    
            mul_f = factor * 2
            return mul_f
        return wrapper

        res = multy_factorial(factorial)
        print(res())