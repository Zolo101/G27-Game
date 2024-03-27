class Waves:
    """
    A class to manage the waves of zombies in the game.
    """

    def __init__(self, zom_num, zom_health, zom_max_health, speed):
        """
        Constructor initializes the number of zombies, their health, and speed for the current wave.
        :param zom_num: The number of zombies in the current wave.
        :param zom_health: The initial health of each zombie in the current wave.
        :param zom_max_health: The maximum health of each zombie in the current wave.
        :param speed: The speed of the zombies in the current wave.
        """
        self.zom_num = zom_num
        self.zom_health = zom_health
        self.zom_max_health = zom_max_health
        self.speed = speed
        self.current_wave = 1  # Track the current wave number

    def update(self, add_hp, add_speed):
        """
        Updates the zombie parameters for the next wave.
        :param add_hp: The additional health to be added to each zombie's health.
        :param add_speed: The additional speed to be added to the zombies' speed.
        """
        self.zom_health += add_hp
        self.zom_max_health += add_hp
        self.speed += add_speed
        self.current_wave += 1  # Increment the wave number

    def reset(self):
        """
        Resets the wave parameters to their initial values.
        """
        self.zom_num = 5  # Set the initial number of zombies
        self.zom_health = 50  # Set the initial zombie health
        self.zom_max_health = 50  # Set the initial maximum zombie health
        self.speed = 2  # Set the initial zombie speed
        self.current_wave = 1  # Reset the wave number to 1