class UI:
    def __init__(self, player):
        self.player = player
        self.bar_height = 50
        self.bar_width = 500
        self.bar_colour = "green"
        self.border_colour = "black"
    
    def draw(self, canvas):
        health_percentage = self.player.health / self.player.max_health
        bar_length = health_percentage * self.bar_width
        
        #border
        canvas.draw_polygon([(10, 10), (10 + self.bar_width, 10), (10 + self.bar_width, 10 + self.bar_height), (10, 10 + self.bar_height)], 1, self.border_colour)
        
        #health bar
        canvas.draw_polygon([(10, 10), (10 + bar_length, 10), (10 + bar_length, 10 + self.bar_height), (10, 10 + self.bar_height)], 1, self.bar_colour, self.bar_colour)
        
        # Display text health value
        text_pos = (10, 10 + self.bar_height + 15)
        canvas.draw_text(f"Health: {self.player.health}/{self.player.max_health}", text_pos, 14, "White")