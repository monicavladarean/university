class FuzzyDescriptions:
    #Encapsulate a description of a fuzzy variable, with a set of functions for each fuzzy region

    def __init__(self):
        self.regions = {}
        self.inverse = {}

    def add_region(self, variable_name, membership_function, inverse=None):
        #Adds a region with a given membership function
        #optionally adds a inverse function for the Sugeno Fuzzy model (if x is A and y is B then z = f(x,y))

        self.regions[variable_name] = membership_function
        self.inverse[variable_name] = inverse

    def fuzzify(self, value):
        #return the fuzzified values for each region

        return {name: membership_function(value) for name, membership_function in self.regions.items()}

    def defuzzify(self, variable_name, value):
        return self.inverse[variable_name](value)