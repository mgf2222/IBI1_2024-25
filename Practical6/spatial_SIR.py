import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Parameters
beta = 0.2  # Infection rate per neighbor
gamma = 0.1  # Recovery rate
time_steps = 100
grid_size = 100

# Initialize grid: 0=Susceptible, 1=Infected, 2=Recovered
population = np.zeros((grid_size, grid_size), dtype=int)

# Set random outbreak location ensuring it's not vaccinated
outbreak = np.random.choice(grid_size, 2)
population[outbreak[0], outbreak[1]] = 1

# Custom colormap: S=purple, I=cyan, R=yellow
colors = ['darkviolet', 'cyan', 'yellow']
cmap = ListedColormap(colors)

# Setup plot
plt.figure(figsize=(10, 6), dpi=100)

for t in range(time_steps):
    new_population = np.copy(population)
    
    # Find infected cells
    infected_i, infected_j = np.where(population == 1)
    
    # Spread infection
    for i, j in zip(infected_i, infected_j):
        # Check all 8 neighbors
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # Skip self
                ni, nj = i + di, j + dj
                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    if population[ni, nj] == 0:  # Infect susceptible
                        if np.random.rand() < beta:
                            new_population[ni, nj] = 1
    
    # Handle recovery
    for i, j in zip(infected_i, infected_j):
        if np.random.rand() < gamma:
            new_population[i, j] = 2
    
    population = new_population
    
    # Plot every 10th time step
    if t % 10 == 0 or t == time_steps-1:
        plt.clf()
        plt.imshow(population, cmap=cmap, vmin=0, vmax=2, interpolation='nearest')
        plt.title(f'Time Step: {t}')
        plt.axis('off')
        plt.pause(0.1)

plt.show()