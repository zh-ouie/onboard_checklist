import numpy as np
import matplotlib.pyplot as plt

def create_random_xy(n):
    """
    Creating a random 2D array with length n.
    
    Parameters
    ----------
    n : int
        The length of the array to be created.

    Returns
    -------
    xy : numpy.ndarray
        The 2D numpy array created.
    """
    xy = np.random.rand(2, n)
    return xy

def plot_xy(xy):
    """
    Plotting a 2D array in matplotlib

    Parameters
    ----------
    xy : numpy.ndarray
        The 2D numpy array created.

    Returns
    -------
    None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xy[0], xy[1], '.')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show()
    return

def main():
    xy = create_random_xy(10)
    plot_xy(xy)
    return


if __name__ == "__main__":
    main()