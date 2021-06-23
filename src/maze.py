import numpy as np
import matplotlib.pyplot as plt

#init
fig = plt.figure(figsize=(5, 5))
ax = plt.gca()
N = 10

#wall in the maze
plt.plot([0, 10], [0, 0], color='black', linewidth=2)
plt.plot([0, 0], [0, 10], color='black', linewidth=2)
plt.plot([0, 10], [10, 10], color='black', linewidth=2)
plt.plot([10, 10], [0, 10], color='black', linewidth=2)
plt.plot([1, 2], [1, 1], color='black', linewidth=2)
plt.plot([3, 3], [0, 1], color='black', linewidth=2)
plt.plot([4, 4], [0, 4], color='black', linewidth=2)
plt.plot([5, 6], [1, 1], color='black', linewidth=2)
plt.plot([7, 7], [0, 1], color='black', linewidth=2)
plt.plot([8, 9], [1, 1], color='black', linewidth=2)
plt.plot([2, 2], [1, 2], color='black', linewidth=2)
plt.plot([5, 5], [1, 5], color='black', linewidth=2)
plt.plot([6, 6], [1, 2], color='black', linewidth=2)
plt.plot([8, 8], [1, 9], color='black', linewidth=2)
plt.plot([1, 1], [2, 3], color='black', linewidth=2)
plt.plot([2, 4], [2, 2], color='black', linewidth=2)
plt.plot([6, 8], [2, 2], color='black', linewidth=2)
plt.plot([9, 9], [2, 3], color='black', linewidth=2)
plt.plot([1, 3], [3, 3], color='black', linewidth=2)
plt.plot([3, 3], [3, 5], color='black', linewidth=2)
plt.plot([5, 6], [3, 3], color='black', linewidth=2)
plt.plot([7, 7], [3, 8], color='black', linewidth=2)
plt.plot([9, 10], [3, 3], color='black', linewidth=2)
plt.plot([0, 2], [4, 4], color='black', linewidth=2)
plt.plot([2, 2], [4, 5], color='black', linewidth=2)
plt.plot([6, 7], [4, 4], color='black', linewidth=2)
plt.plot([8, 9], [4, 4], color='black', linewidth=2)
plt.plot([1, 2], [5, 5], color='black', linewidth=2)
plt.plot([3, 5], [5, 5], color='black', linewidth=2)
plt.plot([4, 4], [5, 6], color='black', linewidth=2)
plt.plot([6, 6], [5, 7], color='black', linewidth=2)
plt.plot([9, 9], [5, 10], color='black', linewidth=2)
plt.plot([0, 1], [7, 7], color='black', linewidth=2)
plt.plot([1, 1], [6, 7], color='black', linewidth=2)
plt.plot([1, 3], [6, 6], color='black', linewidth=2)
plt.plot([3, 3], [7, 8], color='black', linewidth=2)
plt.plot([3, 4], [7, 7], color='black', linewidth=2)
plt.plot([4, 5], [6, 6], color='black', linewidth=2)
plt.plot([5, 5], [6, 7], color='black', linewidth=2)
plt.plot([5, 6], [7, 7], color='black', linewidth=2)
plt.plot([2, 2], [7, 9], color='black', linewidth=2)
plt.plot([1, 1], [8, 9], color='black', linewidth=2)
plt.plot([1, 2], [8, 8], color='black', linewidth=2)
plt.plot([3, 5], [8, 8], color='black', linewidth=2)
plt.plot([6, 8], [8, 8], color='black', linewidth=2)
plt.plot([5, 5], [8, 9], color='black', linewidth=2)
plt.plot([6, 6], [8, 9], color='black', linewidth=2)
plt.plot([5, 6], [9, 9], color='black', linewidth=2)
plt.plot([2, 4], [9, 9], color='black', linewidth=2)
plt.plot([7, 7], [9, 10], color='black', linewidth=2)
plt.plot([4, 4], [9, 10], color='black', linewidth=2)



#start and goal
plt.text(0.5, 9.5, 'START', ha='center')
plt.text(9.5, 0.5, 'GOAL', ha='center')

#drawing range
ax.set_xlim(0, N)
ax.set_ylim(0, N)
plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
ax.axis("off")
#initial agent
line, = ax.plot([0.5], [9.5], marker="o", color='r', markersize=20)

