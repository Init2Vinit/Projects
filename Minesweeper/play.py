import sys
from constants import *
from buttons import Button
from grid import Grid
from texts import Fonts


#game window
game_window = pygame.display.set_mode((window_width, window_height))

#base state of the game
def base_state():
    #intro caption
    pygame.display.set_caption("Minesweeper")

    #project name
    project_name = Fonts("Computer Science Project", "crimson")
    project_name.set_text_size(48)
    x_pos = (window_width - project_name.get_text_box().get_width() - text_padding) / 2
    y_pos = 0
    project_name.display_text_box(game_window, x_pos, y_pos)

    #welcoming the user
    welcome = Fonts("Welcome to Minesweeper", "cyan")
    welcome.set_text_size(32)
    x_pos = (window_width - welcome.get_text_box().get_width() - text_padding) / 2
    y_pos = window_height / 6
    welcome.display_text_box(game_window, x_pos, y_pos)

    #me
    myself = Fonts("coded by: Vinit Praganesh", "yellow")
    x_pos = (window_width - myself.get_text_box().get_width() - text_padding) / 2
    y_pos = window_height / 4
    myself.display_text_box(game_window, x_pos, y_pos)

    #display choices to select a mode
    mode_choice = Fonts("Please choose your difficulty", "green")
    x_pos = (window_width - mode_choice.get_text_box().get_width()) / 2
    y_pos = window_height / 2.5
    mode_choice.display_text_box(game_window, x_pos, y_pos)

    #choice a
    choice_a = Fonts("A.  9 x 9 grid with 10 mines", "white")
    x_pos = (window_width - choice_a.get_text_box().get_width()) / 2
    y_pos += choice_a.get_text_box().get_height()
    choice_a.display_text_box(game_window, x_pos, y_pos)

    #choice b
    choice_b = Fonts("B. 13 x 13 grid with 20 mines", "white")
    x_pos = (window_width - choice_b.get_text_box().get_width()) / 2
    y_pos += choice_b.get_text_box().get_height()
    choice_b.display_text_box(game_window, x_pos, y_pos)

    #choice c
    choice_c = Fonts("C. 16 x 16 grid with 40 mines", "white")
    x_pos = (window_width - choice_c.get_text_box().get_width()) / 2
    y_pos += choice_c.get_text_box().get_height()
    choice_c.display_text_box(game_window, x_pos, y_pos)

    #position of the buttons that will be used to start the game
    y_pos = 2 * window_height / 3 
    x_pos = window_width / 6
    button_a = Button("white", x_pos, y_pos, 150, 34, "A")
    button_a.draw_button(game_window)
    
    x_pos = window_width / 2
    button_b = Button("white", x_pos-80, y_pos, 150, 34, "B")
    button_b.draw_button(game_window)

    button_c = Button("white", x_pos+100, y_pos, 150, 34, "C")
    button_c.draw_button(game_window)

    #leaderboard button
    button_leaderboard = Button("red", x_pos-80, y_pos+75, 170, 50, "Leaderboard")
    button_leaderboard.draw_button(game_window)

    #exit the game anytime -- use ESC (Escape) key
    esc = Fonts("Press Esc key to quit the game", "purple")
    x_pos = (window_width - esc.get_text_box().get_width() - text_padding) / 2
    y_pos = window_height - esc.get_text_box().get_height() - 16
    esc.display_text_box(game_window, x_pos, y_pos)

    #update the window
    pygame.display.update()

    #game running flag -- boolean value
    running = True

    while running:
        #going through different event types
        for event in pygame.event.get():

            #game quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #quit the game if escape key is pressed
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            #mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #left click
                if event.button == 1:
                    x, y = event.dict["pos"]

                    #global variables
                    global grid_dimension, num_mines

                    #checking which button has been pressed
                    if button_a.get_button_rect().collidepoint(x, y):
                        grid_dimension, num_mines = 9, 10
                        running = False

                    elif button_b.get_button_rect().collidepoint(x, y):
                        grid_dimension, num_mines = 13, 20
                        running = False
                    
                    elif button_c.get_button_rect().collidepoint(x,y):
                        grid_dimension, num_mines = 16, 40
                        running = False

                    elif button_leaderboard.get_button_rect().collidepoint(x,y):

                        game_window.fill(colours["black"])

                        top_score = Fonts("These are the top 10 best times:", "white")
                        x_pos = (window_width - top_score.get_text_box().get_width() - text_padding) / 2
                        y_pos = 0
                        top_score.display_text_box(game_window, x_pos, y_pos)

                        top=[]
                        with open("Winner.txt","r")as top10:
                            for line in top10:
                                top.append(line)
                                top.sort(reverse = False)

                        t=1
                        while t < 11:
                            best = Fonts(str(t)+")"+top[t-1],"white")
                            x_pos = (window_width - best.get_text_box().get_width() - text_padding) /2
                            y_pos = 100
                            best.display_text_box(game_window,x_pos,y_pos)
                            t+=1

                        pygame.display.update()

    #clears the window -- fills it black
    game_window.fill(colours["black"])

    game_loop()


