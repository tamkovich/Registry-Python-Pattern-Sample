registry = {}


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        if hasattr(cls, '_name'):
            registry[cls._name] = cls
        else:
            registry[cls.__name__] = cls
        return cls


class Environment:

    def __getitem__(self, classname):
        return registry[classname]

    def __repr__(self):
        return str(registry)


class Registry(metaclass=Meta):

    env = Environment()
