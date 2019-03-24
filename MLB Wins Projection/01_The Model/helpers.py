from scipy.stats import kurtosis
from scipy.stats import skew
import numpy as np


def test_skew(arry):
    if skew(arry) != 0 :
        return skew(arry)



