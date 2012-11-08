from pretend import stub


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

    def test_add(self):
        x = stub(__add__=lambda y: 2 + y)
        assert x + 4 == 6
