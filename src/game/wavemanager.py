from src.game.Zombie import Zombie


class WaveManager:
    """
    A class to manage the waves of zombies in the game.
    """

    def __init__(self):
        self.zom_num = 20
        self.zom_health = 100
        self.speed = 2
        self.current_wave = 1  # Track the current wave number
        self.spawn_cooldown = 900 / self.zom_num

    def new_wave(self, add_health, add_speed):
        self.zom_num = 20 + (10 * self.current_wave)
        self.zom_health += add_health
        self.speed += add_speed
        self.current_wave += 1  # Increment the wave number
        self.spawn_cooldown = 900 / self.zom_num

    def add_zombie(self, zombies, player, shoot):
        if self.zom_num >= 0:
            self.zom_num -= 1
            zombies.append(Zombie(400, 0, player, shoot))

    def reset(self):
        """
        Resets the wave parameters to their initial values.
        """
        self.zom_num = 10  # Set the initial number of zombies
        self.zom_health = 100  # Set the initial zombie health
        self.speed = 2  # Set the initial zombie speed
