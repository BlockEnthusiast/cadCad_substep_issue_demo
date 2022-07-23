"""
Simulation configuration such as the number of timesteps and Monte Carlo runs
"""



DELTA_TIME = int(10)  # epochs per timestep
SIMULATION_TIME_DAYS = 3 # number of days
TIMESTEPS = int(
    240 * SIMULATION_TIME_DAYS // DELTA_TIME
)  # number of simulation timesteps
MONTE_CARLO_RUNS = 1  # number of runs
