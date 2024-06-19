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
class CellWall:
    i:int
    width:int
    height:int

@dataclass
class Stage:
    name:str
    tanks:list[Tank]
    enemytanks:list[Tank]
    enemies:int
    is_game_over:bool
    cells:list[Cell]
    win:bool

        

class Stages:
     def __init__(self) -> None:
        self.stage1=Stage(name="stage1",tanks=[Tank(28,265,vx=0,vy=0,direction="east",state="player",alive=True),Tank(225,183,vx=0,vy=0,direction="south",state="enemy",alive=True)],
                        enemytanks=[Tank(128,60,vx=0,vy=0,direction="south",state="enemy",alive=True),
                               Tank(45,183,vx=0,vy=0,direction="south",state="enemy",alive=True),
                               ],
                        enemies=3,
                        is_game_over=False,
                        cells=[Cell(18,8,width=DIM,height=DIM,state="home",black_screen=False),
                        Cell(18,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,8,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(18,12,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(1,2,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,3,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,11,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,13,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,14,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,15,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(4,1,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,1,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(6,1,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(4,4,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,4,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(6,4,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(7,4,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(8,4,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(9,4,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,7,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(6,8,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(7,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(10,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(11,8,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(4,12,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,12,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(6,12,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(7,12,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(8,12,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(9,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,11,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,12,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(4,16,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,16,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(6,16,width=DIM,height=DIM,state="halfbrick",black_screen=False),

                        Cell(7,1,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,1,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,1,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,2,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,2,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,3,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(9,13,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,14,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,14,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,16,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,16,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,16,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(10,4,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(11,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(10,12,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(11,12,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(15,3,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(12,6,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(13,6,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(12,10,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(13,10,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(15,13,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(14,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,1,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,16,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(10,1,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,2,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(11,1,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(10,13,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,14,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,15,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,16,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(11,16,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(12,4,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(12,12,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(8,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,9,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(10,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(10,9,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(17,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,6,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(17,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(16,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(16,8,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(16,9,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(15,1,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(15,2,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(15,14,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(15,15,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(15,16,width=DIM,height=DIM,state="brick",black_screen=False),

                        ]+[Cell(i, 0, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)]+\
                        [Cell(0, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(COL-1, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(i, ROW-1, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] + \
                        [Cell(i, ROW-2, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] +\
                        [Cell(i, ROW-3, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)],
                        win=False
                          )
        self.stage2=Stage(name="stage2",tanks=[Tank(175,285,vx=0,vy=0,direction="north",state="player",alive=True),Tank(73,70,vx=0,vy=0,direction="south",state="enemy",alive=True),\
                                ],
                        enemytanks=[Tank(240,145,vx=0,vy=0,direction="west",state="enemy",alive=True),
                               Tank(28,240,vx=0,vy=0,direction="east",state="enemy",alive=True),
                               Tank(230,80,vx=0,vy=0,direction="west",state="enemy",alive=True)
                               ],
                        enemies=4,
                        is_game_over=False,
                        cells=[Cell(18,8,width=DIM,height=DIM,state="home",black_screen=False),
                        Cell(18,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,8,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(17,9,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(18,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,4,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,13,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(3,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(4,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,3,width=DIM,height=DIM,state="water",black_screen=False),

                        Cell(1,6,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(2,6,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(1,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,7,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,4,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(1,3,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(2,5,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(1,11,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(2,11,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(3,11,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(3,10,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(4,6,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(5,6,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(3,13,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(3,14,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(2,14,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(3,15,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(3,16,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(2,16,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(1,16,width=DIM,height=DIM,state="halfbrick",black_screen=False),

                        Cell(7,1,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,2,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(8,1,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(9,1,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(8,2,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(8,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(8,4,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(8,5,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(8,6,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(18,14,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,16,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(17,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(17,16,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(16,16,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,13,width=DIM,height=DIM,state="stone",black_screen=False),

                        Cell(9,3,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(9,4,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(10,4,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(9,5,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(11,4,width=DIM,height=DIM,state="halfbrick",black_screen=False),

                        Cell(7,12,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(7,13,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(8,12,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(8,13,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,14,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(7,15,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(7,16,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(6,9,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(7,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(8,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(9,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(10,9,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(9,10,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(10,10,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(12,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(13,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(14,7,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(14,8,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(14,9,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(14,10,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(14,11,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(14,12,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(14,13,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(13,13,width=DIM,height=DIM,state="water",black_screen=False),
                        Cell(12,13,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(11,13,width=DIM,height=DIM,state="brick",black_screen=False),

                        Cell(17,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(18,3,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(16,3,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(17,4,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(17,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,5,width=DIM,height=DIM,state="forest",black_screen=False),
                        Cell(18,1,width=DIM,height=DIM,state="stone",black_screen=False),
                        Cell(18,6,width=DIM,height=DIM,state="forest",black_screen=False),

                        Cell(13,1,width=DIM,height=DIM,state="brick",black_screen=False),
                        Cell(13,2,width=DIM,height=DIM,state="halfbrick",black_screen=False),
                        Cell(11,14,width=DIM,height=DIM,state="northmirror",black_screen=False),
                        Cell(14,4,width=DIM,height=DIM,state="southmirror",black_screen=False),

                        ]+[Cell(i, 0, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)]+\
                        [Cell(0, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(COL-1, j, width=DIM, height=DIM, state="stone",black_screen=True) for j in range(ROW)] + \
                        [Cell(i, ROW-1, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] + \
                        [Cell(i, ROW-2, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)] +\
                        [Cell(i, ROW-3, width=DIM, height=DIM, state="stone",black_screen=True) for i in range(ROW)], 
                        win=False
                          )
        self.stages:list[Stage]=[self.stage1,self.stage2]




#