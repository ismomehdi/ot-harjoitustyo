from os import walk
from config.paths import MAPS_PATH

# The level maps are saved as .txt files in the levels folder.
# The following characters are used to build the level in the .txt file:
#
# P = Player
# X = Ground tile
# x = Sky tile
# o = Coin


def import_maps():
    maps = {}

    for _, __, filenames in walk(MAPS_PATH):
        for filename in sorted(filenames):
            with open(MAPS_PATH + filename, 'r', encoding="utf-8", errors='ignore') as level_file:
                data = level_file.read().replace("'", "").split("\n")
                filename = filename.strip('.txt')
                maps[filename] = data

    return maps