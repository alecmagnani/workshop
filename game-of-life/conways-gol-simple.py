import argparse
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from functools import partial

interpolation_methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 
                         'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 
                         'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

color_maps = [
    # Perceptually Uniform Sequential
    'viridis', 'plasma', 'inferno', 'magma', 'cividis',
    # Sequential2
    'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 
    'cool', 'Wistia',  'hot', 'afmhot', 'gist_heat', 'copper',
    # Qualitative
    'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 
    'tab10', 'tab20', 'tab20b', 'tab20c',
    # Misc
    'flag', 'prism', 'ocean', 'terrain', 'gnuplot', 'gnuplot2',
    'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo'
]

ON = 255
OFF = 0

def randomGrid(N):
    return np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            # 8-neighbor-sum using x and y wrap-around
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # Conway's rules
            if grid[i, j] == ON:
                if (total <2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    # Set up args
    parser = argparse.ArgumentParser("Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--method', dest='method', required=False)
    parser.add_argument('--cmap', dest='cmap', required=False)
    args = parser.parse_args()

    # Set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # Set interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # Set interpolation method
    method = interpolation_methods[2]
    if args.method:
        if (args.method in interpolation_methods):
            method = args.method
        elif (args.method.casefold() == 'random') or (args.method.casefold() == 'rand'):
            method = np.random.choice(interpolation_methods, 1)[0]
            print('Using interpolation method: ' + method)

    # Set color map
    cmap = color_maps[0]
    if args.cmap:
        if (args.cmap in color_maps):
            cmap = args.cmap
        elif (args.cmap.casefold() == 'random') or (args.cmap.casefold() == 'rand'):
            cmap = np.random.choice(color_maps, 1)[0]
            print('Using color map: ' + cmap)

    # Init grid
    grid = randomGrid(N)

    # Start animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap=cmap, interpolation=method)
    ani = animation.FuncAnimation(fig, 
                                  partial(update, img=img, grid=grid, N=N),
                                  save_count=50,
                                  interval=updateInterval)

    plt.show()

if __name__ == '__main__':
    main()
