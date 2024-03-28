class Interaction:
    def sprite_sprite_collision(self, sprite1, sprite2):
        return (sprite1.pos.x < sprite2.pos.x + sprite2.size[0] and
                sprite1.pos.x + sprite1.size[0] > sprite2.pos.x and
                sprite1.pos.y < sprite2.pos.y + sprite2.size[1] and
                sprite1.pos.y + sprite1.size[1] > sprite2.pos.y)