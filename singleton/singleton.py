class Singleton:
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

class SingletonMeta(type):
    _isinstance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._isinstance:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._isinstance[cls] = instance
        return cls._isinstance


class Singleton(metaclass=SingletonMeta):
    pass


class MyClass(Singleton):
    pass


s1 = MyClass()
s2 = MyClass()
print(s1 is s2)

