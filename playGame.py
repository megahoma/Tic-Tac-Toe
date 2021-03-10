from src.game import Game


if __name__ == "__main__":
    _map = [3, 3]
    
    from bot1 import Bot
    bot1 = Bot("AI-бот")
    from bot2 import Bot
    bot2 = Bot("Просто-бот")
    
    game = Game([bot1, bot2], _map)
    game.loop()