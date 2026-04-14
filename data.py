import yfinance as yf
import numpy as np
import pandas as pd

def get_data():
    data = yf.download(["^GSPC", "MXN=X"], start="2015-01-01")["Close"]

    returns = np.log(data / data.shift(1)).dropna()
    returns.columns = ["SP500", "USD_MXN"]

    return returns