from Controller.controller import Controller
from Repository.repository import Repository

if __name__ == '__main__':

    repository = Repository()
    ctrl = Controller(repository)

    print(ctrl.compute({'humidity': 65, 'temperature': 17}));print()
    print(ctrl.compute({'humidity': 10, 'temperature': 17}));print()
    print(ctrl.compute({'humidity': 10, 'temperature': 30}));print()
    print(ctrl.compute({'humidity': 75, 'temperature': 20}));print()

