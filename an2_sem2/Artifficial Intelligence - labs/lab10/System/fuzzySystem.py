class FuzzySystem:
    #Receives variable descriptions and rules and outputs the defuzzified result of the system

    def __init__(self, rules):
        self.in_descriptions = {}
        self.out_description = None
        self.rules = rules

    def add_description(self, name, description, out=False):
        if out:
            if self.out_description is None:
                self.out_description = description
        else:
            self.in_descriptions[name] = description

    def compute(self, inputs):
        #sugeno model

        fuzzy_vals = self._compute_descriptions(inputs)
        print(fuzzy_vals)

        rule_vals = self._compute_rules_fuzzy(fuzzy_vals)
        print(rule_vals)

        fuzzy_out_variables= [(list(description[0].values())[0], description[1]) for description in rule_vals]
        print(fuzzy_out_variables)

        weighted_total = 0
        weight_sum = 0
        for variable in fuzzy_out_variables:
            weight_sum += variable[1]
            weighted_total += self.out_description.defuzzify(*variable) * variable[1]

        self.file((weighted_total/weight_sum).__str__()+"\n")
        return weighted_total/weight_sum

    def _compute_descriptions(self, inputs):
        return {variable_name: self.in_descriptions[variable_name].fuzzify(inputs[variable_name]) for variable_name, val in inputs.items()}

    def _compute_rules_fuzzy(self, fuzzy_vals):
        #returns the fuzzy output of all rules

        return [rule.evaluate(fuzzy_vals) for rule in self.rules if rule.evaluate(fuzzy_vals)[1] != 0]

    def file(self,inputs):
        f = open("output.txt", "a")
        f.write(inputs)
        f.close()