#initial policy  row:state, column:↑→↓←
theta_0 = np.array([[np.nan, 1, 1, np.nan],  #s0
					[np.nan, 1, 1, 1],  #s1
                    [np.nan, 1, np.nan, 1],  #s2
                    [np.nan, 1, np.nan, 1],  #s3
                    [np.nan, 1, 1, 1],  #s4
                    [np.nan, 1, np.nan, 1], #s5
                    [np.nan, np.nan, 1, 1], #s6
                    [np.nan, 1, 1, np.nan], #s7
					[np.nan, np.nan, 1, 1],  #s8
                    [np.nan, np.nan, 1, np.nan],  #s9
                    [1, np.nan, 1, np.nan],  #s10
                    [1, np.nan, np.nan, np.nan],  #s11
                    [np.nan, 1, 1, np.nan],  #s12
                    [np.nan, 1, np.nan, 1], #s13
                    [1, np.nan, np.nan, 1], #s14
					[np.nan, np.nan, 1, np.nan],  #s15
					[1, 1, np.nan, np.nan],  #s16
                    [1, np.nan, np.nan, 1],  #s17
                    [1, np.nan, 1, np.nan],  #s18
                    [1, np.nan, 1, np.nan],  #s19
                    [1, 1, np.nan, np.nan],  #s20
					[np.nan, np.nan, 1, 1],  #s21
                    [1, np.nan, 1, np.nan],  #s22
                    [np.nan, 1, np.nan, np.nan],#s23
                    [np.nan, 1, 1, 1],  #s24
                    [1, 1, np.nan, 1],  #s25
                    [np.nan, np.nan, 1, 1],  #s26
                    [np.nan, np.nan, 1, np.nan],  #s27
                    [1, np.nan, 1, np.nan], #s28
                    [1, np.nan, 1, np.nan], #s29
                    [np.nan, np.nan, 1, np.nan], #s30
					[1, 1, np.nan, np.nan],  #s31
                    [1, 1, np.nan, 1],  #s32
                    [np.nan, 1, 1, np.nan],  #s33
                    [1, np.nan, np.nan, 1],  #s34
                    [np.nan, np.nan, 1, np.nan],  #s35
                    [1, np.nan, 1, np.nan], #s36
                    [1, np.nan, 1, np.nan], #s37
					[1, np.nan, 1, np.nan],  #s38
					[1, np.nan, 1, np.nan],  #s39
                    [1, 1, 1, np.nan],  #s40
                    [np.nan, 1, np.nan, 1],  #s41
                    [np.nan, 1, 1, 1],  #s42
                    [1, np.nan, np.nan, 1],  #s43
					[np.nan, 1, np.nan, np.nan],  #s44
                    [1, np.nan, 1, 1],  #s45
                    [1, np.nan, 1, np.nan],#s46
                    [1, np.nan, 1, np.nan],  #s47
                    [1, np.nan, 1, np.nan],  #s48
                    [1, np.nan, 1, np.nan],  #s49
                    [1, 1, np.nan, np.nan],  #s50
                    [np.nan, np.nan, np.nan, 1], #s51
                    [1, np.nan, 1, np.nan], #s52
                    [np.nan, 1, 1, np.nan], #s53
					[np.nan, np.nan, 1, 1],  #s54
                    [1, 1, 1, np.nan],  #s55
                    [1, np.nan, np.nan, 1],  #s56
                    [1, np.nan, 1, np.nan],  #s57
                    [1, 1, np.nan, np.nan],  #s58
                    [1, np.nan, 1, 1], #s59
                    [np.nan, 1, 1, np.nan], #s60
					[np.nan, 1, np.nan, 1],  #s61
					[1, np.nan, np.nan, 1],  #s62
                    [1, np.nan, 1, np.nan],  #s63
                    [1, np.nan, 1, np.nan],  #s64
                    [1, 1, np.nan, np.nan],  #s65
                    [np.nan, np.nan, 1, 1],  #s66
					[1, np.nan, 1, np.nan],  #s67
                    [np.nan, 1, 1, np.nan],  #s68
                    [1, np.nan, np.nan, 1],#s69
                    [1, np.nan, 1, np.nan],  #s70
                    [np.nan, 1, 1, np.nan],  #s71
                    [np.nan, 1, np.nan, 1],  #s72
                    [1, np.nan, np.nan, 1],  #s73
                    [1, np.nan, 1, np.nan], #s74
                    [np.nan, 1, 1, np.nan], #s75
                    [1, 1, np.nan, 1], #s76
					[1, np.nan, np.nan, 1],  #s77
                    [1, np.nan, 1, np.nan],  #s78
                    [np.nan, np.nan, 1, np.nan],  #s79
                    [1, 1, 1, np.nan],  #s80
                    [1, np.nan, np.nan, 1],  #s81
                    [np.nan, 1, 1, np.nan], #s82
                    [np.nan, np.nan, 1, 1], #s83
					[1, np.nan, 1, np.nan],  #s84
					[1, np.nan, np.nan, np.nan],  #s85
                    [np.nan, 1, 1, np.nan],  #s86
                    [np.nan, np.nan, 1, 1],  #s87
                    [1, 1, np.nan, np.nan],  #s88
                    [1, np.nan, 1, 1],  #s89
					[1, 1, np.nan, np.nan],  #s90
                    [np.nan, 1, np.nan, 1],  #s91
                    [1, np.nan, np.nan, 1],#s92
                    [np.nan, np.nan, np.nan, 1],#s93
                    [1, 1, np.nan, np.nan],#s94
                    [np.nan, 1, np.nan, 1],#s95
                    [1, np.nan, np.nan, 1],#s96
                    [1, 1, np.nan, np.nan],#s97
                    [np.nan, 1, np.nan, 1],#s98
					#[goal, goal, goal, goal] #s
                ])


fig.savefig('figs/maze.png')