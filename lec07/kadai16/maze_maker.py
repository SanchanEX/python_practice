from dataclasses import dataclass, field
from random import randint, sample
from itertools import product
import tkinter as tk

@dataclass
class Cell:
    """
    迷路の１マスを表わすクラス
    state: " "が床，"#"が壁，"S"がスタート，"G"がゴール
    """
    y: int
    x: int
    state:str = " " # デフォルトで床
    dist: int = -1  # スタートからの距離
    adj: list = field(default_factory=list)
    parent: "Cell" = None


class Maze:
    def __init__(self, tate, yoko):
        self.tate, self.yoko = tate, yoko
        self.map = self.generate()

    def generate(self):
        """
        self.tate x self.yokoの迷路を生成する
        Cellインスタンスが並ぶ二次元リストmaze_lstを返す
        """
        XP = [ 0, 1, 0, -1]
        YP = [-1, 0, 1,  0]

        maze_lst = [[Cell(y, x, " ", -1) for x in range(self.yoko)] for y in range(self.tate)]

        for y in range(1, self.tate, 2):
            for x in range(1, self.yoko, 2):
                maze_lst[y][x].state = "#"
        for y in range(1, self.tate-1, 2):
            for x in range(1, self.yoko-1, 2):
                if x > 2: rnd = randint(0, 2)
                else:     rnd = randint(0, 3)
                maze_lst[y+YP[rnd]][x+XP[rnd]].state = "#"

        start_goal = [(s, g) for s, g in product([0, self.tate-1], [0, self.yoko-1])]
        start, goal = sample(start_goal, 2)
        self.start = maze_lst[start[0]][start[1]]
        self.start.state = "S"
        self.goal = maze_lst[goal[0]][goal[1]]
        self.goal.state = "G"
        return maze_lst

    def get_adj(self, current: Cell) -> list[Cell]:
        """
        隣接するマスのうち，壁でないマスのリストを返す
        """
        tonari = [(1,0), (0,1), (-1,0), (0,-1)]
        cy, cx = current.y, current.x
        adj_lst = [self.map[cy+y][cx+x] for y, x in tonari 
                   if 0 <= cy+y < self.tate and 0 <= cx+x < self.yoko and self.map[cy+y][cx+x].state != "#"]
        return adj_lst

    def show_maze(self):
        color = {" ": "white", "#": "gray", "S": "#FFA07A", "G": "#87CEFA", "R": "#DBFAAF"}
        root = tk.Tk()
        canv = tk.Canvas(root, width=self.yoko*50, height=self.tate*50, bg="black")
        canv.pack()
        for y in range(self.tate):
            for x in range(self.yoko):
                canv.create_rectangle(x*50, y*50, x*50+50, y*50+50, fill=color[self.map[y][x].state])
                canv.create_text(x*50+25, y*50+25, text=self.map[y][x].dist, font=("Helvetica", 12))
        root.mainloop()
