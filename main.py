from data import get_data
from models import run_var, run_garch, run_egarch

data = get_data()

print("\n--- DATOS ---")
print(data.head())

# VAR
print("\n--- VAR ---")
run_var(data)

# GARCH (SP500)
print("\n--- GARCH ---")
run_garch(data["SP500"])

# EGARCH
print("\n--- EGARCH ---")
run_egarch(data["SP500"])
import matplotlib.pyplot as plt

data["SP500"].plot(title="Rendimientos S&P500")
plt.show()

data["USD_MXN"].plot(title="Rendimientos USD/MXN")
plt.show()
from models import run_var, run_garch, run_egarch, johansen_test, run_vecm
print("\n--- JOHANSEN TEST ---")
johansen_test(data)

print("\n--- VECM ---")
run_vecm(data)