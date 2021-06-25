import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    import numpy as np

    # a = np.array([[1, 2, 3], [4, 5, 6]])
    a = np.arange(24)
    b=a.reshape(2,4,3)

    print(a)
    print(b)
    print(a.ndim)
    print(b.ndim)
