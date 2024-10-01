from abc import ABC, abstractmethod

import numpy as np
import pandas as pd


class Summator(ABC):
    def __init__(self, array):
        self.sum = self.summate(array)

    @abstractmethod
    def summate(self, array):
        pass


class NumpySummator(Summator):
    def summate(self, array):
        return np.sum(array)


class PandasSummator(Summator):
    def summate(self, array):
        return array.sum()
