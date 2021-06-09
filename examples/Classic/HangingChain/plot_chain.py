from beluga.utils import load
import matplotlib.pyplot as plt

sol_set = load('chain.beluga')['solutions']

for sol in sol_set[-1]:
    plt.plot(sol.y[:, 0], sol.y[:, 1])

plt.show()
