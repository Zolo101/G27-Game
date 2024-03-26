try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
class music:
    #constuctor initialises the song
    def __init__(self):
        self.music = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")
        self.music_object = None

    #starts the music
    def play_music(self):
        if self.music_object is None:
            self.music_object = self.music.play()

    #stops the music
    def stop_music(self):
        if self.music_object is not None:
            self.music_object.pause()
            self.music_object = None

    #switch back and forth
    def toggle_music(self):
        if self.music_object is None:
            self.play_music()
        else:
            self.stop_music()
        
    #use to add the ability for the player to stop/start    
    def update(self, interaction):
        if interaction.get_key("m"):
            self.toggle_music()