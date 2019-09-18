from beluga.bvpsol.Pseudospectral import linter
from beluga.utils import load
import matplotlib.pyplot as plt
import numpy as np

data = load('data.blg')

sol_set = data['solutions']
continuation = sol_set[-1]
ind = 0
L = len(continuation)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.y[:, 0], sol.y[:, 1], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('Phase Plot')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.u[:, 0], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('Control History Plot')
plt.xlabel('Time [s]')
plt.ylabel('Control, $u$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.dual[:, 0], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('$\\lambda_{x1}$ History Plot')
plt.xlabel('Time [s]')
plt.ylabel('$\\lambda_{x1}$')
plt.grid(True)

plt.figure()
for ind, sol in enumerate(continuation):
    plt.plot(sol.t, sol.dual[:, 1], linestyle='-', color=(1*(ind/L), 0, 1*(L-ind)/L))

plt.title('$\\lambda_{x2}$ History Plot')
plt.xlabel('Time [s]')
plt.ylabel('$\\lambda_{x2}$')
plt.grid(True)
plt.show()
