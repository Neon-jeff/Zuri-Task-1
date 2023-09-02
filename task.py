# Python Solution for the project

class myModule():
    # setting the init function to accept the parameters

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def timeSimulator(self,time):
        return time

    def get_distance(self):
        # assuming the distnce is the average of the points
        distance= float((self.a  + self.b)/2)

    def checkPenetrable(self):
        if self.timeSimulator()>60:
            return False
        else:
            return True

