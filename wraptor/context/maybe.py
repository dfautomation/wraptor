class maybe(object):
    def __init__(self, predicate):
        self.predicate = predicate

    def __enter__(self):
        return self.predicate()

    def __exit__(self, exc_type, exc_value, traceback):
        pass
