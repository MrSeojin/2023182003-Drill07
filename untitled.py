from pico2d import*

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
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, self.dir*100, 100, 100, self.x, self.y)

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
    global boy

    running = True
    grass = Grass()
    boy = Boy()

def update_world():
    grass.update()
    boy.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()