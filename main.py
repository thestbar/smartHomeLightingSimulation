import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Smart Lighting 2D Simulation")
logo = pygame.image.load("images/logo.png")

background = pygame.image.load("images/background.png")
walk_right = [pygame.image.load('animation/right0.png'), pygame.image.load('animation/right1.png'), pygame.image.load('animation/right2.png'),
             pygame.image.load('animation/right3.png'), pygame.image.load('animation/right4.png'), pygame.image.load('animation/right5.png'),
             pygame.image.load('animation/right6.png'), pygame.image.load('animation/right7.png')]
walk_left = [pygame.image.load('animation/left0.png'), pygame.image.load('animation/left1.png'), pygame.image.load('animation/left2.png'),
             pygame.image.load('animation/left3.png'), pygame.image.load('animation/left4.png'), pygame.image.load('animation/left5.png'),
             pygame.image.load('animation/left6.png'), pygame.image.load('animation/left7.png')]
walk_front = [pygame.image.load('animation/front0.png'), pygame.image.load('animation/front1.png'), pygame.image.load('animation/front2.png'),
              pygame.image.load('animation/front3.png'), pygame.image.load('animation/front4.png'), pygame.image.load('animation/front5.png'),
              pygame.image.load('animation/front6.png'), pygame.image.load('animation/front7.png')]
walk_back = [pygame.image.load('animation/back0.png'), pygame.image.load('animation/back1.png'), pygame.image.load('animation/back2.png'),
             pygame.image.load('animation/back3.png'), pygame.image.load('animation/back4.png'), pygame.image.load('animation/back5.png'),
             pygame.image.load('animation/back6.png'), pygame.image.load('animation/back7.png')]

character = pygame.image.load('animation/front0.png')

clock = pygame.time.Clock()


