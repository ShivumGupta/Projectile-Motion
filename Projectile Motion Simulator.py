import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams
rcParams['text.usetex'] = True


def calc_max_dist(u,theta,g=9.81):
    #convert theta into radians
    theta = theta*np.pi/180 
    return ((u**2)/g) * np.sin(2*theta)

def calculate_positions(u,theta,n=40):
    max_dist = calc_max_dist(u,theta)
    theta = theta*np.pi/180
    xs = np.linspace(0,max_dist,n)
    time = np.divide(xs,u*np.cos(theta))
    ys = np.multiply (u*np.sin(theta),time)
    ys = np.add(ys,np.multiply(0.5*-9.81,np.power(time,2)))

    xs = list(xs)
    ys = list(ys)
    return [xs,ys]


angles = [15,45,60,50,30,80]
drawings = [calculate_positions(5,angle,100) for angle in angles]

fig = plt.figure()
ax = plt.axes(xlim=(0,max([max(item[0]) for item in drawings])), ylim=(0,max([max(item[1]) for item in drawings])))

lines = []
for n in range(len(drawings)):
    line = ax.plot([],[],label=angles[n]) # Add something to deal with labels
    lines.append(line)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.legend()

# for angle in [45,40,50]:
#     xs,ys = calculate_positions(5,angle)
#     plt.scatter(xs,ys,label=angle)

# plt.legend()
# plt.show()


def animate(i):
    for j in range(len(lines)):
        lines[j][0].set_xdata(drawings[j][0][:i])
        lines[j][0].set_ydata(drawings[j][1][:i])

anim = FuncAnimation(fig, animate,interval=0.001,repeat=True,frames=150)
plt.show()