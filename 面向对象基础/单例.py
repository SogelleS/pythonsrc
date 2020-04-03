class MusicPlayer(object):

    have = None
    # 记录对象的引用

    def __new__(cls, *args, **kwargs):

        # 判断 have 是不是空对象
        # 如果是空对象，就调用父方法分配空间
        # else 返回类属性保存的对象

        if cls.have is None:
            cls.have = super().__new__(cls)
            return cls.have
        else:
            return cls.have



    pass


player1=MusicPlayer()

print(player1)

player2=MusicPlayer()

print(player2)