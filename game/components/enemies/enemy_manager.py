from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self):
        if not self.enemies: # [] {} 0 "" -> false | [1] {1: 1} 1 -2 "asd" -> true
            self.enemies.append(Enemy())

        # if len(self.enemies) == 0:
        #     pass

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)