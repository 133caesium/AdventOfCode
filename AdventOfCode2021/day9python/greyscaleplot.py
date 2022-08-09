from matplotlib import pyplot as plt
import numpy as np

def plot_numpy_matrix(input_matrix):

    # Set the figure size
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # Random data points
    # data = np.random.rand(5, 5)

    # Plot the data using imshow with gray colormap
    plt.imshow(input_matrix, cmap='gray')

    # Display the plot
    plt.show()

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
