from os import system
from time import sleep
from src.timeout import timeout


class Game:
    def __init__(self, _bot, _map):
        self.bots = _bot
        self._map = _map
        self.setup = True
        self.symbol = ['X', 'O']
        self.arena = [['_' for j in range(self._map[0])] for i in range(self._map[1])]
    
    def check(self):
        def check_l(a1, a2, a3, symbol):
            if a1 == symbol and a2 == symbol and a3 == symbol:
                if 'X' == symbol:
                    Game.winner(self, self.bots[0].name)
                else:
                    Game.winner(self, self.bots[1].name)

        if self.setup == False:
            return
        
        for s in self.symbol:    
            for i in range(3):
                check_l(self.arena[i][0], self.arena[i][1], self.arena[i][2], s)
                check_l(self.arena[0][i], self.arena[1][i], self.arena[2][i], s)
            check_l(self.arena[0][0], self.arena[1][1], self.arena[2][2], s)
            check_l(self.arena[2][0], self.arena[1][1], self.arena[0][2], s)
        
        if max([i.count('_') for i in self.arena ]) == 0 and self.setup == True:
            self.setup = False
            print('Игра окончена, никто из ботов не смог выйграть')

    def loop(self):
        while self.setup:
            for i in range(len(self.bots)):
                if self.setup == False:
                    break
                    
                @timeout(1)
                def s(n):
                    try:
                        return self.bots[i].step(self.arena, self.symbol)
                    except TimeoutError:
                        self.setup = False
                        print(f"Игра окончена, бот {n} проиграл!, превышен временной порог в 1 секунду")
                        return None
                _step = s(i)
                if _step == None:
                    break
                
                if self.arena[_step[0]][_step[1]] == '_':
                    self.arena[_step[0]][_step[1]] = self.symbol[i]
                else:
                    Game.over(self, self.bots[i].name)
                
                Game.visible(self, self.bots[i].name, self.symbol[i])
                Game.check(self)            
        
    def visible(self, n_bots, n_symbol):
        if self.setup == False:
            return
        system('cls||clear')
        print(f"Ход бота {n_bots} ('{n_symbol}')")
        for i in self.arena:
            print(''.join(i))
        sleep(1)
        
    def over(self, n_bots):
        self.setup = False
        print(f"Игра окончена, бот {n_bots} проиграл!")

    def winner(self, n_bots):
        self.setup = False
        print(f"Игра окончена, бот {n_bots} выйграл!")
