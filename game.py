
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def __str__(self):
        return f"{self.name} (Health: {self.health})"


class Game:
    def __init__(self, team1, team2):
        self.team1 = Team(team1)
        self.team2 = Team(team2)

    def shoot(self, shooter, target):
        damage = random.randint(1, 20)
        target.take_damage(damage)
        print(f"{shooter.name} shoots {target.name} for {damage} damage!")

    def play(self):
        while self.team1.is_alive() and self.team2.is_alive():
            self.shoot(self.team1, self.team2)
            if not self.team2.is_alive():
                break
            self.shoot(self.team2, self.team1)

        winner = self.team1 if self.team1.is_alive() else self.team2
        print(f"\n{winner.name} wins the game!")

if __name__ == "__main__":
    game = Game("Team A", "Team B")
    game.play()
