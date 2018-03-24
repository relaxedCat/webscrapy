class Tired(object):

    def __init__(self, dev_weights=None, test_weights=None, operate_weights=None):
        self.dev_weights = 0.5 if dev_weights is None else dev_weights
        self.test_weights = 0.2 if test_weights is None else test_weights
        self.operate_weights = 0.3 if operate_weights is None else operate_weights