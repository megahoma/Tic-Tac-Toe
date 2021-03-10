class IBot():
    def __init__(self, name='Default name'):
        self.name = name
    def step(self, arena, symbol):
        
        raise NotImplementedError()