import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import os
os.chdir('Practical6')
# Parameters
N = 10000
beta = 0.3
gamma = 0.05
num_time_steps = 1000

# Vaccination percentages to simulate
vaccination_percentages = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,0.9,1.0]
colors = cm.viridis(np.linspace(0, 1, len(vaccination_percentages)))

plt.figure(figsize=(10, 6))

for idx, p in enumerate(vaccination_percentages):
    vaccinated = int(N * p)
    S_initial = N - vaccinated - 1  # Initial susceptible
    I_initial = 1
    R_initial = 0

    # Initialize compartments
    S = [S_initial]
    I = [I_initial]
    R = [R_initial]

    # Simulate over time
    for _ in range(num_time_steps):
        current_S = S[-1]
        current_I = I[-1]
        current_R = R[-1]

        # Calculate new infections
        infection_prob = beta * current_I / N
        if current_S > 0:
            new_infections = np.random.choice([0, 1], size=current_S, 
                                             p=[1 - infection_prob, infection_prob]).sum()
        else:
            new_infections = 0

        # Calculate new recoveries
        if current_I > 0:
            new_recoveries = np.random.choice([0, 1], size=current_I, 
                                            p=[1 - gamma, gamma]).sum()
        else:
            new_recoveries = 0

        # Update compartments
        S.append(current_S - new_infections)
        I.append(current_I + new_infections - new_recoveries)
        R.append(current_R + new_recoveries)

    # Plot infected curve
    plt.plot(I, color=colors[idx], label=f'{p*100:.0f}%')

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('Impact of Vaccination on Infection Spread')
plt.legend(title='Vaccination Percentage')
plt.savefig('sir_vaccination.png')
plt.show()