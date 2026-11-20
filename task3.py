import numpy as np

# Micro-scale frequency perturbation steps (Hz)
x_values = [1e-4, 1e-8, 1e-12]

print("Evaluating Grid Frequency Stability Sensitivity:")
print("-" * 60)

for x in x_values:
    # Direct formulation (suffers from catastrophic cancellation)
    direct = (np.sqrt(1 + x) - 1) / x

    # Algebraically equivalent stable formulation
    stable = 1 / (np.sqrt(1 + x) + 1)

    abs_error = abs(direct - stable)
    print(f"x = {x:.0e} | Direct: {direct:.12f} | Stable: {stable:.12f} | Abs Error: {abs_error:.2e}")