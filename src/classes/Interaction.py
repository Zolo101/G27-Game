class Interaction:
    def __init__(self, key_map):
        # set every value in a dictionary to False
        self.key_map = key_map
        self.press_map = dict.fromkeys(key_map.values(), False)

    def key_down(self, key):
        self.press_map[key] = True

    def key_up(self, key):
        self.press_map[key] = False

    def get_key(self, key):
        return self.press_map[self.key_map[key]]

    def keys_down(self):
        return [key for key, value in self.press_map.items() if value]
