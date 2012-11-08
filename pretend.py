import sys

PY3K = sys.version_info >= (3,)


class stub(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def _build_special(name):
        def inner(self, *args, **kwargs):
            return self.__dict__[name](*args, **kwargs)
        inner.__name__ = name
        return inner

    __iter__ = _build_special("__iter__")

    __lt__ = _build_special("__lt__")
    __le__ = _build_special("__le__")
    __eq__ = _build_special("__eq__")
    __ne__ = _build_special("__ne__")
    __gt__ = _build_special("__gt__")
    __ge__ = _build_special("__ge__")

    __add__ = _build_special("__add__")
    __and__ = _build_special("__and__")
    if PY3K:
        __div__ = _build_special("__div__")
    __lshift__ = _build_special("__lshift__")
    __mod__ = _build_special("__mod__")
    __mul__ = _build_special("__mul__")
    __or__ = _build_special("__or__")
    __pow__ = _build_special("__pow__")
    __rshift__ = _build_special("__rshift__")
    __sub__ = _build_special("__sub__")
    __truediv__ = _build_special("__truediv__")
    __xor__ = _build_special("__xor__")
