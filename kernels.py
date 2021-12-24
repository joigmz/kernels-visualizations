import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def Squared_exponential_kernel(X, Y, l):
    kernel = euclidean_distances(X, Y) ** 2
    kernel = kernel*(-1/(l**2))
    kernel = np.exp(kernel)
    return kernel

def Orstein_Uhlenbeck_kernel(X, Y, l):
    kernel = euclidean_distances(X, Y)
    kernel = kernel*(-1/(l**2))
    kernel = np.exp(kernel)
    return kernel

def Rational_quadratic_kernel(X, Y, l, sigma, alpha):
    kernel = euclidean_distances(X, Y) ** 2
    kernel = 1 + kernel/(2*alpha*l**2)
    kernel = sigma*kernel**(-alpha)
    return kernel

def Periodic_kernel(X, Y, sigma, p, l):
    kernel = np.pi*euclidean_distances(X, Y)*(1/p)
    kernel = -2*(np.sin(kernel)**2)*(1/l**2)
    kernel = (sigma**2)*np.exp(kernel)
    return kernel

def Polynomial_kernel(X, Y, sigmab, sigmav, mu, alpha):
    kernel = sigmab**2 + (sigmav**2)*(X-mu)@(Y-mu).T
    kernel = kernel**alpha
    return kernel