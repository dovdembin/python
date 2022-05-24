# https://waterprogramming.wordpress.com/2022/02/24/root-finding-algorithm-basics/
import numpy as np

def Fluxes(x):
    # Set parameters
    b = 0.42
    q = 2
    flux = (x**q) / (1 + x**q) - b*x
    return flux

def Bisect(Function, range_start, range_end, maxNFE=1000, tolerance=10 ** -6):
    A = range_start
    B = range_end

    # Check that range bounds have alternate signs
    if np.sign(Function(A)) == np.sign(Function(B)):
        print("Start and end values for the range must correspond to function values of different sign.")

    RootRange = [A, B]

    # Perform Bisection method until tolerance is achieved
    NFE = 0
    spread = RootRange[1] - RootRange[0]

    while (spread > tolerance) and (NFE < maxNFE):

        MidPoint = (RootRange[1] + RootRange[0]) / 2

        if Fluxes(MidPoint == 0):
            Root = MidPoint
            NFE += 1
            return Root, NFE

        elif np.sign(Function(MidPoint)) != np.sign(Function(RootRange[1])):
            RootRange[0] = MidPoint

        else:
            RootRange[1] = MidPoint

        NFE += 1
        spread = RootRange[1] - RootRange[0]

    Root = (RootRange[1] + RootRange[0]) / 2

    return Root, NFE