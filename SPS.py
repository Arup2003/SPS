import pygame
import socket
import threading


# ------------------------------------------------

def choice():
    global player_choice
    c.send(bytes(player_choice, 'utf-8'))
    print("SENT")
    answer = c.recv(1024).decode()
    print(answer)
    return answer

# ------------------------------------------------

go = True
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("SPS")

# The image files gets loaded
Paper_player = pygame.image.load("Paper_player.png")
Scissor_player = pygame.image.load("Scissor_player.png")
Paper_comp = pygame.image.load("Paper_comp.png")
Scissor_comp = pygame.image.load("Scissor_comp.png")
bg = pygame.image.load("bg.jpeg")
stone = pygame.image.load("stone.png")
stone_hover = pygame.image.load("stone_hover.png")
paper = pygame.image.load("paper.png")
paper_hover = pygame.image.load("paper_hover.png")
scissor = pygame.image.load("scissor.png")
scissor_hover = pygame.image.load("scissor_hover.png")
point = pygame.image.load("your_point.png")
no_point = pygame.image.load("their_point.png")
tie = pygame.image.load("tie.png")

# variables for changing icons
hover_s = "off"
hover_p = "off"
hover_sc = "off"

# defining score for program initialization
score_player = 0
score_comp = 0

# terminate loop is for restarting game
terminate = True
connected = "yes"
print("connected")
while terminate:
    if connected == "yes":
        c = socket.socket()
        c.connect(("localhost", 9999))
        connected = "no"

    print("CONNECTED")
    go = True
    show = True
    Stone_player = pygame.image.load("Stone_player.png")
    Stone_comp = pygame.image.load("Stone_comp.png")
    wait_sec = 0
    waiting_time = 0

    # go loop is for looping 5 points of same game
    # go loop has the choosing screen
    # go loop has the result defining algorithm
    while go:
        show = True
        # Reset the waiting hand image graphics
        Stone_player = pygame.image.load("Stone_player.png")
        Stone_comp = pygame.image.load("Stone_comp.png")

        # Wait 3 second after result reset variable
        wait_sec = 0
        waiting_time = 0

        screen.blit(bg, (0, 0))

        # Icon changes size when hovered
        # When clicked it will compute who won and who lost
        # MAIN RESULT ALGORITHM
        if hover_s == "off":
            screen.blit(stone, (50, 430))
        if hover_s == "on":
            screen.blit(stone_hover, (50, 430))
            if pygame.mouse.get_pressed()[0]:
                player_choice = "A"
                data = choice()
                print(data)
                result = data[1]
                computer = data[0]
                show = True
                go = False
        if hover_p == "off":
            screen.blit(paper, (300, 430))
        if hover_p == "on":
            screen.blit(paper_hover, (300, 430))
            if pygame.mouse.get_pressed()[0]:
                player_choice = "B"
                data = choice()
                print(data)
                result = data[1]
                computer = data[0]
                go = False
                show = True
        if hover_sc == "off":
            screen.blit(scissor, (550, 430))
        if hover_sc == "on":
            if pygame.mouse.get_pressed()[0]:
                player_choice = "C"
                data = choice()
                print(data)
                result = data[1]
                computer = data[0]
                go = False
                show = True
            screen.blit(scissor_hover, (550, 430))

        hover_s = "off"
        hover_p = "off"
        hover_sc = "off"

        # Get position of mouse for hover
        if pygame.mouse.get_pos()[0] >= 60 and pygame.mouse.get_pos()[0] <= 210 and pygame.mouse.get_pos()[1] >= 430 and pygame.mouse.get_pos()[1] <= 515:
            hover_s = "on"

        if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] >= 430 and pygame.mouse.get_pos()[1] <= 515:
            hover_p = "on"

        if pygame.mouse.get_pos()[0] >= 560 and pygame.mouse.get_pos()[0] <= 710 and pygame.mouse.get_pos()[1] >= 430 and pygame.mouse.get_pos()[1] <= 515:
            hover_sc = "on"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False
                go = False
                terminate = False

        # Speed variables and position of hand variables for show
        x_change = 5
        y_change = 5
        x_comp_change = 5
        y_comp_change = 5
        play = True
        x = -200
        y = 600
        x_comp = 800
        y_comp = -360
        pygame.display.update()

    while show:

        # score bar
        screen.blit(pygame.image.load("show.png"), (0, 0))
        if score_comp == 0:
            pygame.draw.polygon(screen, "blue", [(10, 60), (35, 50), (137, 141), (10, 190)])
        if score_comp == 1:
            pygame.draw.polygon(screen, "blue", [(10, 75), (45, 60), (137, 141), (10, 190)])
        if score_comp == 2:
            pygame.draw.polygon(screen, "blue", [(10, 88), (56, 70), (137, 141), (10, 190)])
        if score_comp == 3:
            pygame.draw.polygon(screen, "blue", [(10, 118), (79, 90), (137, 141), (10, 190)])
        if score_comp == 4:
            pygame.draw.polygon(screen, "blue", [(10, 150), (105, 113), (137, 141), (10, 190)])

        if score_player == 0:
            pygame.draw.polygon(screen, "red", [(53, 35), (63, 10), (195, 10), (155, 120)])
        if score_player == 1:
            pygame.draw.polygon(screen, "red", [(62, 44), (76, 10), (195, 10), (155, 120)])
        if score_player == 2:
            pygame.draw.polygon(screen, "red", [(71, 52), (88, 10), (195, 10), (155, 120)])
        if score_player == 3:
            pygame.draw.polygon(screen, "red", [(99, 74), (125, 10), (195, 10), (155, 120)])
        if score_player == 4:
            pygame.draw.polygon(screen, "red", [(123, 95), (155, 10), (195, 10), (155, 120)])

        screen.blit(Stone_player, (x, y))
        x += x_change
        y -= y_change

        if x > 100:
            x_change = 0
            y_change = 0
            if player_choice == "A":
                Stone_player = Stone_player
            if player_choice == "B":
                Stone_player = Paper_player
            if player_choice == "C":
                Stone_player = Scissor_player
            screen.blit(Stone_comp, (x_comp, y_comp))

            x_comp -= x_comp_change
            y_comp += y_comp_change

            if x_comp <= 425:
                x_comp_change = 0
                y_comp_change = 0
                if computer == "A":
                    Stone_comp = Stone_comp
                    if result == "w":
                        screen.blit(point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            score_player += 1
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False
                    if result == "l":
                        screen.blit(no_point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            wait_sec = 1
                            score_comp += 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False

                    if result == "t":
                        screen.blit(tie, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False

                if computer == "B":
                    if result == "w":
                        screen.blit(point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            score_player += 1
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False

                    if result == "l":
                        screen.blit(no_point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            score_comp += 1
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False
                    if result == "t":
                        screen.blit(tie, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False

                    Stone_comp = Paper_comp
                if computer == "C":
                    if result == "w":
                        screen.blit(point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            score_player += 1
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False
                    if result == "l":
                        screen.blit(no_point, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            score_comp += 1
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False
                    if result == "t":
                        screen.blit(tie, (425, 325))
                        time = pygame.time.get_ticks()
                        if wait_sec == 0:
                            waiting_time = pygame.time.get_ticks()
                            wait_sec = 1
                        if wait_sec == 1:
                            if time - waiting_time >= 5000:
                                go = True
                                show = False

                    Stone_comp = Scissor_comp
                y_comp_change = 0

        print(score_comp, score_player)

        if score_player == 4 or score_comp == 4:
            show = False
            go = False
            terminate = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate = False
                show = False

        pygame.display.update()
