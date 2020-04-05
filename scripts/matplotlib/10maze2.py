# https://gist.github.com/schedutron/0077053a842e5925f31594bb473a8554

from random import randint, sample
from sys import argv
from time import sleep

try:
    height, width = [int(dim) for dim in argv[1:]]
except (IndexError, ValueError) as ve:
    print("Usage:\n$ disjoint_set_maze_generator.py <height> <width>")
    exit()

if not width or not height:
    exit()

# Just for animation purposes
TOTAL_TIME = 10  # at most, and in seconds (roughly double than observed values)

parent = list(range(width*height))
rank = [0] * len(parent)

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    u, v = find(a), find(b)
    if u == v:
        return
    if rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[u] = v
        if rank[v] == rank[u]:
            rank[v] += 1


def get_coords(num):
    return num // width, num % width


def disp_maze(width=1, height=1, maze={}, timedelta=0.01):
    # Perhaps can be made more concise

    for i in range(height+1):
        print('+', end='')
        for j in range(width):
            if ((i-1, j), (i, j)) in maze or i == 0 or i == height:
                seq = '--'
            else:
                seq = '  '
            if ((i, j), (i, j+1)) in maze or ((i-1, j), (i-1, j+1)) in maze \
                or j == width-1:
                    end = '+'
            elif seq == '--' or i == 0 or i == height:
                end = '-'
            else:
                end = ' '
            print(seq, end=end)
        print()
        if i == height:
            break

        for j in range(width):
            if ((i, j-1), (i, j)) in maze or j == 0 and i != 0:
                seq = '|  '
            else:
                seq = '   '
            print(seq, end='')
        if i != height-1:
            row_last_wall = '|'
        else:
            row_last_wall = ''
        print(row_last_wall)

    # To get back to 0th row ceiling to rerender the new maze layout
    print("\033[%dA" % 2*(height+1))
    sleep(timedelta)  # To slow down, for animation

if __name__ == '__main__':
    edges_of_cells = {
        edge for num in parent[:-1]
        for edge in ((num, num+1), (num, num+width))
        if not (edge[0] % width == width-1 and edge[1]-edge[0] < width) and \
            edge[1] <= parent[-1]
        }
    timedelta = TOTAL_TIME / len(edges_of_cells)

    maze = set()
    # Display initial state of maze
    disp_maze(width, height, maze, 0)

    # while there is more than 1 set of connected cells
    while len(set([find(n) for n in parent])) > 1:
        rand_edge = sample(edges_of_cells, 1)[0]
        edges_of_cells.remove(rand_edge)
        u, v = find(rand_edge[0]), find(rand_edge[1])
        if u != v:
            union(u, v)
        else:
            maze.add((get_coords(rand_edge[0]), get_coords(rand_edge[1])))
            disp_maze(width, height, maze, timedelta)
    # maze = maze.union(
    #     {
    #         (get_coords(edge[0]), get_coords(edge[1]))
    #         for edge in edges_of_cells
    #         }
    #     )

    # The code commented above works, but we'll use the following for a nicer
    # animation

    while edges_of_cells:
        maze.add(tuple(get_coords(num) for num in edges_of_cells.pop()))
        disp_maze(width, height, maze, timedelta)
        # To get back to 0th row ceiling to rerender the new maze layout

    # To reach the end of display
    # 2*(height+1) is probably a higher number but works
    print("\033[%dB" % (2*height))
