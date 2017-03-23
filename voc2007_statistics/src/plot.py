import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def draw_histmap(z, x, y, filename):
    fig = plt.figure()
    ax = Axes3D(fig)
    #ax = fig.gca(projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_zlabel('Objects Count')
    #plt.show()
    plt.savefig(filename)
    plt.close()

def draw_heatmap(data, xlabels, ylabels, filename):
    figure=plt.figure(facecolor='w')
    ax=figure.add_subplot(2,1,1,position=[1,1,1,1])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    _map = ax.imshow(data,interpolation='lanczos',cmap='viridis',aspect='auto',vmin=vmin,vmax=vmax)
    cb = plt.colorbar(mappable=_map,cax=None,ax=None,shrink=2)
    #plt.show()
    plt.savefig(filename)
    plt.close()

def draw_blubble(data, x, y, filename):
    colors = np.random.rand(len(x))
    plt.scatter(x, y, s=data, c=colors, alpha=1)
    # plt.show()
    plt.savefig(filename)
    plt.close()

def draw_bar3d(data, width, height, strip_size, filename):
    x = np.array([i*strip_size for i in range(width/strip_size)])
    y = np.array([i*strip_size for i in range(height/strip_size)])
    hist = np.array(data)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xpos, ypos = np.meshgrid(x[:-1] + 0.25*strip_size, y[:-1] + 0.25*strip_size)
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)

    # Construct arrays with the dimensions for the 3dbars.
    dx = 0.5 * np.ones_like(zpos)
    dy = dx.copy()

    ax.bar3d(xpos, ypos, zpos, dx, dy, hist, color='r', zsort='average')
    # ax.annotate(hist, va="bottom", ha="center")

    # ax.annotate("", xy=zip(xpos, ypos), xytext=hist)
    plt.savefig(filename)
    plt.close()