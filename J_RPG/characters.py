import random as rand


class Char:
    def __init__(self, abil):
        self.hp = abil[0] * 10 + 100
        self.atk = 15 + abil[0]
        self.evasion = 5 * abil[1]


class Hero(Char):
    def __init__(self, abil):
        super().__init__(abil)
        self.magic = abil[2]


class Enemy(Char):
    def __init__(self, abil, lvl):
        super().__init__(abil)
        self.hp += 100 * lvl
        self.atk += 6 * lvl


def create_hero(abil):
    return Hero(abil)


def create_enemy(lvl):
    enemy = []
    for i in range(lvl):
        stat = [rand.randint(0, 8)]
        stat.append(8 - stat[0])
        enemy.append(Enemy(stat, lvl))

    return enemy
