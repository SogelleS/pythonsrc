class Game(object):

    high_score = 0

    @classmethod
    def show_high_score(cls):
        print('high score is %d' % cls.high_score)

    @staticmethod
    def put_help():
        print('help yourself')

    def __init__(self, name):
        self.name = name

    def game_start(self):
        print("%s's game is start" % self.name)
        self.__test()

    def __test(self):
        print('test')

Game.put_help()
print('high score:', Game.high_score)
game1 = Game('user1')



