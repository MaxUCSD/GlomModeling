import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Parameters
t_end = 20
Input_on = [3,6, 7, 8]
tau_c = 2  # Recovery time constant

# Create input signal
I_values = np.zeros(t_end)
I_values[Input_on] = 1  # Turn on at specified times

# Create time points for interpolation
t_points = np.arange(t_end)
I = interp1d(t_points, I_values, kind='nearest', 
            bounds_error=False, fill_value=0)

# Define the ODE system
def concentration_ode(t, y):
    c = y[0]  # Current concentration
    dc_dt = (1 - c)/tau_c - I(t) * c
    return [dc_dt]

# Initial condition: start at steady state (c = 1)
y0 = [1.0]

# Time span and evaluation points
t_span = (0, t_end-1)
t_eval = np.linspace(0, t_end-1, 1000)

# Solve the ODE
result = solve_ivp(concentration_ode, t_span=t_span, y0=y0, 
                   t_eval=t_eval, dense_output=True)

# Create plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Plot input
ax1.plot(t_eval, [I(t) for t in t_eval], 'k-', linewidth=2, label='Input χ(t)')
ax1.set_ylabel('Input', fontsize=12)
ax1.set_title('Input Signal', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.set_ylim(-0.1, 1.2)

# Plot concentration
ax2.plot(result.t, result.y[0], 'b-', linewidth=2, label=f'Concentration c(t), τc={tau_c}')
ax2.axhline(y=1, color='r', linestyle='--', alpha=0.5, label='Steady state (no input)')
ax2.set_xlabel('Time', fontsize=12)
ax2.set_ylabel('Concentration c(t)', fontsize=12)
ax2.set_title('Receptor Concentration Dynamics', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11)

plt.tight_layout()
plt.show()

# Print some diagnostics
print(f"Initial concentration: {result.y[0][0]:.3f}")
print(f"Final concentration: {result.y[0][-1]:.3f}")
print(f"Minimum concentration: {np.min(result.y[0]):.3f}")
print(f"Recovery time constant τc: {tau_c}")
print(f"Steady state with constant input: {1 - tau_c:.3f}")