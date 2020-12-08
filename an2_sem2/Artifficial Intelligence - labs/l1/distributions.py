import numpy as np
import matplotlib.pyplot as plt

def normalDistribbution(n):
    std=1
    mean=0
    normal_array=np.random.normal(0,1,n) #mean, std deviation, "shape" of the array
    #plt.plot(normal_array)
    #plt.show()

    count, bins, ignored = plt.hist(normal_array, 30, density=True)
    plt.plot(bins, 1 / (std * np.sqrt(2 * np.pi)) *np.exp(- (bins - mean) ** 2 / (2 * std ** 2)), linewidth = 2, color = 'r')
    plt.show()

def uniformDistribution(n):
    uniformArray=np.random.uniform(0,n,n) #lower bound, upper bound, "shape" of the array(nr of elems)

    #plt.plot(uniformArray)
    #plt.show()

    count, bins, ignored = plt.hist(uniformArray, 15, density=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()

def menu():
    print("Distributions:")
    print("1. Uniform Distribution")
    print("2. Normal Distribution")
    distribution=input("Choose a distribution:")
    interval=input("Enter the upper bound of the interval of numbers: ")
    if distribution=="1":
        uniformDistribution(int(interval))
    elif distribution=="2":
        normalDistribbution(int(interval))

menu()

