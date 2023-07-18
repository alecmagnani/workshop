import argparse
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    args = parser.parse_args()

    # Set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # Set interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    # Init grid
    grid = randomGrid(N)

    # Start animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10,
                                  interval=updateInterval)

    plt.show()

if __name__ == '__main__':
    main()
