# Import libraries
import pygame

# Initilizing the pygame
pygame.init()

# inilize pygame music
pygame.mixer.init()

# Creating game window
scr_width = 600
scr_height = 600
GameWindow = pygame.display.set_mode((scr_width,scr_height))

# set title
pygame.display.set_caption("My Tic-Tac-Toe")
pygame.display.update()

# Color-RGB
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)

# Create clock for game
clock = pygame.time.Clock()
FPS = 30

# Images
x = pygame.image.load("X.png")                          # For printing X
x = pygame.transform.scale(x,(70,70)).convert_alpha()

y = pygame.image.load("Y.png")                          # for printing 0
y = pygame.transform.scale(y,(70,70)).convert_alpha()

# Background images

HomeImg = pygame.image.load("Home.png")
HomeImg = pygame.transform.scale(HomeImg,(scr_width,scr_height)).convert_alpha()

Gameover = pygame.image.load("gameover.jpeg")
Gameover = pygame.transform.scale(Gameover,(scr_width,scr_height)).convert_alpha()

msgbg  = pygame.image.load("MsgIntr.jpg")
msgbg  = pygame.transform.scale(msgbg,(scr_width,scr_height)).convert_alpha()

board = pygame.image.load("backgroung.jpeg")
board = pygame.transform.scale(board,(scr_width,scr_height)).convert_alpha()


# fxn to print text on screen

font = pygame.font.SysFont(None,30)
def text_on_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    GameWindow.blit(screen_text,(x,y))

# Fxn to show Instruction of Game on screen

def Msg_Instr():
    game_exit = False
    while not game_exit:
        # GameWindow.fill(blue)
        GameWindow.blit(msgbg,(0,0))
        text_on_screen("Press space ", white, 230, 580)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GameLoop()
            pygame.display.update()
            clock.tick(FPS)

# Welcome screen
def Welcome():
    game_exit = False
    pygame.mixer.music.load("MusicBg.mp3")
    pygame.mixer.music.play()
    while not game_exit:
        GameWindow.fill(blue)
        GameWindow.blit(HomeImg,(0,0))
        text_on_screen("Press space ", white,230, 580)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # By pressing space
                    Msg_Instr()
        pygame.display.update()
        clock.tick(FPS)

# Blit X and Y as Enter any key by players

def print(playerA,playerB):
    lst_pos = [(195, 195), (265, 195), (335, 195), (195, 265), (265, 265), (335, 265), (195, 335), (265, 335),
               (335, 335)]
    for pos in playerA:
        GameWindow.blit(x,lst_pos[pos])
    for pos in playerB:
        GameWindow.blit(y,lst_pos[pos])

