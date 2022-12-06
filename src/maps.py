from os import walk

# The level maps are saved as .txt files in the levels folder.
# The following characters are used to build the level:
#
# P = Player
# X = Ground tile
# x = Sky tile
# o = Coin

TILE_SIZE = 64
path = 'src/levels/'
maps = {}

for _, __, filenames in walk(path):
    for filename in sorted(filenames):
        level_file = open(path + filename, 'r')
        data = level_file.read().replace("'", "").split("\n")
        filename = filename.strip('.txt')
        maps[filename] = data
        level_file.close()


        