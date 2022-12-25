import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path = os.path.join(dirname, "../../", ".env"))
except FileNotFoundError:
    pass

MAPS_PATH = os.getenv('MAPS_PATH') or 'src/levels/'

# Sprite images
PLAYER_IMAGES_PATH = os.getenv('PLAYER_IMAGES_PATH') or 'src/assets/images/player/'
ENEMY_IMAGES_PATH = os.getenv('ENEMY_IMAGES_PATH') or 'src/assets/images/enemy/'
COIN_IMAGES_PATH = os.getenv('COIN_IMAGES_PATH') or 'src/assets/images/coin/'
GROUND_TILE_IMAGE_PATH = os.getenv('GROUND_TILE_IMAGE_PATH') or 'src/assets/images/tiles/ground_tile.png'
SKY_TILE_IMAGE_PATH = os.getenv('SKY_TILE_IMAGE_PATH') or 'src/assets/images/tiles/sky_tile.png'
GOAL_IMAGES_PATH = os.getenv('GOAL_IMAGES_PATH') or 'src/assets/images/goal/'

# Menu images
PAUSE_MENU_IMAGES_PATH = os.getenv('PAUSE_MENU_IMAGES_PATH') or 'src/assets/images/menu/pause_menu/'
MAIN_MENU_IMAGES_PATH = os.getenv('MAIN_MENU_IMAGES_PATH') or 'src/assets/images/menu/main_menu/'
