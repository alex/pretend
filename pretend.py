import sys

PY3K = sys.version_info >= (3,)


methods = set([
    "__iter__",
    "__lt__",
    "__le__",
    "__eq__",
    "__ne__",
    "__gt__",
    "__ge__",

    "__add__",
    "__and__",
    "__divmod__",
    "__floordiv__",
    "__lshift__",
    "__mod__",
    "__mul__",
    "__or__",
    "__pow__",
    "__rshift__",
    "__sub__",
    "__truediv__",
    "__xor__",
])
if PY3K:
    methods.add("__div__")
MAGIC_METHODS = frozenset(methods)
del methods


def _build_magic_dispatcher(method):
    def inner(self, *args, **kwargs):
        return self.__dict__[method](*args, **kwargs)
    inner.__name__ = method
    return inner


class stub(object):
    _classes_cache = {}

    def __new__(cls, **kwargs):
        magic_methods_present = MAGIC_METHODS.intersection(kwargs)
        if magic_methods_present not in cls._classes_cache:
            attrs = dict(
                (method, _build_magic_dispatcher(method))
                for method in magic_methods_present
            )
            attrs["__module__"] = cls.__module__
            cls._classes_cache[magic_methods_present] = type("stub", (cls,), attrs)
        new_cls = cls._classes_cache[magic_methods_present]
        return super(stub, new_cls).__new__(new_cls, **kwargs)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
