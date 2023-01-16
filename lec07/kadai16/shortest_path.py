from maze_maker import Maze, Cell
from pprint import pprint
from collections import deque

class ShortestPath:
    def __init__(self, map: Maze):
        self.map = map

    def bfs(self):
        pass

    def back_trace(self):
        pass

if __name__ == "__main__":
    tate, yoko = 9, 15
    maze = Maze(tate, yoko)
    sp = ShortestPath(maze)
    sp.bfs()
    sp.back_trace()
    maze.show_maze()
