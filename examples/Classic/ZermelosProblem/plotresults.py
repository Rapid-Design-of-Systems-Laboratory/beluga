from beluga.utils import load
import matplotlib.pyplot as plt

data = load('data.blg')
sol_set = data['solutions']

sol = sol_set[-1][-1]

plt.figure()
plt.plot(sol.y[:, 0], sol.y[:, 1])
plt.grid(True)
plt.show()
