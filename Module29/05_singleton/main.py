def singleton(cls):
    def wrapper(*args, **kwargs):
        print('Создаётся инстанс...')
        instance = cls(*args, **kwargs)
        return instance
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
