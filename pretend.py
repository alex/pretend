class stub(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __iter__(self):
        return self.__dict__["__iter__"]()

