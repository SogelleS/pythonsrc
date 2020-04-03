class Gun:
    def __init__(self,model='ak-47',bullet=0):
        self.model=model
        self.bullet=bullet

    def addbullet(self,num):

        if (self.bullet>30 or num>30):
            print('cant add bullet max is 30')
        else:
            print('正在上弹...')
            self.bullet+=num

    def shoot(self):
        if self.bullet<=0:
            print('out of ammo cant shoot')
        else:
            self.bullet-=1
            print('nice shoot')
            print('子弹还剩%d'%self.bullet)


class Sold:

    def __init__(self,name,gun=None):
        #新兵没有枪
        self.name=name
        self.gun=gun

    def fire(self):
        # if self.gun==None:
        if self.gun is None:
            # 对none比较时建议使用is运算符
            print('no gun')
        else:
            if self.gun.bullet<=0:
                self.gun.addbullet(30)
            print('检测完毕准备射击')
            self.gun.shoot()


akgun=Gun('ak47',30)

xusanduo=Sold('xusanduo',akgun)
xusanduo.fire()


