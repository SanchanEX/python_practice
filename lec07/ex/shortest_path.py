from maze_maker import Maze, Cell
from pprint import pprint
from collections import deque


class ShortestPath:
    def __init__(self, map: Maze):
        self.map = map

    def bfs(self):
        que = deque()
        start: Cell = self.map.start
        start.dist = 0  # startを0に設定
        # 1.スタートマスをenqueue
        que.append(start)
        while True:
            try:
                # 3. キューからマスを1つdequeue
                current = que.popleft()
            except:
                break
            print(current)
            if current.state == "G":
                break
            for cell in self.map.get_adj(current):
                if cell.dist != -1:  # 既に訪れていたら
                    continue
                # 6.currentの距離+1をcellに設定する
                cell.dist = current.dist + 1
                # 7.cellをキューにenqueueする
                que.append(cell)


if __name__ == "__main__":
    tate, yoko = 9, 15
    maze = Maze(tate, yoko)
    # maze.show_maze()
    sp = ShortestPath(maze)
    sp.bfs()
    maze.show_maze()
