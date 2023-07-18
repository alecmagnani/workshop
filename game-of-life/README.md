# Conway's Game of Life

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a cellular automaton simulator. It is a 'zero-player game', meaning its evolution is determined by its initial state, requiring no further input.

## Rules
The Game of Life takes place in a 2-dimensional grid "universe" of square cells. Each cell exists in a state: `live` or `dead`. Cells interact with their neighbors, any cell that is adjacent. For each step of the simulation, the following rules are applied:

1. Any `live` cell with fewer than two `live neighbors` will be marked `dead`
2. Any `live` cell with two or three `live neighbors` will continue as `live`
3. Any `live` cell with greater than three `live neighbors` will be marked `dead`
4. Any `dead` cell with exactly three `live neighbors` will be marked `live`

## Usage

### Requirements
1. numpy
2. matplotlib
3. argparse
4. pygame

```
git clone https://github.com/alecmagnani/workshop.git
cd workshop/game-of-life
pip install numpy matplotlib argparse pygame
python conways-gol-simple.py [--grid-size 100] [--interval 50]
```
