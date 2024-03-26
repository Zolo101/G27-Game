import random
from perlin_noise import PerlinNoise

from src.classes.Color import Color

BLOCK_SIZE = 20
noise = PerlinNoise()


def rand_col(minimum=0, maximum=255):
    g = random.randrange(minimum, maximum)
    b = random.randrange(minimum, maximum)
    r = random.randrange(minimum, maximum)
    return Color(r, g, b)
    # return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


class Terrain:
    """
    Container that stores every `Block` in the game
    """

    def __init__(self, width, height):
        self.blocks = {}  # (x, y) : Block

        # These are blocks that the player can touch
        self.visible_blocks = {}

        for i in range(0, width // BLOCK_SIZE):
            h = min(35, 30 - (noise.noise(i / 20) * 20) + (noise.noise(i / 10) * 10))
            # h = 30

            for j in range(0, height // BLOCK_SIZE):
                # noise

                if j > h:
                    self.blocks[(i * BLOCK_SIZE, j * BLOCK_SIZE)] = Block(i * BLOCK_SIZE, j * BLOCK_SIZE)
        self.compute_texture()
        self.compute_lighting()
        self.compute_visible()

    def draw(self, canvas):
        """ This gets run on every frame. """
        for block in self.blocks.values():
            block.draw(canvas)

    def any_neighbours(self, block):
        """ Returns True if there is a neighbour block touching this block. """
        return ((block.x, block.y - BLOCK_SIZE) in self.blocks and
                (block.x - BLOCK_SIZE, block.y) in self.blocks and
                (block.x + BLOCK_SIZE, block.y) in self.blocks or
                # not (0 < block.x < 1280)):
                not (20 < block.x < 1240))

    def remove_dead(self):
        """ Removes blocks where health <= 0."""
        to_remove = {}
        for coord, block in self.blocks.items():
            if block.is_dead():
                to_remove[coord] = block

        for coord in to_remove.keys():
            del self.blocks[coord]

        if len(to_remove) > 0:
            self.compute_lighting()
            self.compute_visible()

    def heal(self):
        """ Heal terrain slowly """
        for block in self.blocks.values():
            block.heal(0.05)

    def compute_visible(self):
        """ Updates the dict of blocks that collide with air."""
        self.visible_blocks.clear()

        for block in self.blocks.values():
            # check neighbours
            # if self.any_neighbours(block):
            if not ((block.x, block.y - BLOCK_SIZE * 3) in self.blocks and
                    (block.x - BLOCK_SIZE * 3, block.y) in self.blocks and
                    (block.x + BLOCK_SIZE * 3, block.y) in self.blocks or
                    # not (0 < block.x < 1280)):
                    not (20 < block.x < 1240)):
                self.visible_blocks[(block.x, block.y)] = block

        # print(len(self.visible_blocks), "visible,", len(self.blocks), "total")

    def compute_texture(self):
        """ Gives a color for the block based on some comparisons. """
        for block in self.blocks.values():
            if self.any_neighbours(block):
                block.color = Color(145, 97, 7)
            else:
                block.color = Color(81, 255, 61)

    def compute_lighting(self):
        """
        Computes the lightning for each block by
        checking how many blocks are in a 9x9 grid.
        """

        for block in self.blocks.values():
            block.lighting = 0
            clip = 0

            # for i in range(-1, 2):
            for i in range(-4, 5):
                for j in range(-4, 5):
                    nx = block.x + i * BLOCK_SIZE
                    ny = block.y + j * BLOCK_SIZE
                    if (nx, ny) in self.blocks or not (0 < nx < 1280) or not (0 < ny < 800):
                        block.lighting += 1
                    else:
                        clip += 1

            if clip > 3:
                block.lighting -= 1

            # if block.lighting > 80:
            # block.color += rand_col(0, max(1, block.lighting // 10))

            # block.lighting += (block.x - BLOCK_SIZE, block.y + BLOCK_SIZE) in self.blocks
            # block.lighting += (block.x, block.y + BLOCK_SIZE) in self.blocks
            # block.lighting += (block.x + BLOCK_SIZE, block.y + BLOCK_SIZE) in self.blocks

            # block.lighting += (block.x - BLOCK_SIZE, block.y) in self.blocks
            # block.lighting += (block.x + BLOCK_SIZE, block.y) in self.blocks

            # block.lighting += (block.x - BLOCK_SIZE, block.y - BLOCK_SIZE) in self.blocks
            # block.lighting += (block.x, block.y - BLOCK_SIZE) in self.blocks
            # block.lighting += (block.x + BLOCK_SIZE, block.y - BLOCK_SIZE) in self.blocks


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lighting = 0
        self.offset_colour = rand_col(0, 10)
        self.color = rand_col()
        self.health = 100

    def draw(self, canvas):
        """ This gets run on every frame. """

        x = self.lighting * 0.7

        # This gradually makes the block more red as damaged
        color = self.color
        color += self.offset_colour
        color += Color(255 - ((self.health / 101) * 255), 0, 0)

        # Darken terrain depending on lightning
        color -= Color(x, x, x)

        canvas.draw_polygon([(self.x, self.y),
                             (self.x + BLOCK_SIZE, self.y),
                             (self.x + BLOCK_SIZE, self.y + BLOCK_SIZE),
                             (self.x, self.y + BLOCK_SIZE)],
                            1,
                            color.__str__(),
                            color.__str__())

    def heal(self, amount):
        self.health = min(100, self.health + amount);

    def get_color(self):
        return self.color

    def is_dead(self):
        return self.health < 0
