from src.classes.Vector import Vector


class Interaction:
    """ For handling interactions """

    def __init__(self, key_map):
        # set every value in a dictionary to False
        self.key_map = key_map
        self.press_map = dict.fromkeys(key_map.values(), False)
        self.mouse_pos = Vector(0,0)

    def key_down(self, key):
        self.press_map[key] = True

    def key_up(self, key):
        self.press_map[key] = False

    def mouse_click(self, pos):
        self.mouse_pos.x = pos[0]
        self.mouse_pos.y = pos[1]

    # def mouse_drag(self, pos):
    #     self.m
    #     print(pos)

    def get_key(self, key):
        """
        Checks if a key is down. For example:


        interaction.get_key("a")
        interaction.get_key("space")
        """
        return self.press_map[self.key_map[key]]

    def keys_down(self):
        # TODO: Do we need this function?
        """ Returns a list of keys currently down """
        return [key for key, value in self.press_map.items() if value]
