from System.fuzzyDescriptions import FuzzyDescriptions
from System.fuzzyRule import FuzzyRule

class Repository:
    def __init__(self):
        self.temperature=FuzzyDescriptions()
        self.humidity = FuzzyDescriptions()
        self.time = FuzzyDescriptions()
        self.rules = []
        self.populate_repository()

    def populate_repository(self):

        file = open('C:\\Users\\Monica\\OneDrive\\Desktop\\AI\\lab10\\input.txt', 'r')
        Lines = file.readlines()
        ok1=False;ok2=False;ok3=False;ok4=False
        for line in Lines:
            if("1) rules:" in line):
                ok1=True
                continue
            if("2) temperatureRegion:" in line):
                ok1=False;ok2=True
                continue
            if ("3) humidityRegion:" in line):
                ok1=False;ok2=False;ok3=True
                continue
            if ("4) timeRegion:" in line):
                ok1=False;ok2=False;ok3=False;ok4=True
                continue
            if(ok1):
                rule = line.strip().split(";")
                self.rules.append(FuzzyRule(eval(rule[0]), eval(rule[1])))
            if(ok2):
                temperature_region = line.strip().split(";")
                self.temperature.add_region(temperature_region[0], eval(temperature_region[1]))
            if(ok3):
                humidity_region = line.strip().split(";")
                self.humidity.add_region(humidity_region[0], eval(humidity_region[1]))
            if(ok4):
                time_region = line.strip().split(";")
                self.time.add_region(time_region[0], eval(time_region[1]),eval(time_region[2]))

    def trap_region(self, a, b, c, d):
        #returns a higher order function for a trapezoidal fuzzy region
        return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))

    def tri_region(self,a, b, c):
        #returns a higher order function for a triangular fuzzy region
        return self.trap_region(a, b, b, c)

    def inverse_line(self,a, b):
        return lambda val: val * (b - a) + a

    def inverse_tri(self,a, b, c):
        return lambda val: (self.inverse_line(a, b)(val) + self.inverse_line(c, b)(val)) / 2

    def get_temperature(self):
        return self.temperature

    def get_rules(self):
        return self.rules

    def get_time(self):
        return self.time

    def get_humidity(self):
        return self.humidity