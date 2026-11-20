import numpy as np

# 24 hourly solar energy generation records (kWh) over 1 day
hourly_kwh = np.array([
    0, 0, 0, 0, 0, 2, 12, 28,
    45, 62, 74, 80, 78, 70, 55, 38,
    18, 4, 0, 0, 0, 0, 0, 0
])

# Statistical metrics
mean_kwh = np.mean(hourly_kwh)
min_kwh = np.min(hourly_kwh)
max_kwh = np.max(hourly_kwh)

# Vectorized feed-in tariff revenue ($0.15/kWh + $5.00 grid availability credit)
hourly_revenue = 0.15 * hourly_kwh + 5.0

print(f"Daily Mean Generation: {mean_kwh:.2f} kWh")
print(f"Minimum Hourly Generation: {min_kwh} kWh")
print(f"Peak Hourly Generation: {max_kwh} kWh")
print("Midday hourly revenues (Hours 10-15, $):", np.round(hourly_revenue[10:16], 2))