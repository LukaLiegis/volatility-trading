import numpy as np
import pandas as pd


class VolModel:
    def __init__(self):
        self.window = 30
        self.trading_periods = 252
        self.clean = True
        print("Initializing VolModel")

    def close_to_close(self):
        """
        Calculates the close-to-close volatility estimator.
        :return:
        """

    def parkinson(self, data: pd.DataFrame):
        """
        Calculates the parkinson volatility estimator.
        :return:
        """
        const = 4 * np.log(2)

        rs = (np.log(data["High"] / data["Low"]) ** 2.0).rolling(window=self.window).sum()

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
