import pyxel
import pyxelgrid
import random
from stage import Tank,Bullet,Cell,Stage1
from stage import TANK_WIDTH,TANK_LENGTH,DIM,ROW,COL



def is_disjoint(a: tuple[int,int]|tuple[float,float], b: tuple[int,int]|tuple[float,float]):
    assert(a[0] <= a[1]) and (b[0] <= b[1])
    return (a[0] > b[1]) or (b[0] > a[1])
   
def intersects(a: tuple[int,int]|tuple[float,float], b: tuple[int,int]|tuple[float,float]):
    return not is_disjoint(a,b)

class MyGame(pyxelgrid.PyxelGrid[int]):

    def __init__(self):
        super().__init__(r=ROW, c=COL, dim=DIM)  
    def init(self) -> None:
        # called once at initialization time
        self.gamestate=Stage1()
        self.tanks_appended=0
        self.tanks:list[Tank]=self.gamestate.tanks
        self.Cell:list[Cell]=self.gamestate.cells
        for cell in self.Cell:
            assert 0<=cell.i<self.r and 0<=cell.j<self.c, f"{cell} is out of bounds"
        self.bullets:list[Bullet]=[]
        self.direction=["north","south","west","east"]
        self.vy=[-1,1,0,0]
        self.vx=[0,0,-1,1]
        self.bulletspeed=3
        self.bullet_speed_y=[-1*self.bulletspeed,1*self.bulletspeed,0,0]
        self.bullet_speed_x=[0,0,-1*self.bulletspeed,1*self.bulletspeed]
        self.black_screen=[Cell for Cell in self.Cell if Cell.black_screen]
        
        self.movement=1
        self.cooldown=30
        self.recent_button: int = 0  
        self.recent_button_timer: int = 0
        self.bullet_per_every_frame=10
        self.dimension=self.dim
        self.bullet_radius=2
        pyxel.load("test.pyxres")
        pyxel.mouse(visible=True)
        
    
    def tank_cell_collision(self,tank:Tank):
        Cell=self.Cell
        for stone in Cell:
            if stone.state is not None and stone.state!="mirror":
                i,j=stone.i,stone.j
                start_height,end_height=((i)*self.dim),((i+1)*self.dim)
                
                start_width,end_width=((j)*self.dim),((j+1)*self.dim)
                if tank.direction in ["north", "south"]:
                    if intersects((start_width,end_width), ((tank.x),(tank.x+TANK_WIDTH-1))) \
                        and intersects((start_height,end_height), ((tank.y),(tank.y+TANK_LENGTH-1))):
                        return True
                elif tank.direction in ["east", "west"]:
                    if intersects((start_width,end_width), ((tank.x),(tank.x+TANK_LENGTH-1))) \
                        and intersects((start_height,end_height), ((tank.y),(tank.y+TANK_WIDTH-1))):
                        
                        return True
                else:
                    raise RuntimeError
        return False
    
    def tank_inbounds(self,tank:Tank)->bool:
        return not ((tank.x>=self.width-16 or tank.y>=self.height-16 or tank.x<=0 or tank.y<=0) or self.tank_cell_collision(tank))
    
            
        
    def move_tank(self,direction:str,tank:Tank):
        vy=self.vy
        vx=self.vx
        tank.direction=direction
        tank.vy=vy[self.direction.index(tank.direction)]
        tank.vx=vx[self.direction.index(tank.direction)]
        if tank.state=="player":
            self.movement=1
            tank.y+=tank.vy
            tank.x+=tank.vx
        if tank.state=="enemy":
            self.movement=4
            for _ in range(self.movement):
                tank.y+=tank.vy
                tank.x+=tank.vx
        
        if not self.tank_inbounds(tank):
            tank.y-=tank.vy*self.movement
            tank.x-=tank.vx*self.movement
        
    def bullet_collision(self,bullet:Bullet)->bool|tuple[bool,tuple[int,int]]:
        Cell=self.Cell
        for material in Cell:
            if material.state!="northmirror" and material.state!="southmirror" and material.state!="water" and material.state is not None:
                i,j=material.i,material.j
                start_height,end_height=((i)*self.dim),((i+1)*self.dim)
                start_width,end_width=((j)*self.dim),((j+1)*self.dim)
                
                if start_width<=bullet.x<=end_width and start_height<=bullet.y<=end_height:
                    return True,(i,j)
        return False
    
    def check_bullet_to_bullet_collision(self,bullet:Bullet):
        for bullets in self.bullets:
            if bullets!=bullet:
                if intersects((bullet.x-self.bullet_radius+self.bulletspeed,bullet.x+self.bullet_radius+self.bulletspeed),
                              (bullets.x-self.bullet_radius+self.bulletspeed,bullets.x+self.bullet_radius+self.bulletspeed)) \
                              and intersects((bullet.y-self.bullet_radius+self.bulletspeed,bullet.y+self.bullet_radius+self.bulletspeed),
                              (bullets.y-self.bullet_radius+self.bulletspeed,bullets.y+self.bullet_radius+self.bulletspeed)):

                    self.bullets.remove(bullet)
                    self.bullets.remove(bullets)

    def mirror_bounds(self,x1:int,x2:int,y1:int,y2:float,x:float,y:float)->bool:
        return min(x1,x2)<=x<=max(x1,x2) and min(y1,y2)<=y<=max(y1,y2)
                    
    def mirror_bullet_collision(self,bullet:Bullet)->None:
        Cell=self.Cell
        vx,vy=bullet.vx,bullet.vy
        direction_index=-1
        if vx!=0:
            direction_index=self.bullet_speed_x.index(vx)
        if vy!=0:
            direction_index=self.bullet_speed_y.index(vy)
        assert direction_index>=0
        bullet_direction=self.direction[direction_index]
        for material in Cell:
            if material.state=="northmirror":
                change_of_dir:dict[str,str]={"north":"east","east":"north","south":"west","west":"south"}
                new_direction=change_of_dir[bullet_direction]
                direction_index = self.direction.index(new_direction)
                i,j=material.i,material.j
                start_height,end_height=((i)*self.dim),((i+1)*self.dim)
                start_width,end_width=((j)*self.dim),((j+1)*self.dim)
                if self.mirror_bounds(start_width,end_width,start_height,end_height,bullet.x,bullet.y):
                    bullet.vy = self.bullet_speed_y[direction_index]
                    bullet.vx = self.bullet_speed_x[direction_index]
            elif material.state=="southmirror":
                change_of_dir:dict[str,str]={"east":"south","south":"east","west":"north","north":"west"}
                new_direction=change_of_dir[bullet_direction]
                direction_index = self.direction.index(new_direction)
                i,j=material.i,material.j
                start_height,end_height=((i)*self.dim),((i+1)*self.dim)
                start_width,end_width=((j)*self.dim),((j+1)*self.dim)
                if self.mirror_bounds(start_width,end_width,start_height,end_height,bullet.x,bullet.y):
                    bullet.vy = self.bullet_speed_y[direction_index]
                    bullet.vx = self.bullet_speed_x[direction_index]
       
    def tank_bullet_collision(self,bullet:Bullet):
        tanks=self.tanks
        origin=bullet.origin
        for tank in tanks:
            start_height,end_height=tank.y,tank.y+TANK_LENGTH-1
            start_width,end_width=tank.x,tank.x+TANK_WIDTH-1
            if start_width<=bullet.x<=end_width and start_height<=bullet.y<=end_height:
                if origin=="player" and tank.state=="enemy" and tank.alive:
                    tank.alive=False
                    self.gamestate.enemy-=1
                    if self.bullets:
                        self.bullets.remove(bullet)
                elif origin=="enemy" and tank.state=="player":
                    tank.alive=False
                    self.gamestate.is_game_over=True
                    if self.bullets:
                        self.bullets.remove(bullet)
        
                
    def shoot_bullets(self,tank:Tank)->None:
        x = tank.x
        y = tank.y
        direction_index = self.direction.index(tank.direction)
        bullet_vy = self.bullet_speed_y[direction_index]
        bullet_vx = self.bullet_speed_x[direction_index]
        if bullet_vy != 0:
            x += 8
        if bullet_vx != 0:
            y += 8 
        if not any(bullet.origin== "player" for bullet in self.bullets) and tank.state=="player":
            bullet=Bullet(x,y,bullet_vx,bullet_vy,tank.state)
            if bullet.origin=="player":
                pyxel.play(0,0)
            self.bullets.append(bullet)
        elif tank.state=="enemy":
            bullet=Bullet(x,y,bullet_vx,bullet_vy,tank.state)
            self.bullets.append(bullet)
    def update(self) -> None:
        DIRECTION_KEYS = {
        pyxel.KEY_W: "north",
        pyxel.KEY_A: "west",
        pyxel.KEY_S: "south",
        pyxel.KEY_D: "east",
        }
        
        if not self.gamestate.is_game_over:
            if pyxel.frame_count!=0 and pyxel.frame_count%150==0 and self.tanks_appended<len(self.gamestate.enemytanks):
                self.gamestate.tanks.append(self.gamestate.enemytanks[self.tanks_appended])
                self.tanks_appended+=1
            for tank in self.tanks:
                if tank.state=="player" and tank.alive:
                    if self.recent_button_timer > 0:
                        self.recent_button_timer -= 1
                    if pyxel.btnp(pyxel.KEY_W,hold=1,repeat=1):
                        if self.recent_button == pyxel.KEY_W or self.recent_button_timer == 0:
                            self.recent_button = pyxel.KEY_W
                            self.move_tank(DIRECTION_KEYS[pyxel.KEY_W],tank)
                        if self.recent_button_timer == 0:
                            self.recent_button_timer = self.cooldown
                    elif pyxel.btnp(pyxel.KEY_S,hold=1,repeat=1):
                        if self.recent_button == pyxel.KEY_S or self.recent_button_timer == 0:
                            self.recent_button = pyxel.KEY_S
                            self.move_tank(DIRECTION_KEYS[pyxel.KEY_S],tank)

                        if self.recent_button_timer == 0:
                            self.recent_button_timer = self.cooldown
        
                    elif pyxel.btnp(pyxel.KEY_A,hold=1,repeat=1):
                        if self.recent_button == pyxel.KEY_A or self.recent_button_timer == 0:
                            self.recent_button = pyxel.KEY_A
                            self.move_tank(DIRECTION_KEYS[pyxel.KEY_A],tank)

                        if self.recent_button_timer == 0:
                            self.recent_button_timer = self.cooldown
                    elif pyxel.btnp(pyxel.KEY_D,hold=1,repeat=1):
                        if self.recent_button == pyxel.KEY_D or self.recent_button_timer == 0:
                            self.recent_button = pyxel.KEY_D
                            self.move_tank(DIRECTION_KEYS[pyxel.KEY_D],tank)
                        if self.recent_button_timer == 0:
                            self.recent_button_timer = self.cooldown
                    
                    if pyxel.btnp(pyxel.KEY_SPACE,hold=1,repeat=self.bullet_per_every_frame):
                        self.shoot_bullets(tank)
                if tank.state=="enemy" and tank.alive:
                    choices = ["direction", "move","fire"]
                    weights = [0.33, 0.33,0.33]
                    direction=self.direction
                    if pyxel.frame_count%20==0:
                        result = random.choices(choices, weights=weights, k=1)[0]
                        if result==choices[0]:
                            index=random.randint(0,3)
                            tank.direction=direction[index]
                        if result==choices[1]:
                            for _ in range(3):
                                self.move_tank(tank.direction,tank)
                        if result==choices[2]:
                            self.shoot_bullets(tank)
            
                
            for bullet in self.bullets:
                self.check_bullet_to_bullet_collision(bullet)
                if not self.bullet_collision(bullet):
                    bullet.x+=bullet.vx
                    bullet.y+=bullet.vy
                elif self.bullet_collision(bullet):
                    result=self.bullet_collision(bullet)
                    assert  isinstance (result,tuple)
                    coordinate=result[1]
                    for cell in self.Cell:
                        if cell.i==coordinate[0] and cell.j==coordinate[1] and cell.state=="brick":
                            cell.state="halfbrick"
                        elif cell.i==coordinate[0] and cell.j==coordinate[1] and cell.state=="halfbrick":
                            cell.state=None
                    if self.bullets:
                        self.bullets.remove(bullet)
                self.tank_bullet_collision(bullet)
                self.mirror_bullet_collision(bullet)
            
            if self.gamestate.enemy==0:
                self.gamestate.is_game_over=True
            
            
    def draw_cell(self, i: int, j: int, x: int, y: int) -> None:
        for stone in self.Cell:
            if stone.i==i and stone.j==j and stone.state=="stone":
                pyxel.blt(x,y,0,32,48,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone.state=="brick":
                pyxel.blt(x,y,0,32,32,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone.state=="halfbrick":
                pyxel.blt(x,y,0,48,32,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone.state=="northmirror":
                pyxel.blt(x,y,0,0,48,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone.state=="southmirror":
                pyxel.blt(x,y,0,16,48,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone.state=="water":
                pyxel.blt(x,y,0,0,64,self.dim,self.dim)
            if stone.i==i and stone.j==j and stone in self.black_screen:
                pyxel.rect(x,y,16,16,13)
        pyxel.blt(305,100,0,32,64,16,16)
        pyxel.blt(289,100,0,32,64,16,16)
        pyxel.blt(273,100,0,32,64,16,16)

    def pre_draw_grid(self) -> None:
        pyxel.cls(0)
        
        bullets=self.bullets
        for bullet in bullets:
            if bullet.origin=="player":
                pyxel.circ(bullet.x,bullet.y,self.bullet_radius,1)
            elif bullet.origin=="enemy":
                pyxel.circ(bullet.x,bullet.y,self.bullet_radius,2)
        for tank in self.tanks:
            if tank.state=="player" and tank.alive:
                if tank.direction=="north":
                    pyxel.blt(tank.x,tank.y,0,0,0,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="south":
                    pyxel.blt(tank.x,tank.y,0,16,0,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="east":
                    pyxel.blt(tank.x,tank.y,0,32,0,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="west":
                    pyxel.blt(tank.x,tank.y,0,48,0,w=TANK_WIDTH,h=TANK_LENGTH)
            elif tank.state=="enemy" and tank.alive:
                if tank.direction=="north":
                    pyxel.blt(tank.x,tank.y,0,0,16,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="south":
                    pyxel.blt(tank.x,tank.y,0,16,16,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="east":
                    pyxel.blt(tank.x,tank.y,0,32,16,w=TANK_WIDTH,h=TANK_LENGTH)
                elif tank.direction=="west":
                    pyxel.blt(tank.x,tank.y,0,48,16,w=TANK_WIDTH,h=TANK_LENGTH)
            elif tank.state=="player" and not tank.alive:
                pyxel.blt(tank.x,tank.y,0,0,32,w=TANK_WIDTH,h=TANK_LENGTH)
            elif tank.state=="enemy" and not tank.alive:
                pyxel.blt(tank.x,tank.y,0,16,32,w=TANK_WIDTH,h=TANK_LENGTH)
        
    def post_draw_grid(self) -> None:
        if self.gamestate.is_game_over:
            pyxel.text(100, 100, "Game Over!", pyxel.frame_count % 16)
        
    

my_game = MyGame()
my_game.run(title="Battle City", fps=60)
# The keyword arguments are passed directly to pyxel.init




