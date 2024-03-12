import numpy as np 
from numpy import ndarray
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
import matplotlib.pyplot as plt
from typing import Optional


import numpy as np 
from numpy import ndarray
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
import matplotlib.pyplot as plt
from typing import Optional
import matplotlib.animation as animation

import os, sys
sys.path.append(os.getcwd())
from helper_functions.helper_functions.general import linspace



def imshow_animated(
        trajectory,
        moviename = None,
        cmap = 'plasma',
        interval = 75,
        repeat_delay = 1000,
        dt=1
):
    n_step = trajectory.shape[0]
    t = linspace(0,n_step,dt)
    fig, ax = plt.subplots()
    ims = []
    for j in range(trajectory.shape[0]):
        title = '{}s'.format(t[j])
        im = ax.imshow(
            np.abs(trajectory[j,...]), 
            animated=True, 
            interpolation='bicubic',
            cmap=cmap,
            origin="lower")
        ttl = ax.text(
            0.5, 1.01, title, 
            horizontalalignment='center', 
            verticalalignment='bottom', 
            transform=ax.transAxes)
        ims.append([im, ttl])
    ani = animation.ArtistAnimation(
        fig, ims, 
        interval=interval, 
        blit=False,
        repeat_delay=repeat_delay)
    if moviename is not None:
        ani.save(filename=moviename, writer="pillow")


# def imshow_animated(
#         trajectory,
#         moviename = None,
#         cmap = 'plasma',
#         interval = 75,
#         repeat_delay = 1000
# ):
#     fig, ax = plt.subplots()
#     ims = []
#     for i in range(len(trajectory)):
#         im = ax.imshow(
#             np.abs(trajectory[i]), 
#             animated=True, 
#             interpolation='bicubic',
#             cmap=cmap,
#             origin="lower")
#         if i == 0:
#             ax.imshow(np.abs(
#                 trajectory[i]), 
#                 interpolation='bicubic',
#                 cmap=cmap,
#                 origin="lower")  # show an initial one first
#         ims.append([im])

#     ani = animation.ArtistAnimation(
#         fig, ims, 
#         interval=interval, 
#         blit=True,
#         repeat_delay=repeat_delay)
#     if moviename is not None:
#         ani.save(filename=moviename, writer="pillow")

        


class Contourf2Gif():
    def __init__(
            self, 
            field : ndarray,  
            Lx : Optional[int] = 1, 
            Ly : Optional[int] = 1, 
            namesave : Optional[str] = None,
            cmap : str = 'inferno',
            normalize : bool = True,
            ) -> None:
        self.simulation_time = np.linspace(0, field.shape[0])
        # self.field = np.transpose(field, (0, 2, 1))
        if normalize:
            field = (field-field.min())/(field.max()-field.min())
        self.field = field
        self.cvals = np.linspace(0,self.field.max(),50)      # set contour values 
        Ly = 1
        Lx = field.shape[2]/field.shape[1]
        self.y,self.x = np.meshgrid(
            np.linspace(0,Ly,field.shape[1]),
            np.linspace(0,Lx,field.shape[2]),
            indexing='xy'
            )
        self.x, self.y = self.x.T, self.y.T
        self.namesave = namesave
        self.interval = 200 # ms between 2 frames
        self.cmap = cmap

    def update_plot(self, i : int):
        z = self.field[i,:,:]
        for c in self._p1:
            c.remove()  # removes only the contours, leaves the rest intact
        self._p1 = plt.contourf(self.x, self.y, z, self.cvals,cmap=self.cmap).collections
        self.axes.set_aspect('equal')
        plt.title('t = %i' % (i))
        return self._p1

    def start_simulation(self):
        self.fig, self.axes = plt.subplots()
        self._p1 = plt.contourf(self.x, self.y, self.field[0,:,:], self.cvals,cmap=self.cmap).collections
        self.ani = FuncAnimation(
            fig=self.fig,
            func=self.update_plot,
            interval=self.interval, 
            repeat = False,
            blit=False, 
            frames=self.field.shape[0]
            )
        if self.namesave is not None:
            self.ani.save(
                filename=self.namesave,
                writer=PillowWriter(
                    fps=1/self.interval*1000,
                    metadata=dict(artist='Me'),
                    bitrate=1800))
            
            

def contour_gif(
        data,
        animation_name = None,
        Lx = 1,
        Ly = 1,
        ):
    global anim
    x,y = np.meshgrid(
        np.linspace(0,Lx,data.shape[1]),
        np.linspace(0,Lx,data.shape[2])
    )
    Nt = data.shape[0]

    fig = plt.figure()
    ax = plt.axes(xlim=(0, Lx), ylim=(0, Ly), xlabel='x', ylabel='y')
    cvals = np.linspace(0,data.max(),50)      # set contour values 
    cont = plt.contourf(x, y, data[0,:,:], cvals)    # first image on screen
    plt.colorbar()

    # animation function
    def animate(i):
        z = data[i,:,:]
        # for c in cont.collections:
        #     c.remove()  # removes only the contours, leaves the rest intact
        cont = plt.contourf(x, y, z, cvals)
        plt.title('t = %i' % (i))
        return cont

    anim = FuncAnimation(fig, animate, frames=Nt, repeat=True)
    if animation_name is not None:
        anim.save(animation_name, writer=FFMpegWriter())
    return anim
