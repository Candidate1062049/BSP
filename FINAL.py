import numpy as np
import matplotlib.pyplot as plt
import math
import time

n = input("Enter n:")
mesh = input("Specify the mesh:")

startTime = time.time()

epsilon = int(n) / int(mesh)


# We define the function
def xa(a1, a2):
    # Initialize the sum
    xa = 0
    # Perform the double summation with respect to the truncation of a 4x4 grid ar
    for i in np.arange(a1-2, a1+2.1, epsilon):
        for j in np.arange(a2-2, a2+2.1, epsilon):
            alphaij = np.random.normal(0, epsilon ** 2)
            xa += alphaij * np.exp(-((a1-i) ** 2 + (a2-j) ** 2))
    xa = xa * math.sqrt(2 / math.pi)
    return xa


# Generate random field data (2D example)
xs = np.linspace(0, int(n), int(mesh))
ys = np.linspace(0, int(n), int(mesh))

z = []

for i in xs:
    for j in ys:
        z = np.append(z, xa(i, j))

Z = z.reshape(int(mesh), int(mesh))

print(Z)

# Define threshold levels
thresholds = [0.5, 1.0]

# Plot the random field
plt.contourf(xs, ys, Z, cmap='coolwarm')
plt.colorbar(label='Random Field Value')

# Plot excursion sets
for threshold in thresholds:
    excursion_set = np.where(Z >= threshold, 1, 0)
    plt.contour(xs, ys, excursion_set, levels=[0.5], colors='black', linewidths=2)

endTime = time.time()
elapsedTime = endTime - startTime
print('Elapsed time: ', elapsedTime)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('2-D Bargmann-Fock Field with ϵ = 0.1')
plt.grid(True)
plt.show()

