from abc import ABC, abstractmethod


class Estimator(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass


class LeastSquaresLinearEstimator(Estimator):

    def fit(self, X, y):
        pass
