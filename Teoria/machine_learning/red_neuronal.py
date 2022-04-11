from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


def plot_data(x, y, x_label, y_label, mark):
    plt.figure(figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
    plt.plot(x, y, mark)
    plt.xlabel = x_label
    plt.ylabel = y_label
    plt.show()


def plot_loss(x, x_label, y_label):
    plt.figure(figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k')
    plt.plot(x)
    plt.xlabel = x_label
    plt.ylabel = y_label
    plt.show()


model = keras.Sequential()
model.add(keras.layers.Dense(units=40, input_dim=1, activation='relu'))
model.add(keras.layers.Dense(units=20, activation='relu'))
model.add(keras.layers.Dense(units=10, activation='relu'))
model.add(keras.layers.Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

'''Al agregar valores negativos mejora la calidad de la data
np.random.random() crea valores entre 0 y 1
nrow = 25k ncol = 1'''

xs = -50 + np.random.random((25000, 1)) * 100
ys = xs ** 2

hist = model.fit(xs, ys, epochs=15)

plot_data(xs, ys, 'X', 'Y', 'bo')
plot_loss(hist.history['loss'], 'epoch', 'loss')
