try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from src.classes.Vector import Vector

GRAVITY = 2

class Spritesheet:
    def __init__(self, img_url, width, height, columns, rows):
        self.img_url = img_url
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.pos = Vector(0, 0)


        # Calculate frame dimension
        self._init_dimension()

        # Set up frame index
        self.frame_index = [2, 1]

    def _init_dimension(self):
        self.frame_width = self.width / self.columns
        self.frame_height = self.height / self.rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2

    def draw(self, canvas):

        source_centre = (
            self.frame_width * self.frame_index[0] + self.frame_centre_x,
            self.frame_height * self.frame_index[1] + self.frame_centre_y
        )

        source_size = (self.frame_width, self.frame_height)
        # destination_centre = (self.x, self.y)
        # # doesn't have to be same aspect ratio as frame!
        # destination_size = (self.height, self.width)

        img = simplegui.load_image(self.img_url)



        canvas.draw_image(img,
                          source_centre,
                          source_size,
                          (self.pos.x, self.pos.y),
                          (self.height, self.width))









    def next_frame(self):

        self.frame_index[0] += 1

        # go to the next row once it reaches the end
        if self.frame_index[0] >= self.columns:
            self.frame_index[0] = 0
            self.frame_index[1] += 1

        # go back to the start once it reaches the end of the last row
        if self.frame_index[1] >= self.rows:
            self.frame_index[0] = 0
            self.frame_index[1] = 0

