import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import plotly.graph_objects as go
import plotly.offline as pyo

# Parameters
t_end = 50
Input_on = [3, 12,13,14]
tau_c = [0.5, 0.6, 10]
tau_s = [0.5, 0.6, 5] 
tau_r = [0.5, 0.6, 1]
# Create input signal
I_values = np.zeros(t_end)
I_values[Input_on] = 1  # Turn on at specified times

# Create time points for interpolation
t_points = np.arange(t_end)
I = interp1d(t_points, I_values, kind='nearest', 
            bounds_error=False, fill_value=0)

def single_glom(t, y, tau_c, tau_s, tau_r):
    c,s,r = y  
    dc_dt = (1 - c)/tau_c - I(t) * c
    ds_dt = -s/tau_s + c * I(t)
    dr_dt = -r/tau_r + s

    return [dc_dt, ds_dt, dr_dt]


t_span = (0, t_end-1)
y0 = (1, 0, 0)
t_eval = np.linspace(0, t_end-1, 10000)
results = {}
    # Solve the ODE with current tau_c
for i, (tc, ts, tr) in enumerate(zip(tau_c, tau_s, tau_r)):
    print(i)
    results[f'glom{i}'] = solve_ivp(single_glom, t_span, y0, t_eval=t_eval, 
                       args=(tc, ts, tr), method='RK45')
    results[f'glom{i}']['tau_c'] = tc
    results[f'glom{i}']['tau_s'] = ts
    results[f'glom{i}']['tau_r'] = tr


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 10))
# Plot input

ax1.plot(t_eval, [I(t) for t in t_eval], 'k-', linewidth=2, label='Input χ(t)')
ax1.set_ylabel('Input', fontsize=12)
ax1.set_title('Input Signal', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.set_ylim(-0.1, 1.2)



for i in range(len(results)):
    result = results[f'glom{i}']
    print(result)
    ax2.plot(t_eval, result.y[0], linewidth=2, label=f'c {i} ({result["tau_c"]})')
    ax2.set_ylabel('c', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=11)

    ax3.plot(t_eval, result.y[1], linewidth=2, label=f's {i} ({result["tau_s"]})')
    ax3.set_ylabel('s', fontsize=12)
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=11)

    ax4.plot(t_eval, result.y[2], linewidth=2, label=f'r {i} ({result["tau_r"]})')
    ax4.set_ylabel('r', fontsize=12)
    ax4.grid(True, alpha=0.3)
    ax4.legend(fontsize=11)

fig.savefig(fname='all_vars.png')



fig_plotly = go.Figure(data=[go.Scatter3d(
    x=t_eval,
    y=results['glom0'].y[2],
    z=results['glom1'].y[2],
    mode='markers',
    marker=dict(
        size=2,
        color=t_eval,  # Color by time
        colorscale='Viridis',
        showscale=True
    )
)])

fig_plotly.update_layout(
    title='Glom State Space',
    scene=dict(
        xaxis_title='Time',
        yaxis_title='Glom0',
        zaxis_title='Glom1'
    )
)

# Save as interactive HTML
pyo.plot(fig_plotly, filename='glomstatespace.html', auto_open=False)
