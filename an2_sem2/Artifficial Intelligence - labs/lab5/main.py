from Service.Controller import Controller
import matplotlib.pyplot as plt

def validationTest(n, numberOfAnts, alpha, beta, q0, rho):
    std = []
    mean = []  # avg
    # we apply 30 runs:
    for i in range(30):
        # keep the fitness of every state in every pop in a run
        aco = Controller(n, 40, 1000, numberOfAnts, alpha, beta, q0, rho)
        std1, mean1 = aco.validateTest()
        std.append(std1)
        mean.append(mean1)
        print(i)
    std, = plt.plot(std, color='m', label='Standard Deviation')
    mean, = plt.plot(mean, color='y', label='Average')
    plt.legend(handles=[std, mean])
    plt.show()

n = int(input("n: "))
populationSize = int(input("populationSize : "))
trials = int(input("trials: "))
numberOfAnts = int(input("numberOfAnts: "))
alpha = float(input("alpha: "))
beta = float(input("beta: "))
q0 = float(input("q0: "))
rho = float(input("rho: "))

ctrl= Controller(n, populationSize, trials, numberOfAnts, alpha, beta, q0, rho)
ctrl.mainForACO()
#validationTest(n,numberOfAnts,alpha,beta,q0,rho)

