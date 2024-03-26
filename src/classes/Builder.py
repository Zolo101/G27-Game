from src.classes.Color import Color
from src.classes.Vector import Vector
from src.game.Terrain import Block


class Builder:
    def __init__(self):
        self.pos = Vector(0, 0)
        pass

    def draw(self, canvas, interaction):
        self.pos = interaction.mouse_pos.snap(Vector(20, 20))

        canvas.draw_polygon([
            (interaction.mouse_pos.x, interaction.mouse_pos.y),
            (interaction.mouse_pos.x + 20, interaction.mouse_pos.y),
            (interaction.mouse_pos.x + 20, interaction.mouse_pos.y + 20),
            (interaction.mouse_pos.x, interaction.mouse_pos.y + 20)],
            0,
            "blue",
            "blue"
        )

    def build(self, terrain):
        block = Block(self.pos.x, self.pos.y)
        block.color = Color(156, 156, 156)
        terrain.blocks[self.pos.get_p()] = block

        terrain.compute_visible()
        terrain.compute_lighting()
