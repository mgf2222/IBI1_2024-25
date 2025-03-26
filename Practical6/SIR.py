import numpy as np
import matplotlib.pyplot as plt

# Define initial parameters
N = 10000  # Total population
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Initialize the compartments
S = [9999]  # Susceptible
I = [1]     # Infected
R = [0]     # Recovered

# Number of time steps to simulate
num_time_steps = 1000
'''for each time step in num_time_steps:
    get the current values of S, I, R
    calculate the infection probability for susceptibles
    determine new infections based on infection probability
    determine new recoveries based on recovery rate
    update the compartments S, I, R'''
# Simulate over time
for _ in range(num_time_steps):
    current_S = S[-1]
    current_I = I[-1]
    current_R = R[-1]
    
    # Calculate infection probability for susceptibles
    infection_prob = beta * current_I / N
    
    # Determine new infections
    if current_S > 0:
        new_infections = np.random.choice([0, 1], size=current_S, p=[1 - infection_prob, infection_prob]).sum()
    else:
        new_infections = 0
    
    # Determine new recoveries
    if current_I > 0:
        new_recoveries = np.random.choice([0, 1], size=current_I, p=[1 - gamma, gamma]).sum()
    else:
        new_recoveries = 0
    
    # Update compartments
    S.append(current_S - new_infections)
    I.append(current_I + new_infections - new_recoveries)
    R.append(current_R + new_recoveries)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend()
plt.savefig('sir_model.png', format='png')
plt.show()

