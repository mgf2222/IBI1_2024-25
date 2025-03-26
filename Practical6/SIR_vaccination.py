import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define initial parameters
N = 10000          # Total population
beta = 0.3         # Infection rate
gamma = 0.05       # Recovery rate
num_time_steps = 1000
vaccination_percentages = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Create figure and color map
plt.figure(figsize=(10, 6))
colors = cm.viridis(np.linspace(0, 1, len(vaccination_percentages)))

for idx, p in enumerate(vaccination_percentages):
    # Initial vaccinated and susceptible populations
    V0 = int(p * N)
    S0 = N - V0 - 1  # Initial susceptible
    I0 = 1
    R0 = 0

    # Initialize compartments
    S = [S0]
    I = [I0]
    R = [R0]

    # Run simulation
    for _ in range(num_time_steps):
        current_S, current_I, current_R = S[-1], I[-1], R[-1]
        
        # Calculate new infections
        infection_prob = beta * current_I / N
        new_infections = np.random.choice([0, 1], size=current_S, p=[1 - infection_prob, infection_prob]).sum() if current_S > 0 else 0
        
        # Calculate new recoveries
        new_recoveries = np.random.choice([0, 1], size=current_I, p=[1 - gamma, gamma]).sum() if current_I > 0 else 0
        
        # Update compartments
        S.append(current_S - new_infections)
        I.append(current_I + new_infections - new_recoveries)
        R.append(current_R + new_recoveries)
    
    # Plot infected curve
    plt.plot(I, color=colors[idx], label=f'{p*100:.0f}% Vaccinated')

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('Impact of Vaccination on Infection Spread')
plt.legend()
plt.savefig('sir_vaccination.png')
plt.show()