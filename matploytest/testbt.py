import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(-1, 1, 100)
    y1 = 2 * x + 1
    y2 = x ** 2

    # plt.figure()
    plt.plot(x, y1)
    # plt.figure(figsize=(8,5))
    plt.plot(x, y2)

    plt.show()