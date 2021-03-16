class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big=big
        self.medium=medium
        self.small=small
        
        

    def addCar(self, carType):
        d = {
            1:'big',
            2:'medium',
            3:'small'
        }
        if d[carType]=='big' and self.big:
            self.big-=1
            return True
        if d[carType]=='medium' and self.medium:
            self.medium-=1
            return True
        if d[carType]=='small' and self.small:
            self.small-=1
            return True
        return False     