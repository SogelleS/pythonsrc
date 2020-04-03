class Dog(object):

    def __init__(self,name):
        self.name=name

    @staticmethod
    def run():
        print('dog run!!!')

    # def run(self):
    #     print('run %s!!!'% self.name)

    # 静态方法使用不需要self参数
    # 和单独封装一个函数差不多只是调用方式不同
    # 与对象没有属性和方法上的交互
    # 类方法中访问实例的方法和属性会报错
    # 并且使用@staticmethod修饰
    # 可以直接使用类名调用



dog1=Dog('dog1')
Dog.run()
dog1.run()


