class FuzzyRule:
    #Define a conjunctive fuzzy rule; X and Y and ... => Z

    def __init__(self, inputs, out):
        self.output_variable = out
        self.inputs = inputs

    def evaluate(self, inputs):
        #Receives a dictionary of all the input values and returns the conjunction of their values
        #and = min ; or = max
        #returns a fuzzy value

        return [self.output_variable,
                min([inputs[desctiption_name][var_name] for desctiption_name, var_name in self.inputs.items()])]