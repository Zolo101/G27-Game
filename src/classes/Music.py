
# In case the simplegui module is not available
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class music:
    """
    A class to handle music playback in a simple GUI application.
    """

    def __init__(self):
        """
        Constructor initializes the song and related attributes.
        """
        self.music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
        self.music_object = None
        self.music_position = 0  # Track the current position of the music
        self.music_volume = 1.0  # Set the initial volume to maximum

    def play_music(self):
        """
        Starts playing the music from the beginning or the current position.
        """
        if self.music_object is None:
            self.music_object = self.music.play()
            self.music_position = 0  # Reset the position when starting from the beginning
        else:
            self.music_object.resume()

    def stop_music(self):
        """
        Stops the music and stores the current position.
        """
        if self.music_object is not None:
            self.music_position = self.music_object.get_position()  # Store the current position
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

        # Increase volume with the 'up' arrow key
        if interaction.get_key("up"):
            self.set_volume(min(self.music_volume + 0.1, 1.0))

        # Decrease volume with the 'down' arrow key
        if interaction.get_key("down"):
            self.set_volume(max(self.music_volume - 0.1, 0.0))

        # Seek forward in the music with the 'right' arrow key
        if interaction.get_key("right"):
            if self.music_object is not None:
                self.music_position = min(self.music_position + 5000, self.music.get_length())
                self.music_object.set_position(self.music_position)

        # Seek backward in the music with the 'left' arrow key
        if interaction.get_key("left"):
            if self.music_object is not None:
                self.music_position = max(self.music_position - 5000, 0)
                self.music_object.set_position(self.music_position)

