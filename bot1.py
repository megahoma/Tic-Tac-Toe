from random import randint
from src.bot import IBot


class Bot(IBot):
    def step(self, arena, symbol):
        for s in symbol:
            for n in range(3):
                if arena[n][0] == '_' and arena[n][1] == s and arena[n][2] == s:
                    return (n, 0)
                if arena[n][0] == s and arena[n][1] == '_' and arena[n][2] == s:
                    return (n, 1)
                if arena[n][0] == s and arena[n][1] == s and arena[n][2] == '_':
                    return (n, 2)       
                
                if arena[0][n] == '_' and arena[1][n] == s and arena[2][n] == s:
                    return (0, n)
                if arena[0][n] == s and arena[1][n] == '_' and arena[2][n] == s:
                    return (1, n)
                if arena[0][n] == s and arena[1][n] == s and arena[2][n] == '_':
                    return (2, n)
                
            if arena[0][0] == '_' and arena[1][1] == s and arena[2][2] == s:
                return (0, 0)
            if arena[0][0] == s and arena[1][1] == '_' and arena[2][2] == s:
                return (1, 1)
            if arena[0][0] == s and arena[1][1] == s and arena[2][2] == '_':
                return (2, 2)
                        
            if arena[2][0] == '_' and arena[1][1] == s and arena[0][2] == s:
                return (2, 0)
            if arena[2][0] == s and arena[1][1] == '_' and arena[0][2] == s:
                return (1, 1)
            if arena[2][0] == s and arena[1][1] == s and arena[0][2] == '_':
                return (0, 2)  

        while True:
            x, y = randint(0, 2), randint(0, 2)
            if arena[x][y] == '_':
                return (x, y)