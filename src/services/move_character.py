from services.level import level_rect


def move_player(rect, direction, speed):
    """Moves the player sprite. The clamp_ip method is used
    to prevent the player from moving outside the level area.

    Args:
        rect: The rect of the player sprite.
        direction: The direction vector of the player sprite.
        speed: The speed integer of the player sprite.
    """
    rect.x += direction.x * speed
    rect.clamp_ip(level_rect)


def move_enemy(
        rect, direction, speed, starting_pos_x,
        area_size, chase_speed, player):
    """Moves the enemy sprite. The clamp_ip method is used
    to prevent the enemy from moving outside the level area.

    Args:
        rect: The rect of the enemy sprite.
        direction: The direction vector of the enemy sprite.
        speed: The speed integer of the enemy sprite.
        starting_pos_x: The starting x position integer of the enemy sprite.
        area_size: The area size integer of the enemy sprite.
        chase_speed: The chase speed integer of the enemy sprite.
        player: The player sprite.
    """

    # This defines the area the enemy can move in
    if rect.x < starting_pos_x:
        direction.x *= -1
    elif rect.x > starting_pos_x + area_size:
        direction.x *= -1

    # This makes the enemy chase the player if they are in the enemy's area
    if starting_pos_x < player.sprite.rect.x \
            < starting_pos_x + area_size:
        if player.sprite.rect.x - chase_speed > rect.x:
            direction.x = 1
        if player.sprite.rect.x + chase_speed < rect.x:
            direction.x = -1

    rect.x += direction.x * speed
    rect.clamp_ip(level_rect)