# Game Loop
def GameLoop():

    # Global variables
    game_exit = False
    game_over = False
    # start = True
    playerA = []
    playerB = []
    TurnofA = True
    TurnofB = False
    win = [(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
    winA = False
    winB = False
    curr_click_a = -1
    curr_click_b = -1

    # play music
    pygame.mixer.music.load("Run.mp3")
    pygame.mixer.music.play()

    while not game_exit:

        if game_over:
            GameWindow.fill(black)
            GameWindow.blit(Gameover,(0,0))
            if winA:
                text_on_screen("\t\t Winner-A \t\t",white,230,120)
                text_on_screen("Press Enter to continue",white,190,550)
            elif winB :
                text_on_screen("\t\t Winner-B \t\t",white,230,120)
                text_on_screen("Press Enter to continue",white,190,550)
            else:
                text_on_screen("\t\t RESET \t\t", white, 230, 120)
                text_on_screen("Press Enter to continue",white,190,550)
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # restart by pressing enter
                        # Welcome()
                        GameLoop()
        else:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    # start = False
                    # Working / functionality  of each key
                    if event.key == pygame.K_0 and TurnofA:
                        if 0 not in playerA and 0 not in playerB:
                            playerA.append(0)
                            curr_click_a = 0
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_0 and TurnofB:
                        if 0 not in playerB and 0 not in playerA:
                            playerB.append(0)
                            curr_click_b = 0
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_1 and TurnofA:
                        if 1 not in playerA and 1 not in playerB:
                            playerA.append(1)
                            curr_click_a = 1
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_1 and TurnofB:
                        if 1 not in playerB and 1 not in playerA:
                            playerB.append(1)
                            curr_click_b = 1
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_2 and TurnofA:
                        if 2 not in playerA and 2 not in playerB:
                            playerA.append(2)
                            curr_click_a = 2
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_2 and TurnofB:
                        if 2 not in playerB and 2 not in playerA:
                            playerB.append(2)
                            curr_click_b = 2
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_3 and TurnofA:
                        if 3 not in playerA and 3 not in playerB:
                            playerA.append(3)
                            curr_click_a = 3
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_3 and TurnofB:
                        if 3 not in playerB and 3 not in playerA:
                            playerB.append(3)
                            curr_click_b = 3
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_4 and TurnofA:
                        if 4 not in playerA and 4 not in playerB:
                            playerA.append(4)
                            curr_click_a = 4
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_4 and TurnofB:
                        if 4 not in playerB and 4 not in playerA:
                            playerB.append(4)
                            curr_click_b = 4
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_5 and TurnofA:
                        if 5 not in playerA and 5 not in playerB:
                            playerA.append(5)
                            curr_click_a = 5
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_5 and TurnofB:
                        if 5 not in playerB and 5 not in playerA:
                            playerB.append(5)
                            curr_click_b = 5
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_6 and TurnofA:
                        if 6 not in playerA and 6 not in playerB:
                            playerA.append(6)
                            curr_click_a = 6
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_6 and TurnofB:
                        if 6 not in playerB and 6 not in playerA:
                            playerB.append(6)
                            curr_click_b = 6
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_7 and TurnofA:
                        if 7 not in playerA and 7 not in playerB:
                            playerA.append(7)
                            curr_click_a = 7
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_7 and TurnofB:
                        if 7 not in playerB and 7 not in playerA:
                            playerB.append(7)
                            curr_click_b = 7
                        TurnofB = False
                        TurnofA = True
                    elif event.key == pygame.K_8 and TurnofA:
                        if 8 not in playerA and 8 not in playerB:
                            playerA.append(8)
                            curr_click_a = 8
                        TurnofA = False
                        TurnofB = True
                    elif event.key == pygame.K_8 and TurnofB:
                        if 8 not in playerB and 8 not in playerA:
                            playerB.append(8)
                            curr_click_b = 8
                        TurnofB = False
                        TurnofA = True

            GameWindow.fill(white)
            GameWindow.blit(board, (0, 0))

            #  Wining conditions
            #  A win
            if TurnofB:
                for cond in win:
                    flag = True
                    for ele in cond:
                        if ele not in playerA:
                            flag = False
                    if flag:
                        winA = True
                        game_over = True
                        pygame.mixer.music.load("Gamover.mp3")
                        pygame.mixer.music.play()
                        start = True
                        break
            # B win
            elif TurnofA:
                for cond in win:
                    flag = True
                    for ele in cond:
                        if ele not in playerB:
                            flag = False
                    if flag:
                        winB = True
                        game_over = True
                        pygame.mixer.music.load("Gamover.mp3")
                        pygame.mixer.music.play()
                        start = True
                        break

            text_on_screen("Player A ",white,30,50)
            # text_on_screen(f"A{playerA}", white, 30, 100)

            text_on_screen("Player B ", white, 480, 50)
            # text_on_screen(f"A{playerB}", white, 480, 100)

            if(TurnofA and not TurnofB):
                text_on_screen("Turn of A",white,250,50)
            if(TurnofB and not TurnofA):
                text_on_screen("Turn of B",white,250,50)
            # Fxn for printing X or 0 as per turn
            print(playerA,playerB)

            # When no one will be  win
            if len(playerA)+len(playerB) == 9:
                start = True
                text_on_screen("Press space to continue",white,190,580)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE: # space to continue
                            game_over = True
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()
Welcome()
