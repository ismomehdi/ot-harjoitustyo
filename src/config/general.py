import os

# Background color
BG_COLOR = '#E8F8FF'

# Most of the sprites are fixed size or
# they are scaled to the tile size.
TILE_SIZE = 48

# The enemy size offset is used to make the enemy
# sprite appear on the correct position.
ENEMY_SIZE_OFFSET = 27

# Player constants
PLAYER_SPEED = 8
PLAYER_GRAVITY = 0.7
PLAYER_JUMP_SPEED = 17
PLAYER_COLLISION_JUMP_SPEED = 14
PLAYER_HEALTH = 3
PLAYER_GRACE_PERIOD = 500

# Enemy constants
ENEMY_AREA_SIZE = TILE_SIZE * 20
ENEMY_SPEED = 2
ENEMY_CHASE_SPEED = 100
ENEMY_GRAVITY = 0.7

# The points the player gets
COIN_POINTS = 1
ENEMY_POINTS = 10
