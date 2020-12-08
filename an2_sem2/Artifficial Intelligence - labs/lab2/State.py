class State():
    def __init__(self, vals):
        self._values = vals

    def get_values(self):
        return self._values

    def set_values(self, v):
        self._values = v

    def add_to_table(self, i, j):
        self._values[i - 1][j - 1] = 1

    def __str__(self):
        s = ""
        for l in self._values:
            s += str(l)
            s += "\n"
        return s

    def __eq__(self, otherr):

        other = otherr.get_values()

        for i in range(len(self._values)):
            for j in range(len(self._values)):
                if self._values[i][j] != other[i][j]:
                    return False
        return True
