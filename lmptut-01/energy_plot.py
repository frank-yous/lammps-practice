import matplotlib.pyplot as plt

# Initialize empty lists to store the data
time_steps = []
time = []
kinetic_energy = []
potential_energy = []

# Read the data from the file
with open('energy.dat', 'r') as f:
    # Skip the first two lines of the file
    next(f)
    next(f)
    # Loop over the remaining lines and extract the data
    for line in f:
        data = line.split()
        time_steps.append(int(data[0]))
        kinetic_energy.append(float(data[1]))
        potential_energy.append(float(data[2]))

for time_step in time_steps:
    time.append(time_step * 0.005)

# Plot the kinetic energy
plt.plot(time, kinetic_energy)
plt.xlabel('Time')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy vs. Timestamp')
plt.show()

# Plot the potential energy
plt.plot(time, potential_energy)
plt.xlabel('Time')
plt.ylabel('Potential Energy')
plt.title('Potential Energy vs. Timestamp')
plt.show()
