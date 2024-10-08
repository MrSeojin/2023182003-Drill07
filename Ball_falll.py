from pico2d import*
import random

class Grass:
    def __init__(self):
        # 모양없는 납작한 붕어빵의 납작한 초기 모습
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.dir = 1
        self.image = load_image('animation_sheet.png')
    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, self.dir*100, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(20, 770), 599
        self.speed = random.randint(1, 5)
    def update(self):
        self.y -= self.speed
        if self.y <= 70:
            self.y = 70
    def draw(self):
        self.image.draw(self.x, self.y)

class SmallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(10, 780), 599
        self.speed = random.randint(1, 5)
    def update(self):
        self.y -= self.speed
        if self.y <= 60:
            self.y = 60
    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global s_balls
    global b_balls
    global world

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team
    num = random.randint(1,19)
    s_balls = [SmallBall() for i in range(num)]
    b_balls = [BigBall() for i in range(20 - num)]
    world += s_balls
    world += b_balls

def update_world():
    grass.update()
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()