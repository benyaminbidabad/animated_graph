import numpy as np
import matplotlib
from matplotlib.animation import PillowWriter
import matplotlib.pyplot as plt

fig=plt.figure()



l,=plt.plot([],[],"k-")

# plt.plot([], [], "k-") creates a plot object in Matplotlib. 
# Even though it is plotting empty data (empty lists for x and y), it still returns a list (or technically, a tuple) containing the plot objects (usually one or more Line2D objects).

# If you need to manipulate the line object later (for example, updating its data during animation), it's more convenient to have l directly reference the Line2D object rather than the tuple containing it. This is a common pattern in plotting or animation scripts where the plot needs to be updated dynamically.

plt.xlim(-5,5)
plt.ylim(-5,5)
def func(x):
    return np.sin(x)*3

writer=PillowWriter(fps=15)


xlist=[]
ylist=[]

with writer.saving(fig,"./Output/sinWave.gif",100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        l.set_data(xlist,ylist)
        writer.grab_frame()