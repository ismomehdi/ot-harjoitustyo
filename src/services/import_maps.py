from os import walk
from config.paths import MAPS_PATH


def import_maps():
    """Imports the level maps from the levels folder.

    The level maps are saved as .txt files. The following characters are used to
    build the level in the .txt file:

    P = Player
    X = Ground tile
    x = Sky tile
    o = Coin
    e = Enemy
    f = Goal

    Returns:
        dictionary: Dictionary containing the level maps (keys: 1, 2, 3 etc).
    """
    maps = {}

    for _, __, filenames in walk(MAPS_PATH):
        for filename in sorted(filenames):
            with open(MAPS_PATH + filename, 'r', encoding="utf-8", errors='ignore') as level_file:
                data = level_file.read().replace("'", "").split("\n")
                filename = filename.strip('.txt')
                maps[filename] = data

    return maps
