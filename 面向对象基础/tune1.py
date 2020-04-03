class Mytime(object):

    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__sec = s
        self.__code = h * 3600 + m * 60 + s
        # 从0,0,0开始

    def addsecond(self, sec):
        self.__code += sec

        print(self.__chengadd__())

    def addmin(self, minu):

        self.__code += minu * 60

        print(self.__chengadd__())

    def addhour(self, hour):
        self.__code += hour * 3600
        print(self.__chengadd__())

    def __chengadd__(self):

        while self.__code < 0:
            self.__code += 86400

        i = self.__code % 60
        j = int(self.__code / 60)  % 60      # 分钟
        k = int(self.__code / 3600) % 24     # 小时

        return (k,j,i)




time = Mytime(10,23,23)

time.addsecond(-2)
time.addhour(23)