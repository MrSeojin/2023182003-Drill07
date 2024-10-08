from pico2d import*

class Grass:
    def __init__(self):
        # 모양없는 납작한 붕어빵의 납작한 초기 모습
        self.image = load_image('grass.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(400,30)
    pass



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

    running = True
    grass = Grass()

def update_world():
    grass.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    update_canvas()

open_canvas()

running = True
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()