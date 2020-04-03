class MusicPlayer(object):

    have = None
    init_flag=False

    def __new__(cls, *args, **kwargs):


        if cls.have is None:
            cls.have = super().__new__(cls)
            return cls.have
        else:
            return cls.have

    def __init__(self):
        # print('初始化播放器')
        # 执行两次

        if MusicPlayer.init_flag is False:
            print('初始化')
            MusicPlayer.init_flag=True
        # 初始化两次



    pass


player1=MusicPlayer()

print(player1)

player2=MusicPlayer()

print(player2)