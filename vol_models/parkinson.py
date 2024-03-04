import math
import numpy as np

def parkinson(data, window = 30, trading_periods = 252, clean = True):
    rs = (1.0 / (4.0 * math.log(2.0))) * ((data["High"] / data["Low"]).apply(np.log)) ** 2.0
    def f(v):
        return (trading_periods * v.mean()) ** 0.5

    result = rs.rolling(window=window, center=False).apply(func=f)

    if clean:
        return result.dropna()
    else:
        return result