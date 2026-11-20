import numpy as np
import timeit

# 1,000,000 smart meter current readings (Amperes) across a regional grid
rng = np.random.default_rng(202)
current_amps = rng.uniform(5.0, 120.0, 1_000_000)
line_resistance = 0.04  # Ohms

def loop_version():
    power_loss = []
    for amp in current_amps:
        power_loss.append((amp ** 2) * line_resistance)
    return power_loss

def vectorized_version():
    return (current_amps ** 2) * line_resistance

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("First 5 line power loss values (Watts):", np.round(result[:5], 2))
print(f"Standard Loop Execution Time: {loop_time:.4f} s")
print(f"Vectorized Execution Time: {vector_time:.4f} s")
print(f"Speed-up Factor: {loop_time / vector_time:.1f}x")