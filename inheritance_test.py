class Robot:

    def __init__(self, name):
        self.name = name;
        self.position =[0,0]
        print('My name is ', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:',self.position)

class RobotDog(Robot):

    def make_noise(self):
        print('Woof Woof!')

my_robot = RobotDog('Sunny')
my_robot.walk(10)
my_robot.make_noise()