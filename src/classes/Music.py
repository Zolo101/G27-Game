
# In case the simplegui module is not available
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class music:
    def __init__(self):
        """
        Constructor initializes the song and related attributes.
        """
        self.music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
        self.music_object = None
        self.music_volume = 1.0  # Set the initial volume to maximum

    def play_music(self):
            self.music_object = self.music.play()


    def stop_music(self):
        if self.music_object is not None:
            self.music_object.pause()
            self.music_object = None

    def toggle_music(self):
        """
        Toggles between playing and stopping the music.
        """
        if self.music_object is None:
            self.play_music()
        else:
            self.stop_music()

    def set_volume(self, volume):
        """
        Sets the volume of the music playback.
        :param volume: A float value between 0.0 (muted) and 1.0 (maximum volume).
        """
        self.music_volume = volume
        if self.music_object is not None:
            self.music_object.set_volume(volume)

    def update(self, interaction):
        """
        Handles user interactions and updates the music playback accordingly.
        :param interaction: An object containing information about user input (e.g., key presses).
        """
        # Toggle music playback with the 'm' key
        if interaction.get_key("m"):
            self.toggle_music()