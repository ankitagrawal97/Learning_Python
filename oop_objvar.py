class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(initialzing {})".format(self.name))

        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        print("Greetings, my master calls me {}".format(self.name))

    def how_many():
        print("we have {:d} robots.".format(Robot.population))


droid1 = Robot("R2 D2")
droid1.say_hi()

droid2 = Robot("C -3PO")
droid2.say_hi()


Robot.how_many()

print("Robots do some work")

Robot.die()

Robot.how_many()
