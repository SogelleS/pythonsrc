class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 内置的静态方法

        print('get a player')
        re = super().__new__(cls)
        print(re)

        return re


    def __init__(self):
        print('player is ready')


player = MusicPlayer()
print(player)

