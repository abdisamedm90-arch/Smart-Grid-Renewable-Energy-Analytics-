# BIT 2118: Scientific Computing Project Portfolio

**Student Name:** [MOHAMED ABDISAMAD]  
**Admission Number:** [BSCCS/2025/39474]  
**Course Code & Title:** BIT2118 Scientific Computing  
**Institution:** Mount Kenya University  
**Domain Theme:** Smart Grid & Renewable Energy Analytics  

---

## Overview & Group Work Alignment

This repository contains the complete individual submission for **BIT2118 Scientific Computing**, covering all 19 required tasks (Tasks A through S / Tasks 02 through 20).

1. **Tasks A through D (Shared Group Mathematical Baseline):**  
   Follows the group's standardized numerical foundations—1D NumPy array processing, C-array vectorization speed-up benchmarking, floating-point cancellation stability, and 2D spatial matrix transformations—adapted to Smart Grid telemetry metrics.

2. **Tasks E through S (Individual Real-World Domain Application):**  
   Applies numerical linear algebra, root-finding, interpolation, curve fitting, numerical calculus, ordinary differential equations, constrained optimization, and Monte Carlo simulations specifically to **Smart Grid & Renewable Energy Analytics**.

---

## Repository File Structure

| Task | Topic / Mathematical Focus | Python Script File |
| :--- | :--- | :--- |
| **Task A** | NumPy Arrays & Vectorized Solar Calculations | `Task_02_solar_output_stats.py` |
| **Task B** | Array Speed-Up & Smart Meter Vectorization | `Task_03_smart_meter_vectorization.py` |
| **Task C** | Floating-Point Precision & Frequency Stability | `Task_04_grid_frequency_precision.py` |
| **Task D** | Wind Turbine Spatial Matrix Transformations | `Task_05_wind_turbine_matrices.py` |
| **Task E** | Linear Systems ($Ax = b$) | `Task_06_power_plant_linear_systems.py` |
| **Task F** | LU Decomposition & Substation Dispatch | `Task_07_substation_lu.py` |
| **Task G** | Iterative Solvers (Jacobi & Gauss-Seidel) | `Task_08_transmission_voltage_iterative.py` |
| **Task H** | Eigenvalues & Grid Hub Centrality | `Task_09_grid_hub_eigenvalues.py` |
| **Task I** | Root Finding (Bisection & Fixed-Point) | `Task_10_tariff_equilibrium_roots.py` |
| **Task J** | Root Finding (Newton-Raphson & Secant) | `Task_11_solar_farm_irr_newton.py` |
| **Task K** | Systems of Nonlinear Equations | `Task_12_inverter_nonlinear_system.py` |
| **Task L** | Interpolation (Cubic Splines) | `Task_13_solar_irradiance_interpolation.py` |
| **Task M** | Curve Fitting & EV Demand Forecasting | `Task_14_ev_charging_curve_fit.py` |
| **Task N** | Numerical Differentiation | `Task_15_battery_degradation_diff.py` |
| **Task O** | Numerical Integration (Simpson's Rule) | `Task_16_wind_energy_integration.py` |
| **Task P** | Ordinary Differential Equations (Euler Method) | `Task_17_capacitor_discharge_euler.py` |
| **Task Q** | Numerical ODE Solvers (`solve_ivp`) | `Task_18_reservoir_hydro_ode.py` |
| **Task R** | Constrained Optimization | `Task_19_energy_dispatch_optimization.py` |
| **Task S** | Monte Carlo Simulation & Blackout Risk | `Task_20_blackout_risk_monte_carlo.py` |

---

## Detailed Task Documentation

### Task A: NumPy Arrays and Basic Numerical Computation
* **Script:** `Task_02_solar_output_stats.py`
* **Scenario & Assumptions:** Recording 24 hourly solar generation outputs (kWh) and computing feed-in tariff revenue ($\text{Revenue} = 0.15 \times \text{kWh} + \$5.00$).
* **Interpretation:** Mean generation ($23.58\text{ kWh}$) and peak output ($80\text{ kWh}$) guide daily grid balancing and inverter sizing.

### Task B: Mathematical Functions and Vectorization
* **Script:** `Task_03_smart_meter_vectorization.py`
* **Scenario & Assumptions:** Computing resistive line losses ($I^2 R$) across $1,000,000$ smart meter current logs.
* **Interpretation:** NumPy C-level vectorization executes $>50\times$ faster than standard Python `for` loops.

### Task C: Floating-Point Arithmetic and Numerical Errors
* **Script:** `Task_04_grid_frequency_precision.py`
* **Scenario & Assumptions:** Evaluating micro-scale frequency drift perturbations ($10^{-4}$ down to $10^{-12}\text{ Hz}$).
* **Interpretation:** Demonstrates catastrophic cancellation in direct subtraction and confirms precision preservation via algebraic rationalization.

### Task D: Matrix Algebra and Matrix Operations
* **Script:** `Task_05_wind_turbine_matrices.py`
* **Scenario & Assumptions:** Re-aligning 4 wind turbine coordinates $[X, Y]$ using a $60^\circ$ prevailing-wind rotation and wake-spacing scaling matrix.
* **Interpretation:** Matrix multiplication updates all turbine coordinates simultaneously; a non-zero determinant ($1.26$) confirms invertibility.

### Task E: Solution of Systems of Linear Equations
* **Script:** `Task_06_power_plant_linear_systems.py`
* **Scenario & Assumptions:** Allocating Solar ($x$) and Wind ($y$) generation blocks to meet $31\text{ MWh}$ energy and $18$-unit inertia targets.
* **Interpretation:** `np.linalg.solve` yields exact block allocations ($x = 2$, $y = 5$) with zero residual error.

### Task F: Gaussian Elimination and LU Decomposition
* **Script:** `Task_07_substation_lu.py`
* **Scenario & Assumptions:** Dispatching generation across North, Central, and South substations across Morning, Afternoon Peak, and Night demand periods.
* **Interpretation:** Factoring matrix $A$ once (`lu_factor`) enables rapid repeated solves (`lu_solve`) across all three daily load periods.

### Task G: Iterative Methods for Linear Systems
* **Script:** `Task_08_transmission_voltage_iterative.py`
* **Scenario & Assumptions:** Solving steady-state bus voltages across a 5-node feeder between $230\text{ kV}$ sending and $218\text{ kV}$ receiving boundaries.
* **Interpretation:** Both Jacobi and Gauss-Seidel converge to exact bus voltages, with Gauss-Seidel reaching tolerance in fewer iterations.

### Task H: Eigenvalues and Eigenvectors
* **Script:** `Task_09_grid_hub_eigenvalues.py`
* **Scenario & Assumptions:** Identifying critical transmission hubs across 4 interconnected power grid nodes.
* **Interpretation:** The dominant eigenvector highlights the Main Grid Hub as the highest-centrality node requiring redundant protection.

### Task I: Root Finding: Bisection and Fixed-Point Methods
* **Script:** `Task_10_tariff_equilibrium_roots.py`
* **Scenario & Assumptions:** Finding the equilibrium battery storage level where charging balances nonlinear discharge ($f(E) = E - 30 - 12e^{-E/25}$).
* **Interpretation:** Bisection and fixed-point iteration converge to the exact equilibrium capacity ($\approx 32.89\text{ MWh}$).

### Task J: Root Finding: Newton-Raphson and Secant Methods
* **Script:** `Task_11_solar_farm_irr_newton.py`
* **Scenario & Assumptions:** Computing the Internal Rate of Return (IRR) for a \$1,500,000 utility solar installation over 4 operating years.
* **Interpretation:** Newton-Raphson finds the exact discount rate where Net Present Value equals zero.

### Task K: Polynomial and Nonlinear Equation Solving
* **Script:** `Task_12_inverter_nonlinear_system.py`
* **Scenario & Assumptions:** Determining active power ($P$) and reactive power ($Q$) operating points under a $5\text{ MVA}$ apparent power limit and voltage regulation curve.
* **Interpretation:** `scipy.optimize.root` solves the coupled nonlinear equations simultaneously.

### Task L: Interpolation
* **Script:** `Task_13_solar_irradiance_interpolation.py`
* **Scenario & Assumptions:** Estimating intermediate solar irradiance ($\text{W/m}^2$) at 11:00 AM between 2-hour pyranometer readings.
* **Interpretation:** Cubic Spline interpolation constructs a smooth, physically realistic solar irradiance curve.

### Task M: Curve Fitting and Approximation
* **Script:** `Task_14_ev_charging_curve_fit.py`
* **Scenario & Assumptions:** Forecasting Quarter 10 regional EV charging demand (MWh) from 7 historical quarters.
* **Interpretation:** Quadratic curve fitting (`curve_fit`) projects future EV load growth to guide substation upgrades.

### Task N: Numerical Differentiation
* **Script:** `Task_15_battery_degradation_diff.py`
* **Scenario & Assumptions:** Calculating the annual capacity degradation rate ($\text{MWh/yr}$) of a grid battery over 6 years.
* **Interpretation:** Central difference approximations track accelerating degradation to schedule cell replacement.

### Task O: Numerical Integration
* **Script:** `Task_16_wind_energy_integration.py`
* **Scenario & Assumptions:** Integrating wind farm power output ($\text{MW}$) over 12 hours to compute total generated energy ($\text{MWh}$).
* **Interpretation:** Simpson's rule integration accurately computes total cumulative energy yield.

### Task P: Ordinary Differential Equations - Euler Method
* **Script:** `Task_17_capacitor_discharge_euler.py`
* **Scenario & Assumptions:** Modeling grid capacitor bank voltage decay ($dV/dt = -k V$) from $400\text{ V}$ over 15 seconds.
* **Interpretation:** Step-by-step Euler integration tracks transient voltage decay for protective relay timing.

### Task Q: Numerical Solution of ODEs Using SciPy
* **Script:** `Task_18_reservoir_hydro_ode.py`
* **Scenario & Assumptions:** Simulating hydroelectric reservoir water head depletion ($dH/dt = -k H$) during a 12-hour peak discharge.
* **Interpretation:** SciPy's adaptive `solve_ivp` solver models hydraulic head drop to maintain minimum turbine pressure.

### Task R: Numerical Optimization
* **Script:** `Task_19_energy_dispatch_optimization.py`
* **Scenario & Assumptions:** Minimizing generation cost across Solar (\$50/unit) and Hydro (\$80/unit) blocks to satisfy a $300\text{ MWh}$ grid demand.
* **Interpretation:** `scipy.optimize.minimize` computes the lowest-cost generation mix that meets grid load requirements.

### Task S: Random Numbers and Monte Carlo Methods
* **Script:** `Task_20_blackout_risk_monte_carlo.py`
* **Scenario & Assumptions:** Running 100,000 Monte Carlo simulations of peak grid demand ($\mu = 420\text{ MW}$, $\sigma = 45\text{ MW}$) against a $500\text{ MW}$ capacity limit.
* **Interpretation:** Quantifies exact grid overload probability to inform reserve capacity procurement.

---

## Author Verification

* **Student:** [Friend's Full Name]
* **Admission No:** [Friend's Admission Number]
* **Course:** BIT2118 Scientific Computing
* **Submitted via:** Mount Kenya University VLMS Portal