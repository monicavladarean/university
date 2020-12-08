import numpy as np

class NeuralNetwork:

    #VERY particular network with 2 layers (plus one for input)

    def __init__(self, x, y, hidden):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], hidden)
        self.weights2 = np.random.rand(hidden, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.loss = []

    def feedforward(self):
        # computes the output of the network for some input
        self.layer1 = self.sigmoid(np.dot(self.input,self.weights1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))

    #the backpropagation algorithm
    def backprop(self, l_rate):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) *self.sigmoid_derivative()))

        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y -self.output) *
                                                  self.sigmoid_derivative(),self.weights2.T) *self.sigmoid_derivative()))
        # update the weights with the derivative (slope) of the loss function

        self.weights1 += l_rate * d_weights1
        self.weights2 += l_rate * d_weights2
        self.loss.append(sum((self.y - self.output)**2)/497)

    #activation function:
    def sigmoid(self,x):
        return x


    #derivate of te activation function
    def sigmoid_derivative(self):
        return 1