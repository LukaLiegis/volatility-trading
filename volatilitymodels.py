import numpy as np
import pandas as pd

class VolModel:
    def __init__(self):
        self.window = 30
        self.trading_periods = 252
        self.clean = True

    def close_to_close(self):
        """
        Calculates the close-to-close volatility estimator.
        :return:
        """

    def parkinson(self, data):
        """
        Calculates the parkinson volatility estimator.
        :return:
        """
        const = 4 * np.log(2)

        rs = (np.log(data["high"] / data["low"]) ** 2.0).rolling(window=self.window)

        result = (rs / (const * self.trading_periods)) ** 0.5

        if self.clean:
            return result.dropna()
        else:
            return result

    def garman_klass(self):
        """
        Calculates the Garman Klass volatility estimator.
        :return:
        """