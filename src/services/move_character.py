from level import level_rect


def move_player(rect, direction, speed):
    rect.x += direction.x * speed
    rect.clamp_ip(level_rect)


def move_enemy(
        rect, direction, speed, starting_pos_x,
        area_size, chase_speed, player):

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
