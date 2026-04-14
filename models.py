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

from statsmodels.tsa.vector_ar.vecm import coint_johansen, VECM

def johansen_test(data):
    result = coint_johansen(data, det_order=0, k_ar_diff=1)

    print("\n=== JOHANSEN TEST ===")
    print("Eigenvalues:", result.eig)
    print("Trace statistic:", result.lr1)
    print("Critical values (90%, 95%, 99%):", result.cvt)

    return result

def run_vecm(data):
    model = VECM(data, k_ar_diff=1, coint_rank=1)
    res = model.fit()

    print("\n=== VECM SUMMARY ===")
    print(res.summary())

    return res
