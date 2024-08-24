




class Player:

    def __init__(self, health, mana, damage):

        self.health = health
        self.mana = mana
        self.damage = damage
        self.armour = 0
        self.effects = []



    def attack(self, opp):
        opp.health -= max(1, self.damage-opp.armour)



    def magic_missle(self, opp):
        self.mana -= 53
        opp.health -=4

    def drain(self,opp):
        self.mana -=74
        opp.health -=2
        self.health +=2


class Effect:

    def __init__(self, name, duration):
        self.name=name
        self.duration=duration







class Game:
    def __init__(self):
        self.boss = Boss()
        self.player = Player()
        self.effects = []





if __name__ == '__main__':
    p1 = Player(50, 500, 0)
    boss = Boss(55, 0, 8)
