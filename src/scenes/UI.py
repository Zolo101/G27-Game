class UI:
    def __init__(self, player):
        self.player = player
        self.health_bar_height = 50
        self.health_bar_width = 500
        self.health_bar_colour = "green"
        self.health_bar_border_colour = "gold"
        self.health_bar_background_colour = "red"

    def draw(self, canvas, night_count):
        health_percentage = self.player.health / self.player.max_health
        current_health_bar_length = health_percentage * self.health_bar_width

        #background bar
        canvas.draw_polygon([(10, 10), (10 + self.health_bar_width, 10), (10 + self.health_bar_width, 10 + self.health_bar_height), (10, 10 + self.health_bar_height)], 1, self.health_bar_background_colour, self.health_bar_background_colour)

        #health bar
        canvas.draw_polygon([(10, 10), (10 + current_health_bar_length, 10), (10 + current_health_bar_length, 10 + self.health_bar_height), (10, 10 + self.health_bar_height)], 1, self.health_bar_colour, self.health_bar_colour)

        #border
        canvas.draw_polygon([(10, 10), (10 + self.health_bar_width, 10), (10 + self.health_bar_width, 10 + self.health_bar_height), (10, 10 + self.health_bar_height)], 5, self.health_bar_border_colour)

        # money colour
        money_colour = "Green"

        if self.player.money == 0:
            money_colour = "Red"

        # money text
        canvas.draw_text(f"£{self.player.money}", (10, 120), 60, money_colour)

        # Display text health value
        text_pos = (13, self.health_bar_height)
        canvas.draw_text(f"Health: {self.player.health}/{self.player.max_health}", text_pos, 30, "White")

        # nights text
        canvas.draw_text(f"Night {night_count}", (13, self.health_bar_height + 100), 30, "Blue")
        #canvas.draw_text(f"Time Survived: {self.player.time_survived}", (422, 568), 60, "Black")
        #canvas.draw_text(f"Time Survived: {self.player.time_survived}", (425, 570), 60, "Yellow")