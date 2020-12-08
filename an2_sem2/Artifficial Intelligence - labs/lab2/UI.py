from Controller import *

class UI:
    def __init__(self, ctrl):
        self._controller = ctrl

    def mainMenu(self):
        print("What method do you want?")
        print("1.DFS?")
        print("2.Greedy")
        n=int(input("Your choice: "))
        if n==1:
            node = self._controller.dfs(self._controller.get_initial())
        elif n==2:node = self._controller.gbfs(self._controller.get_initial())
        print(node)
