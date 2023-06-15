import random
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies: # [] {} 0 "" -> false | [1] {1: 1} 1 -2 "asd" -> true
            enemy_variant = random.randint(1, 2)
            self.enemies.append(Enemy(enemy_variant))

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)