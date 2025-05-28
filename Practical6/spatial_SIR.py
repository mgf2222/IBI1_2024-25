import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

"""Copy the current population grid.
Find all currently infected cells.
For each infected cell, check its 8 neighbors; infect each susceptible neighbor with probability beta.
For each infected cell, recover with probability gamma.
Update the population grid.
If it's the last time step or every 10th time step, clear the plot, display the updated grid with the colormap, set the title to the current time step, remove axes, and pause briefly for animation."""

# Parameters
beta = 0.3 # Infection rate per neighbor
gamma = 0.05  # Recovery rate
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