class Mytime(object):

    def __init__(self, h, m, s):
        self.__hour=h
        self.__minute=m
        self.__sec=s

    def addsecond(self, sec):
        self.secaddtomin(sec)
        self.minaddtohour(0)
        self.houraddtoday(0)

    def addmin(self,min):
        self.secaddtomin(0)
        self.minaddtohour(min)
        self.houraddtoday(0)

    def addhour(self,hour):
        self.secaddtomin(0)
        self.minaddtohour(0)
        self.houraddtoday(hour)



    def secaddtomin(self,sec):
        if self.__sec + sec > 60:
            i = int((self.__sec + sec) / 60)
            self.__tempmin = self.__minute
            self.__minute += i
            self.__sec = self.__sec + (sec % 60)
        else:
            self.__sec += sec
            self.__tempmin = self.__minute




    def minaddtohour(self, min):
        if self.__minute + min > 60:
            i = int((self.__minute + min) / 60)
            self.__temphour = self.__hour
            self.__hour += i
            self.__minute = (self.__minute-self.__tempmin) % 60 + (self.__tempmin)

        else:
            self.__minute += min
            self.__temphour = self.__hour


    def houraddtoday(self, hour):
        if self.__hour + hour > 24:
            i = (((self.__hour-self.__temphour) + hour) % 24)

            if i + self.__temphour >24:
                i = (i + self.__temphour) % 24
                self.__hour = i + self.__temphour
            else:
                self.__hour = self.__temphour + i
        else:
            self.__hour += hour

    def puttime(self):

        print('hour[%d]min[%d]sec[%d]' % (self.__hour,self.__minute,self.__sec))




test1 = Mytime(12,23,14)
test1.addhour(49)
test1.puttime()


