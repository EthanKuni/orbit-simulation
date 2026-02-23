import numpy as np
import matplotlib.pyplot as plt

# initial conditions
x, y = 1.0, 0.0
vx, vy = 0.0, 1.0

# time settings
dt = 0.01
steps = 5000

# store positions for plotting
xs = []
ys = []
energies = []
for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    ax = -x / r**3
    ay = -y / r**3

    vx += ax * dt
    vy += ay * dt
    
    x += vx * dt
    y += vy * dt
    # recompute r after updating position
    r = np.sqrt(x**2 + y**2)
    print(r)
    v2 = vx**2 + vy**2
    E = 0.5 * v2 - 1 / r
    if _ % 500 == 0:
        print("r =", r, "E =", E)
    if r < 0.3:
        print("SMALL r:", r)


    energies.append(E)
    xs.append(x)
    ys.append(y)

plt.plot(energies)
plt.xlabel("Step")
plt.ylabel("Total Energy")
plt.show()

