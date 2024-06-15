from dataclasses import dataclass
TANK_WIDTH=16
TANK_LENGTH=16
COOLDOWN = 10
ROW=20
COL=20
DIM=16
@dataclass
class Tank:
    x:float
    y:float
    direction:str
    vx:float
    vy:float
    state:str
    alive:bool
@dataclass
class Bullet:
    x:float
    y:float
    vx:int
    vy:int
    origin:str
@dataclass
class Cell:
    i:int
    j:int
    width:int
    height:int
    state:str|None
    black_screen:bool


@dataclass
class PyxelGrid:
    rows:int
    columns:int
    

@dataclass
class CellWall:
    i:int
    width:int
    height:int

class Stage1:
    def __init__(self) -> None:
        self.tanks:list[Tank]=[Tank(120,120,vx=0,vy=0,direction="north",state="player",alive=True),Tank(50,50,vx=0,vy=0,direction="north",state="enemy",alive=True)]
        self.enemytanks:list[Tank]=[Tank(200,200,vx=0,vy=0,direction="north",state="enemy",alive=True),
                               Tank(120,120,vx=0,vy=0,direction="north",state="enemy",alive=True),
                               ]
        
        self.lives=2
        self.enemy=1+len(self.enemytanks)
        self.is_game_over:bool=False
        self.cells:list[Cell]=[Cell(10,10,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(11,10,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(11,12,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,14,width=DIM,height=DIM,state="northmirror",black_screen=False),
                        Cell(5,5,width=DIM,height=DIM,state="southmirror",black_screen=False),
                        Cell(5,8,width=DIM,height=DIM,state="water",black_screen=False)
                        ]+[Cell(i, 0, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(20)]+\
                        [Cell(0, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(20)] + \
                        [Cell(COL-1, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(20)] + \
                        [Cell(i, ROW-1, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(20)] + \
                        [Cell(i, ROW-2, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(20)] +\
                        [Cell(i, ROW-3, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(20)] 
        
        self.win:bool=False


        

#