class Home(object):
    def __init__(self):
        self.led_room = False
        self.led_bathroom = False
        self.led_bedroom = False
        self.led_corridor = False
        self.motion_sensor0 = False
        self.motion_sensor1 = False
        self.light_sensor0 = False
        self.light_sensor1 = False
        self.is_empty = True
        self.control_panel = False
        self.noone_in_bedroom = True

        # home walls' hit boxes
        self.left_wall_hitbox = (90, 40, 20, 470)
        self.right_wall_hitbox = (690, 40, 20, 470)
        self.top_wall_hitbox = (90, 40, 620, 20)
        self.down_wall_hitbox0 = (90, 490, 270, 20)
        self.down_wall_hitbox1 = (440, 490, 270, 20)
        self.inside_wall_hitbox0 = (90, 240, 285, 20)
        self.inside_wall_hitbox1 = (425, 240, 285, 20)
        self.inside_wall_hitbox2 = (365, 40, 10, 70)
        self.inside_wall_hitbox3 = (425, 40, 10, 70)
        self.inside_wall_hitbox4 = (365, 190, 10, 70)
        self.inside_wall_hitbox5 = (425, 190, 10, 70)

        self.home_hitboxes = [self.left_wall_hitbox, self.right_wall_hitbox, self.top_wall_hitbox,
                              self.right_wall_hitbox, self.down_wall_hitbox0, self.down_wall_hitbox1,
                              self.inside_wall_hitbox0, self.inside_wall_hitbox1, self.inside_wall_hitbox2,
                              self.inside_wall_hitbox3, self.inside_wall_hitbox4, self.inside_wall_hitbox5]

        # door motion sensor
        self.motion_sensor0_hitbox = (360, 490, 80, 10)

        #bed room motion sensor
        self.motion_sensor1_hitbox = (434, 95, 250, 130)

        # home rooms
        self.room_light = (103, 253, 595, 245)
        self.corridor_light = (373, 53, 55, 200)

        self.bathroom_light = (103, 53, 265, 195)
        self.bathcor = (368, 115, 5, 70)
        self.bedcor = (428, 115, 5, 70)

        self.bedroom_light = (433, 53, 265, 195)

        # home buttons
        self.switch0 = (285, 253, 23, 5)
        self.switch1 = (365, 201, 3, 15)
        self.switch2 = (433, 201, 3, 15)

        # switches hitboxes
        self.s0_hitbox = (270, 253, 50, 50)
        self.s1_hitbox = (337, 190, 30, 40)
        self.s2_hitbox = (433, 190, 30, 40)

    def control_panel_menu(self, win):
        pygame.draw.rect(win, (0, 0, 0), (200, 150, 400, 300), 0)
        font0 = pygame.font.SysFont('Arial', 45)
        font1 = pygame.font.SysFont('Arial', 40)
        font2 = pygame.font.SysFont('Arial', 30)
        window.blit(font0.render('Control Panel', True, (255, 0, 0)), (220, 150))
        window.blit(font1.render('Main Room', True, (255, 255, 255)), (220, 222))
        window.blit(font1.render('Corridor', True, (255, 255, 255)), (220, 274))
        window.blit(font1.render('Bedroom', True, (255, 255, 255)), (220, 326))
        window.blit(font1.render('Bathroom', True, (255, 255, 255)), (220, 378))

        pygame.draw.rect(win, (255, 255, 100), (500, 222, 50, 50), 0)
        pygame.draw.rect(win, (255, 255, 100), (500, 274, 50, 50), 0)
        pygame.draw.rect(win, (255, 255, 100), (500, 326, 50, 50), 0)
        pygame.draw.rect(win, (255, 255, 100), (500, 378, 50, 50), 0)

        if home.led_room:
            window.blit(font2.render('ON', True, (0, 0, 0)), (505, 228))
        else:
            window.blit(font2.render('OFF', True, (0, 0, 0)), (500, 228))
        if home.led_corridor:
            window.blit(font2.render('ON', True, (0, 0, 0)), (505, 280))
        else:
            window.blit(font2.render('OFF', True, (0, 0, 0)), (500, 280))
        if home.led_bedroom:
            window.blit(font2.render('ON', True, (0, 0, 0)), (505, 332))
        else:
            window.blit(font2.render('OFF', True, (0, 0, 0)), (500, 332))
        if home.led_bathroom:
            window.blit(font2.render('ON', True, (0, 0, 0)), (505, 384))
        else:
            window.blit(font2.render('OFF', True, (0, 0, 0)), (500, 384))
        mouse = pygame.mouse.get_pos()
        # print(mouse)
        if keys[pygame.K_ESCAPE]:
            home.control_panel = not home.control_panel
        if 500 < mouse[0] < 550:
            if 220 < mouse[1] < 275 and keys[pygame.K_SPACE]:
                home.led_room = not home.led_room
                pygame.time.delay(100)
            elif 275 < mouse[1] < 325 and keys[pygame.K_SPACE]:
                home.led_corridor = not home.led_corridor
                pygame.time.delay(100)
            elif 325 < mouse[1] < 378 and keys[pygame.K_SPACE]:
                home.led_bedroom = not home.led_bedroom
                pygame.time.delay(100)
            elif 378 < mouse[1] < 430 and keys[pygame.K_SPACE]:
                home.led_bathroom = not home.led_bathroom
                pygame.time.delay(100)

    def draw_switches(self, win):
        pygame.draw.rect(win, (138, 43, 226), self.switch0, 0)
        pygame.draw.rect(win, (138, 43, 226), self.switch1, 0)
        pygame.draw.rect(win, (138, 43, 226), self.switch2, 0)

    def enable_room_light(self, win):
        pygame.draw.rect(win, (255, 255, 200), self.room_light, 0)

    def enable_corridor_light(self, win):
        pygame.draw.rect(win, (255, 255, 200), self.corridor_light, 0)
        pygame.draw.rect(win, (255, 255, 200), self.bathcor, 0)
        pygame.draw.rect(win, (255, 255, 200), self.bedcor, 0)

    def enable_bathroom_light(self, win):
        pygame.draw.rect(win, (255, 255, 200), self.bathroom_light, 0)

    def enable_bedroom_light(self, win):
        pygame.draw.rect(win, (255, 255, 200), self.bedroom_light, 0)

    def disable_room_light(self, win):
        pygame.draw.rect(win, (169, 169, 169), self.room_light, 0)

    def disable_corridor_light(self, win):
        pygame.draw.rect(win, (169, 169, 169), self.corridor_light, 0)
        pygame.draw.rect(win, (169, 169, 169), self.bathcor, 0)
        pygame.draw.rect(win, (169, 169, 169), self.bedcor, 0)

    def disable_bathroom_light(self, win):
        pygame.draw.rect(win, (169, 169, 169), self.bathroom_light, 0)

    def disable_bedroom_light(self, win):
        pygame.draw.rect(win, (169, 169, 169), self.bedroom_light, 0)

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), self.left_wall_hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.right_wall_hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.top_wall_hitbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.down_wall_hitbox0, 2)
        pygame.draw.rect(win, (255, 0, 0), self.down_wall_hitbox1, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox0, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox1, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox2, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox3, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox4, 2)
        pygame.draw.rect(win, (255, 0, 0), self.inside_wall_hitbox5, 2)

        pygame.draw.rect(win, (200, 0, 255), self.motion_sensor0_hitbox, 2)
        pygame.draw.rect(win, (200, 0, 255), self.motion_sensor1_hitbox, 2)

        pygame.draw.rect(win, (0, 0, 255), self.s0_hitbox, 2)
        pygame.draw.rect(win, (0, 0, 255), self.s1_hitbox, 2)
        pygame.draw.rect(win, (0, 0, 255), self.s2_hitbox, 2)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 2
        self.left = False
        self.right = False
        self.top = False
        self.down = False
        self.walk_count = 0
        self.hitbox = (self.x + 10, self.y, 30, 60)
        self.can_move = True

    def draw(self, win):
        if self.walk_count + 1 >= 24:
            self.walk_count = 0
        if self.left:
            win.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.top:
            win.blit(walk_back[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.down:
            win.blit(walk_front[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(character, (self.x, self.y))
        self.hitbox = (self.x + 10, self.y, 30, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


def redraw_game_window():
    window.blit(background, (0, 0))

    if home.led_room:
        home.enable_room_light(window)
    else:
        home.disable_room_light(window)

    if home.led_corridor:
        home.enable_corridor_light(window)
    else:
        home.disable_corridor_light(window)

    if home.led_bathroom:
        home.enable_bathroom_light(window)
    else:
        home.disable_bathroom_light(window)

    if home.led_bedroom:
        home.enable_bedroom_light(window)
    else:
        home.disable_bedroom_light(window)

    home.draw_switches(window)

    home.draw(window)
    # always draw the character last so he is on top of the screen
    player.draw(window)

    if home.control_panel:
        home.control_panel_menu(window)

    pygame.display.update()


player = Player(260, 530, 48, 64)
home = Home()
button_delay = 0
# mainloop
run = True
while run:
    clock.tick(48)

    if button_delay > 0:
        button_delay += 1
    if button_delay > 20:
        button_delay = 0

    for hitbox in home.home_hitboxes:
        if player.hitbox[1] < hitbox[1] + hitbox[3] and player.hitbox[1] + player.hitbox[3] > hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > hitbox[0] and player.hitbox[0] < hitbox[0] + hitbox[2]:
                player.can_move = False

    if not player.can_move:
        if player.top:
            player.y += player.velocity
        elif player.down:
            player.y -= player.velocity
        elif player.left:
            player.x += player.velocity
        else:
            player.x -= player.velocity
        player.can_move = True

    if home.is_empty:
        if player.hitbox[1] < home.motion_sensor0_hitbox[1] + home.motion_sensor0_hitbox[3] and player.hitbox[1] + player.hitbox[3] > home.motion_sensor0_hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > home.motion_sensor0_hitbox[0] and player.hitbox[0] < home.motion_sensor0_hitbox[0] + home.motion_sensor0_hitbox[2]:
                # print("someone entered the house")
                home.is_empty = False
                home.led_room = True
                home.led_corridor = True

    if home.noone_in_bedroom:
        if player.hitbox[1] < home.motion_sensor1_hitbox[1] + home.motion_sensor1_hitbox[3] and player.hitbox[1] + player.hitbox[3] > home.motion_sensor1_hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > home.motion_sensor1_hitbox[0] and player.hitbox[0] < home.motion_sensor1_hitbox[0] + home.motion_sensor1_hitbox[2]:
                print("someone entered the bedroom")
                home.led_bedroom = True
                # FTIAKSE TIN PATENTA ME TO DWMATIO
                home.noone_in_bedroom = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if player.hitbox[1] < home.s1_hitbox[1] + home.s1_hitbox[3] and player.hitbox[1] + player.hitbox[3] > home.s1_hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > home.s1_hitbox[0] and player.hitbox[0] < home.s1_hitbox[0] + home.s1_hitbox[2]:
            # print("bathroom")
            if keys[pygame.K_SPACE] and button_delay == 0:
                home.led_bathroom = not home.led_bathroom
                button_delay = 1

    if player.hitbox[1] < home.s0_hitbox[1] + home.s0_hitbox[3] and player.hitbox[1] + player.hitbox[3] > home.s0_hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > home.s0_hitbox[0] and player.hitbox[0] < home.s0_hitbox[0] + home.s0_hitbox[2]:
            if keys[pygame.K_SPACE] and button_delay == 0:
                # print("control panel")
                home.control_panel = True

    if player.hitbox[1] < home.s2_hitbox[1] + home.s2_hitbox[3] and player.hitbox[1] + player.hitbox[3] > home.s2_hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > home.s2_hitbox[0] and player.hitbox[0] < home.s2_hitbox[0] + home.s2_hitbox[2]:
            # print("bedroom")
            if keys[pygame.K_SPACE] and button_delay == 0:
                home.led_bedroom = not home.led_bedroom
                button_delay = 1

    if keys[pygame.K_LEFT] and player.x > 0 and player.can_move:
        player.x -= player.velocity
        player.left = True
        player.right = False
        player.top = False
        player.down = False
    elif keys[pygame.K_RIGHT] and player.x < (window_width - player.width) and player.can_move:
        player.x += player.velocity
        player.left = False
        player.right = True
        player.top = False
        player.down = False
    elif keys[pygame.K_UP] and player.y > 0 and player.can_move:
        player.y -= player.velocity
        player.left = False
        player.right = False
        player.top = True
        player.down = False
    elif keys[pygame.K_DOWN] and player.y < (window_height - player.height) and player.can_move:
        player.y += player.velocity
        player.left = False
        player.right = False
        player.top = False
        player.down = True
    else:
        player.left = False
        player.right = False
        player.top = False
        player.down = False
        player.walk_count = 0

    redraw_game_window()

pygame.quit()
