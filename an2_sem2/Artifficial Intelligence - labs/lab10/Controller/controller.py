from System.fuzzySystem import FuzzySystem

class Controller:
    def __init__(self,repository):
        self.system = FuzzySystem(repository.rules)
        self.system.add_description('temperature', repository.temperature)
        self.system.add_description('humidity', repository.humidity)
        self.system.add_description('time', repository.time, out=True)

    def compute(self, inputs):
        self.file(inputs)
        return "For humidity: " + str(inputs['humidity']) + \
               " and temperature: " + str(inputs['temperature']) + \
               " => operating time: " + str(self.system.compute(inputs))

    def file(self,inputs):
        f = open("output.txt", "a")
        f.write("For humidity: " + str(inputs['humidity']) + \
                " and temperature: " + str(inputs['temperature']) + " => operating time: ")
        f.close()