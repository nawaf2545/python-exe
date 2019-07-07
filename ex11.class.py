class Car:
    def __init__(self,color,name,model):
        self.color = color
        self.name = name
        self.model = model
    def goBack(self):
        print(self.name,"is going back")
    def goForward(self):
        print(self.name,"is going forward")
if __name__ == '__main__':
    car1 =Car("RED","KIA",2018)
    Car2 =Car("Green","BMW",2015)

    car1.goBack()
    Car2.goForward()