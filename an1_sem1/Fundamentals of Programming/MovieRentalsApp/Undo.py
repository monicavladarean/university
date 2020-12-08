


'''class UndoController:
    def __init__(self):
        self.operations = []
        self.index = -1
        self.duringUndo = False

    def addOperation(self, operation):
        if self.duringUndo == True:
            return

        self.index += 1
        self.operations = self.operations[:self.index + 1]
        self.operations.append(operation)

    def undo(self):
        if self.index == -1:
            return False

        self.duringUndo = True
        self.operations[self.index].undo()
        self.duringUndo = False
        self.index -= 1
        return True

    def redo(self):
        if self.index >= len(self.operations) or self.index == -1:
            return False

        self.duringUndo = True
        self.index += 1
        self.operations[self.index].redo()
        self.duringUndo = False
        return True


class CascadedOperation:
    def __init__(self):
        self.operation = []

    def add(self, oper):
        self.operations.append(oper)

    def undo(self):
        for o in self.operation:
            o.undo()

    def redo(self):
        for o in self.operation:
            o.redo()


class Operation:
    def __init__(self, undoFunction, redoFunction):
        self.undoFunction = undoFunction
        self.redoFunction = redoFunction

    def undo(self):
        self.undoFunction.call()

    def redo(self):
        self.redoFunction.call()


class FunctionCall:
    def __init__(self, func, *params):
        self.func = func
        self.params = params

    def call(self):
        self.func(*self.params)
'''
