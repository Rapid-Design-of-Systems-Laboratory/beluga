import matplotlib.pyplot as plt

nodes = [31, 81, 151]
epsilon = [1e-4, 1e-5, 1e-6]

plt.figure()
plt.semilogx(epsilon, nodes, 'o-', mew=2, lw=2.0, ms=10)
plt.gca().invert_xaxis()
plt.xlabel('$\epsilon_i$', fontsize=13)
plt.ylabel('Number of QCPI nodes required', fontsize=13)
plt.tight_layout()
plt.savefig('plots/app_eps_nodes.eps')
plt.show()
