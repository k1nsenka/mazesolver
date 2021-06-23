import numpy as np
import matplotlib.pyplot as plt

#init
fig = plt.figure(figsize=(5, 5))
ax = plt.gca()
N = 5

#wall in the maze
plt.plot([1, 1], [1, 2], color='black', linewidth=2)
plt.plot([2, 5], [1, 1], color='black', linewidth=2)
plt.plot([0, 3], [2, 2], color='black', linewidth=2)
plt.plot([3, 3], [2, 4], color='black', linewidth=2)
plt.plot([4, 4], [2, 3], color='black', linewidth=2)
plt.plot([1, 2], [3, 3], color='black', linewidth=2)
plt.plot([3, 4], [3, 3], color='black', linewidth=2)
plt.plot([1, 1], [3, 4], color='black', linewidth=2)
plt.plot([2, 3], [4, 4], color='black', linewidth=2)
plt.plot([4, 4], [4, 5], color='black', linewidth=2)
plt.plot([0, 0], [0, 5], color='black', linewidth=2)
plt.plot([5, 5], [0, 5], color='black', linewidth=2)
plt.plot([0, 5], [5, 5], color='black', linewidth=2)
plt.plot([0, 5], [0, 0], color='black', linewidth=2)

#start and goal
plt.text(0.5, 4.5, 'START', ha='center')
plt.text(4.5, 0.5, 'GOAL', ha='center')

#drawing range
ax.set_xlim(0, N)
ax.set_ylim(0, N)
plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
ax.axis("off")
#initial agent
line, = ax.plot([0.5], [4.5], marker="o", color='r', markersize=20)


fig.savefig('figs/maze.png')