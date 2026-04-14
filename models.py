from statsmodels.tsa.api import VAR
from arch import arch_model

# VAR
def run_var(data):
    model = VAR(data)
    results = model.fit(maxlags=5, ic='aic')
    print(results.summary())
    return results


# GARCH
def run_garch(series):
    model = arch_model(series, vol='Garch', p=1, q=1)
    res = model.fit(disp="off")
    print(res.summary())
    return res


# EGARCH
def run_egarch(series):
    model = arch_model(series, vol='EGarch', p=1, q=1)
    res = model.fit(disp="off")
    print(res.summary())
    return res