#main game loop
def game_loop():
    #game caption
    pygame.display.set_caption("Minesweeper")

    #game variables
    timer = 0
    switched_on = False

    #grid location
    grid_x = (window_width - (grid_dimension * tile_size)) / 2
    grid_y = (window_width - (grid_dimension * tile_size)) / 3

    #drawing the grid with the given values from input
    grid = Grid(grid_x, grid_y, grid_dimension, num_mines)
    grid.draw_grid()

    #result font
    result_fonts = Fonts(text="", colour="black")
    center_x, center_y = 0, 0

    #game runnning -- boolean value
    running = True
    while running:
        #timer and mine count
        timer_text = f"Time: {timer:<6}"
        flags_text = f"Flags: {grid.get_mine_count():2}"

        #updating the display
        pygame.display.update()

        #start the timer
        if switched_on:
            clock = pygame.time.Clock()
            timer += clock.tick(1) // 1000

        #won or lost
        result = ""

        #different events looked for whilst playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #left click
                if event.button == 1:
                    click = "left"
                elif event.button == 3:
                    #right click
                    click = "right"
                else:
                    continue #no or wrong click

                #turning on the timer after the first click
                switched_on = True

                #position of the click made
                x, y = event.dict["pos"]

                result = grid.update(x, y, click)
                flags_text = f"Flags: {grid.get_mine_count():2}" #updating the mines count displayed after each click

        #showing the timer and the mines
        timer_font = Fonts(timer_text, "yellow")
        timer_font.display_text_box(game_window, text_padding, text_padding)

        flags_font = Fonts(flags_text, "cyan")
        flags_font.display_text_box(game_window, -text_padding, text_padding)

        #window center
        center_y = text_padding

        #result -- either won or lost
        if result == "lost":
            #dispaly game over
            result_fonts.set_colour("red")
            result_fonts.set_text("You Lost")
            center_x = (window_width - result_fonts.get_text_box().get_width() - text_padding) / 2
            result_fonts.display_text_box(game_window, center_x, center_y)
            switched_on = False
            running = False

        elif result == "won":
            #display you won
            result_fonts.set_colour("green")
            result_fonts.set_text("You WON!")
            center_x = (window_width - result_fonts.get_text_box().get_width() - text_padding) / 2
            result_fonts.display_text_box(game_window, center_x, center_y)
            switched_on = False
            running = False
            pygame.display.update()

            file = open('Winner.txt', 'a')
            file.write(str(timer)+"\n")
            file.close()

    #update the display
    pygame.display.update()

    #waiting for 2 seconds
    pygame.time.wait(3000)

    #clearing the fonts
    result_fonts.set_colour("black")
    result_fonts.display_text_box(game_window, center_x, center_y)

    #quit the game
    game_over_state()


#game over
def game_over_state():
    #window caption
    pygame.display.set_caption("Play Again?")

    #button position
    center_x = (window_width - button_width) / 2
    center_y = text_padding

    #restart button
    restart_button = Button(colour="white", x=center_x, y=center_y, height = 35, text="Restart")
    restart_button.draw_button(game_window)
    pygame.display.update()


    while True:
        #catch different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                #left click
                if event.button == 1:
                    x, y = event.dict["pos"]

                    #check for restart
                    if restart_button.get_button_rect().collidepoint(x, y):
                        #clear the game window
                        game_window.fill(colours["black"])

                        #goto bast state
                        base_state()