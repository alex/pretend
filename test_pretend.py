from __future__ import print_function

import operator

import pytest

from pretend import stub, PY3K


class TestPretend(object):
    def test_attribute(self):
        x = stub(attr=3)
        assert hasattr(x, "attr")
        assert x.attr == 3

    def test_function(self):
        x = stub(meth=lambda x, y: x + y)
        assert x.meth(3, 4) == 7

    def test_iterable(self):
        x = stub(__iter__=lambda: iter([1, 2, 3]))
        iterator = iter(x)
        assert next(iterator) == 1

    @pytest.mark.parametrize(("func", "op"), [
        (operator.lt, "__lt__"),
        (operator.le, "__le__"),
        (operator.eq, "__eq__"),
        (operator.ne, "__ne__"),
        (operator.gt, "__gt__"),
        (operator.ge, "__ge__"),

        (operator.add, "__add__"),
        (operator.and_, "__and__"),
        (divmod, "__divmod__"),
        (operator.floordiv, "__floordiv__"),
        (operator.lshift, "__lshift__"),
        (operator.mod, "__mod__"),
        (operator.mul, "__mul__"),
        (operator.or_, "__or__"),
        (operator.pow, "__pow__"),
        (operator.rshift, "__rshift__"),
        (operator.sub, "__sub__"),
        (operator.truediv, "__truediv__"),
        (operator.xor, "__xor__"),
    ])
    def test_special_binops(self, func, op):
        x = stub(**{
            op: lambda y: func(2, y)
        })
        assert func(x, 4) == func(2, 4)
        assert func(x, 2) == func(2, 2)

    @pytest.mark.skipif(lambda self: PY3K)
    def test_div(self):
        x = stub(
            __div__=lambda y: 4
        )
        assert x / 3 == 4

    def test_missing_op_error(self):
        x = stub()
        with pytest.raises(TypeError):
            x + 2
