class waves:
   
   #there for num of zombies per wave
   #their max hp and speed
    def __init__(self, zom_num, zom_health, zom_max_health, speed):
      self.zom_num = zom_num
      self.zom_health = zom_health
      self.zom_max_health = zom_max_health
      self.speed = speed

    #updates the zombies
    def update(self,add_hp, add_speed):
      self.zom_health += add_hp
      self.zom_max_health += add_hp
      self.speed += add_speed
