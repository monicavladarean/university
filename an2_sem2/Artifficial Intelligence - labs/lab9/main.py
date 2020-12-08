import tensorflow as tf
from keras.models import Sequential
import matplotlib.pyplot as plt
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

(trainSet, labelsTrainSet), (testSet, labelsTestSet) = tf.keras.datasets.mnist.load_data()

# Reshaping the array to 4-dims so that it can work with the Keras API
trainSet = trainSet.reshape(trainSet.shape[0], 28, 28, 1) #60,000 images images
testSet = testSet.reshape(testSet.shape[0], 28, 28, 1) #10,000 images images
input_shape = (28, 28, 1)
# Making sure that the values are float so that we can get decimal points after division
trainSet = trainSet.astype('float32')
testSet = testSet.astype('float32')
# Normalizing the RGB codes by dividing it to the max RGB value.
trainSet /= 255
testSet /= 255
print('trainingSet shape:', trainSet.shape)
print('Number of images in training: ', trainSet.shape[0])
print('Number of images in testing: ', testSet.shape[0])

# Creating a Sequential Model and adding the layers
model = Sequential()
model.add(Conv2D(8, kernel_size=(3,3), input_shape=input_shape,use_bias=False)) #params:nr of filters, dimension of kernel(one filter), image shape, noBias
model.add(MaxPooling2D(pool_size=2)) #apply max filter to reduce the dimension
model.add(Flatten()) # flattens the 2D arrays
model.add(Dense(10,activation=tf.nn.softmax)) #matrix vector multiplication; softmax converts the real vector to a vector of categorical probabilities

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) # adam: stochastic gradient descent method

print("Model compiled. Starting training")
model.fit(x=trainSet, y=labelsTrainSet, epochs=1)

print("Training done. Starting testing")
results=model.evaluate(testSet, labelsTestSet)
print('[loss, accuracy]: ',results)
image_index = 4444
plt.imshow(testSet[image_index].reshape(28, 28),cmap='Greys')
plt.show()
pred = model.predict(testSet[image_index].reshape(1, 28, 28, 1))
print(pred.argmax())
