try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from src.classes.Vector import Vector

GRAVITY = 0

class Spritesheet:
    """ Manipulates a spritesheet for the Sprite class """

    def __init__(self, img_url, width, height, columns, rows,sprite_size_h,sprite_size_w):
        self.img_url = img_url
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.pos = Vector(0, 0)
        self.sprite_size_h = sprite_size_h                                                  # The height of the sprite in game.
        self.sprite_size_w = sprite_size_w                                                  # The width of the sprite in game.
        self.image = simplegui._load_local_image(self.img_url)

        # Calculate frame dimension
        self._init_dimension()

        # Set up frame index

        self.frame_index = [0,0]

    def _init_dimension(self):
        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

    def draw(self, canvas):
        """ This gets run on every frame. """

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)

        canvas.draw_image(self.image,
                          source_centre,
                          source_size,
                          self.pos.get_p(),
                          (self.sprite_size_h, self.sprite_size_w))

    def next_frame(self):
        """
        Goes to the next frame of the spritesheet.
        If there is none, it goes back to the beginning.
        """

        self.frame_index[0] += 1

        # go to the next row once it reaches the end
        if self.frame_index[0] >= self.max_c:
            self.frame_index[0] = 0
            # self.frame_index[1] += 1

        # go back to the start once it reaches the end of the last row
        # if self.frame_index[1] >= self.rows:
        #     self.frame_index[0] = 0
        #     self.frame_index[1] = 0