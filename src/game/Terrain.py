import random
import noise

BLOCK_SIZE = 10


def rand_col():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'


class Terrain:
    def __init__(self):
        self.blocks = {}  # (x, y) : Block

        for i in range(0, 600 // BLOCK_SIZE):
            h = 20 + (noise.pnoise1(i / 10) * 10)

            for j in range(0, 400 // BLOCK_SIZE):
                # noise

                if j > h:
                    self.blocks[(i * BLOCK_SIZE,j * BLOCK_SIZE)] = Block(i * BLOCK_SIZE, j * BLOCK_SIZE)
        # self.compute_lighting()
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
                block.color = "brown"
            else:
                block.color = "green"

    def compute_lighting(self):
        for block in self.blocks:
            block.lighting = 0
            for other in self.blocks:
                if block != other:
                    if abs(block.x - other.x) <= BLOCK_SIZE and abs(block.y - other.y) <= BLOCK_SIZE:
                        block.lighting += 1


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = rand_col()
        self.lighting = 0

    def draw(self, canvas):
        x = 255 - (self.lighting * 30)
        # color = f"rgb({x}, {x}, {x})"
        color = self.color
        canvas.draw_polygon([(self.x, self.y),
                             (self.x + BLOCK_SIZE, self.y),
                             (self.x + BLOCK_SIZE, self.y + BLOCK_SIZE),
                             (self.x, self.y + BLOCK_SIZE)],
                            1,
                            color,
                            color)
