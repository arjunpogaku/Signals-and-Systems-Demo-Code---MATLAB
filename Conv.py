import numpy as np

def convolve(x, h):
    # Length of the output signal is (len(x) + len(h) - 1)
    y_length = len(x) + len(h) - 1
    y = np.zeros(y_length)  # Initialize the output array with zeros

    # Perform the convolution using the summation formula
    for n in range(y_length):
        y[n] = sum(x[k] * h[n - k] for k in range(len(x)) if 0 <= n - k < len(h))

    return y

# Example usage:
x = [1, 2, 3]  # Input signal
h = [0, 1, 0.5]  # Impulse response

y = convolve(x, h)
print("The convolution result is:", y)
