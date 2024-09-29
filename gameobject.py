import pygame
from constants import Color

class HealthMixin:

    def __init__(self):
        self.max_health = self.health = None

    def draw_health_bar(self, screen):
        """Draw the health bar above the object."""
        bar_width = self.rect.width
        bar_height = 5
        health_ratio = self.health / self.max_health
        green_width = max(0, int(bar_width * health_ratio))

        bar_x = self.x
        bar_y = self.y - 10  # 10 pixels above the object

        pygame.draw.rect(screen, Color.RED  , (bar_x, bar_y,   bar_width, bar_height))
        pygame.draw.rect(screen, Color.GREEN, (bar_x, bar_y, green_width, bar_height))

    def take_damage(self, damage):
        """Reduce the minion's health by the given damage"""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_destroyed(self):
        """Check if the minion is destroyed (health <= 0)."""
        return self.health <= 0