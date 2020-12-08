from Repository.Repository import Repository
from Service.Controller import Controller
from Ui.Ui import Ui

repository=Repository()
controller=Controller(repository)
ui=Ui(controller)
ui.gradientDescent()