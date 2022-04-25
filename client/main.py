import sys
import pygame
from pygame.locals import *
from globals import *
import random
from entity import *
from networking import *


def main():
    pygame.init()

    frame_per_sec = pygame.time.Clock()
    pygame.display.set_caption("Networking Test")
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.draw.circle(DISPLAYSURF, GREEN, (200, 50), 30)

    # Connect to the network
    network = Network()
    network.connect()

    # Start creating necessary entities
    gb = Entity("resources/grass_bg.png", SCREEN_WIDTH, SCREEN_HEIGHT)
    player = Player("resources/awesomeface.png",
                    xinit=random.randint(0, SCREEN_WIDTH),
                    yinit=random.randint(0, SCREEN_HEIGHT))
    none_players = {}
    game_state = {}

    def handle_non_players(client_id, players, position_datum):
        for client in position_datum:
            if client == client_id:
                continue
            new_x = position_datum[client]["x_pos"]
            new_y = position_datum[client]["y_pos"]
            if client not in players:
                players[client] = Entity("resources/awesomeface.png", xinit=new_x, yinit=new_y)
            else:
                players[client].update_position(new_x, new_y)
        return players

    while True:
        # Get events and execute them accordingly
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Receive the new state from the server
        new_game_state = network.receive_message()
        if new_game_state is not None:
            game_state = new_game_state

        # Update all the non player positions
        if "player_position" in game_state:
            none_players = handle_non_players(network.client_id, none_players, game_state["player_position"])

        # Update all entities
        update = player.update()
        if update is not None:
            print(update)
            network.send_message(update)

        # Redraw all entities
        DISPLAYSURF.fill(WHITE)
        gb.draw(DISPLAYSURF)
        player.draw(DISPLAYSURF)
        for non_play in none_players:
            none_players[non_play].draw(DISPLAYSURF)

        # Update the display and FPS
        pygame.display.update()
        frame_per_sec.tick(FPS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt was caught")
        print("Exiting...")
        sys.exit(0)
