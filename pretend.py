class stub(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def _build_special(name):
        def inner(self, *args, **kwargs):
            return self.__dict__[name](*args, **kwargs)
        inner.__name__ = name
        return inner

    __iter__ = _build_special("__iter__")
    __add__ = _build_special("__add__")
    __sub__ = _build_special("__sub__")
    __mul__ = _build_special("__mul__")
