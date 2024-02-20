import numpy as np 
from numpy import ndarray
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
import matplotlib.pyplot as plt
from typing import Optional


class Contourf2Gif():
    def __init__(
            self, 
            field : ndarray,  
            Lx : Optional[int] = 1, 
            Ly : Optional[int] = 1, 
            namesave : Optional[str] = None,
            cmap : str = 'inferno'
            ) -> None:
        self.simulation_time = np.linspace(0, field.shape[0])
        self.field = field 
        self.cvals = np.linspace(0,self.field.max(),50)      # set contour values 
        self.x, self.y = np.meshgrid(
            np.linspace(0,Lx,field.shape[1]),
            np.linspace(0,Ly,field.shape[2])
            )
        self.namesave = namesave
        self.interval = 200 # ms between 2 frames
        self.cmap = cmap

    def update_plot(self, i : int):
        z = self.field[i,:,:]
        for c in self._p1:
            c.remove()  # removes only the contours, leaves the rest intact
        self._p1 = plt.contourf(self.x, self.y, z, self.cvals,cmap=self.cmap).collections
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
