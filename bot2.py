from random import randint
from src.bot import IBot


class Bot(IBot):
    def step(self, arena, symbol):
        while True:
            x, y = randint(0, 2), randint(0, 2)
            return (x, y)