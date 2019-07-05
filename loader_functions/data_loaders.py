import os

import shelve

base_dir = '.data/'


def save_game(player, entities, game_map, message_log, game_state):

    if not os.path.isdir(base_dir):
        try:
            os.mkdir(base_dir)
        except OSError:
            print('Unable to create data directory')

    with shelve.open(base_dir + 'savegame', 'n') as data_file:
        data_file['player_index'] = entities.index(player)
        data_file['entities'] = entities
        data_file['game_map'] = game_map
        data_file['message_log'] = message_log
        data_file['game_state'] = game_state


def load_game():

    if not os.path.isfile(base_dir + 'savegame.dat'):
        raise FileNotFoundError

    with shelve.open(base_dir + 'savegame', 'r') as data_file:
        player_index = data_file['player_index']
        entities = data_file['entities']
        game_map = data_file['game_map']
        message_log = data_file['message_log']
        game_state = data_file['game_state']

    player = entities[player_index]

    return player, entities, game_map, message_log, game_state