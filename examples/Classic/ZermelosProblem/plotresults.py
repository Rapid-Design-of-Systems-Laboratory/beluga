from beluga.utils import load
import matplotlib.pyplot as plt

sol_set = load('data.json')

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:, 0], sol.y[:, 1])
plt.grid(True)
plt.show()
