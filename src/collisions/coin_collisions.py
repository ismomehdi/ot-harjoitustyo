def apply_coin_collisions(rect, coin_sprites):
    for sprite in coin_sprites:
        if sprite.rect.colliderect(rect):
            sprite.kill()