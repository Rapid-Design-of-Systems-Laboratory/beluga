import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, formatter=None):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        if formatter is None:
            label = '%.2f' % (height)
        else:
            label = formatter(height)

        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                label,
                ha='center', va='bottom')

# data to plot
n_groups = 5
qcpi_time = (0.06, 0.14, 0.49, 0.63, 7.76)
shooting_time = (1.26, 1.7, 4.4, 9.35, 39.2)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, shooting_time, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Shooting Method')

rects2 = plt.bar(index + bar_width, qcpi_time, bar_width,
                 alpha=opacity,
                 color='g',
                 label='QCPI')

plt.xlabel('Number of Vehicles',fontsize=13)
plt.ylabel('Runtime [sec]',fontsize=13)
# plt.title('Scores by person')
plt.xticks(index + bar_width, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
plt.legend()

autolabel(rects1)
autolabel(rects2)
plt.ylim([0,45])
plt.grid(True)

plt.tight_layout()
plt.show()


# data to plot
plt.figure()
n_groups = 5
qcpi_speedup = tuple(s_t/q_t for s_t,q_t in zip(shooting_time,qcpi_time))

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, qcpi_speedup, bar_width,
                 alpha=opacity,
                 color='b',
                 label='QCPI Speedup')

# rects2 = plt.bar(index + bar_width, qcpi_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='QCPI')

plt.xlabel('Number of Vehicles',fontsize=13)
plt.ylabel('QCPI Speedup [x]',fontsize=13)
# plt.title('Scores by person')
plt.xticks(index, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
# plt.legend()

autolabel(rects1, formatter=lambda h: '%d'%int(h))

plt.ylim([0,45])
plt.grid(True)

plt.tight_layout()
plt.show()




# data to plot
plt.figure()
n_groups = 5
qcpi_compile_time = (2.76,3.58,8.00,19.01,96.68,)
shooting_compile_time = (0.37,0.5,0.96,1.77,5)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, shooting_compile_time, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Shooting Method')

rects2 = plt.bar(index + bar_width, qcpi_compile_time, bar_width,
                 alpha=opacity,
                 color='g',
                 label='QCPI')

plt.xlabel('Number of Vehicles',fontsize=13)
plt.ylabel('Compile time [sec]',fontsize=13)

plt.xticks(index + bar_width, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
# plt.legend()

autolabel(rects1)

plt.ylim([0,105])
plt.grid(True)

plt.tight_layout()
plt.show()
