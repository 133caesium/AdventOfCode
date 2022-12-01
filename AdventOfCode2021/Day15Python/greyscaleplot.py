from matplotlib import pyplot as plt
import numpy

count = 0

def plot_numpy_matrix(input_matrix, first):



    # Set the figure size
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # Random data points
    # data = np.random.rand(5, 5)

    # Plot the data using imshow with gray colormap
    plt.imshow(input_matrix, cmap='gray')

    if first==True:
        plt.show()
        # plt.pause(0.1)
        # plt.close()

    # Display the plot
    plt.draw()

def plot_3_numpy_matricies(inputmatrix1, inputmatrix2, inputmatrix3):
    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Vertically stacked subplots')
    ax1.imshow(inputmatrix1, cmap='gray')
    ax2.imshow(inputmatrix2, cmap='gray')
    ax3.imshow(inputmatrix3, cmap='jet')
    plt.show()

def plot_n_numpy_matricies(*inputmatricies):
    fig, axs = plt.subplots(1, len(inputmatricies))
    fig.suptitle('Vertically stacked subplots')
    plots = zip(axs,inputmatricies)
    for plot in plots:
        plot[0].imshow(plot[1], cmap='jet')
    plt.show()
#
# fig,ax = plt.subplots(1,1)
# image = numpy.array([[1,1,1], [2,2,2], [3,3,3]])
# im = ax.imshow(image)
#
# while True:
#     image = numpy.multiply(1.1, image)
#     im.set_data(image)
#     fig.canvas.draw_idle()
#     plt.pause(1)

import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y,c='red')
plt.xlim(0,10)
plt.ylim(0,10)

plt.draw()
for i in range(1000):
    if i % 10 ==0:
        x, y = [], []
    x.append(np.random.rand(1)*10)
    y.append(np.random.rand(1)*10)
    sc.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(1)

plt.waitforbuttonpress()