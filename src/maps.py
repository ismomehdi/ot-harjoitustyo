from os import walk

# The level maps are saved as .txt files in the levels folder.
# The following characters are used to build the level in the .txt file:
#
# P = Player
# X = Ground tile
# x = Sky tile
# o = Coin

PATH = 'src/levels/'
maps = {}

# Import .txt files from the levels folder to the maps dictionary.
for _, __, filenames in walk(PATH):
    for filename in sorted(filenames):
        with open(PATH + filename, 'r', encoding="utf-8", errors='ignore') as level_file:
            data = level_file.read().replace("'", "").split("\n")
            filename = filename.strip('.txt')
            maps[filename] = data
