import random
import noise

from src.classes.Color import Color

BLOCK_SIZE = 10


def rand_col(minimum=0, maximum=255):
    g = random.randrange(minimum, maximum)
    b = random.randrange(minimum, maximum)
    r = random.randrange(minimum, maximum)
    return Color(r, g, b)
    # return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


class Terrain:
    def __init__(self, width, height):
        self.blocks = {}  # (x, y) : Block

        for i in range(0, width // BLOCK_SIZE):
            h = 50 - (noise.pnoise1(i / 20) * 25) + (noise.pnoise1(i / 10) * 10)

            for j in range(0, height // BLOCK_SIZE):
                # noise

                if j > h:
                    self.blocks[(i * BLOCK_SIZE, j * BLOCK_SIZE)] = Block(i * BLOCK_SIZE, j * BLOCK_SIZE)
        self.compute_lighting()
        self.compute_texture()

    def draw(self, canvas):
        for block in self.blocks.values():
            block.draw(canvas)

    def compute_texture(self):
        #
        #
        # HERE IS WHERE YOU WOULD COMPUTE THE TEXTURE
        # FOR EACH BLOCK
        #
        #
        # TODO: RIGHT NOW ITS DOING SOLID COLOURS BUT LATER ON WE GOT TO DO TEXTURES
        #
        #

        for block in self.blocks.values():
            if ((block.x, block.y - BLOCK_SIZE) in self.blocks and
                    (block.x - BLOCK_SIZE, block.y) in self.blocks and
                    (block.x + BLOCK_SIZE, block.y) in self.blocks):
                block.color = Color(145, 97, 7)
            else:
                block.color = Color(81, 255, 61)

    def compute_lighting(self):
        # compute how much blocks are in each 3x3 chunk
        for block in self.blocks.values():
            block.lighting = 0
            e = 0

            # for i in range(-1, 2):
            for i in range(-4, 5):
                for j in range(-4, 5):
                    nx = block.x + i * BLOCK_SIZE
                    ny = block.y + j * BLOCK_SIZE
                    if (nx, ny) in self.blocks or not (0 < nx < 1280) or not (0 < ny < 800):
                        block.lighting += 1
                    else:
                        e += 1

            if e > 3:
                block.lighting -= 1

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
        self.color = rand_col()

    def draw(self, canvas):
        x = self.lighting * 0.9
        # color = f"rgb({x}, {x}, {x})"
        color = self.color - Color(x, x, x)
        canvas.draw_polygon([(self.x, self.y),
                             (self.x + BLOCK_SIZE, self.y),
                             (self.x + BLOCK_SIZE, self.y + BLOCK_SIZE),
                             (self.x, self.y + BLOCK_SIZE)],
                            1,
                            color.__str__(),
                            color.__str__())

    def get_color(self):
        return self.color
