"""
A class of which only one instance can exist
Example, Prime Minister of India or __main__ method in Python
"""

class MySingleton(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = MySingleton()
        return cls.INSTANCE

obj1 = MySingleton.get_instance()
obj2 = MySingleton()
