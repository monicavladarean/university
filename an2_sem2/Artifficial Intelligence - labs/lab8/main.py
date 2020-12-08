from Repository.Repository import Repository
from Service.Controller import Controller
from Ui.Ui import Ui

repository=Repository()
ctrl=Controller(repository)
console=Ui(ctrl)
console.runApp()