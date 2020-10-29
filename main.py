from durand_kerner import DK
import numpy as np

args = [87, 54, -13, 120, 14, 23, 51, -312, 35,
        43, 3, 213, 43, 1, 32, 98, 123, 90, 2, 1, 823]

ITERATIONS = 100


roots = DK(args, ITERATIONS)
