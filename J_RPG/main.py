import J_RPG.characters as char
import random as rand

POPULATION_SIZE = 10
RAND_SEED = 9
P_CROSS = 0.9
P_MUTATION = 0.1
MAX_GENERATION = 10
rand.seed(RAND_SEED)
LVL = 10


def game(hero, enemies):
    res = 0
    for lvl in range(10):
        win = battle(hero, enemies[lvl])
        if win:
            res += 1
    return res


def battle(hero, enemy):
    turn = 1
    while True:
        if turn % 2 == 1:
            # Всегда в начале боя накладываем яд на противника
            enemy.hp -= hero.magic

            f = evade(enemy.evasion)
            if not f:
                enemy.hp -= hero.atk
            if enemy.hp <= 0:
                return 1
        else:
            f = evade(hero.evasion)
            if not f:
                hero.hp -= enemy.atk
            if hero.hp <= 0:
                return 0
        turn += 1


def evade(p):
    return rand.choices([1, 0], weights=[p, 100-p])[0]


def generate_population(n):
    heroes = []
    for i in range(n):
        h = [rand.randint(0, 10), 0, 0]

        # 15 очков талантов у каждого героя
        for j in range(15-h[0]):
            h[rand.randint(1, 2)] += 1
        heroes.append(h)
    return heroes


def tournament(pop, pop_res, pop_size):
    elita = []
    for i in range(pop_size):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = rand.randint(0, pop_size-1), rand.randint(0, pop_size-1), rand.randint(0, pop_size-1)
        if pop_res[i1] < pop_res[i2]:
            i1, i2 = i2, i1
        if pop_res[i1] < pop_res[i3]:
            i1, i3 = i3, i1
        elita.append(pop[i1])

    return elita


def cross(par, par2):
    i3 = rand.randint(0, 2)
    if i3 == 0:
        i1, i2 = 1, 2
    elif i3 == 1:
        i1, i2 = 0, 2
    else:
        i1, i2 = 0, 1

    par[i1], par[i2], par2[i1], par2[i2] = par2[i1], par2[i2], par[i1], par[i2]

    # насколько статы родителей отличаются
    dif = par[i1] + par[i2] - par2[i1] - par2[i2]
    while dif != 0:
        if par[i3] > 10 or par2[i3] > 10 or par[i3] < 0 or par2[i3] < 0:
            if dif > 0:
                par[i1] -= dif
                par2[i2] += dif
            else:
                par[i1] += dif
                par2[i2] -= dif
            break
        if dif > 0:
            par[i3] -= 1
            par2[i3] += 1
            dif -= 1
        else:
            par[i3] += 1
            par2[i3] -= 1
            dif += 1

    return par, par2


def mutation(x):
    x = x
    for i in range(3):
        ind = rand.randint(0,2)
        while x[ind] <= 0:
            ind = rand.randint(0,2)
        x[ind] -= 1
        ind2 = rand.randint(0,2)
        x[ind2] += 1
    return x


gen_hero = generate_population(POPULATION_SIZE)
enemies = char.create_enemy(LVL)
results = [0]*POPULATION_SIZE

gen_count = 0
game_pass = 0

while not game_pass and gen_count < MAX_GENERATION:
    for i in range(POPULATION_SIZE):
        super_heroine_x = char.Hero(gen_hero[i])
        results[i] = game(super_heroine_x, enemies)

    if 10 in results:
        game_pass = 1
        stat = gen_hero[results.index(10)]
        print('Игра пройдена поколением: {}'.format(gen_count))
        print('А именно героем со статами:{}, {}, {}'.format(stat[0], stat[1], stat[2]))
        break

    gen_hero = tournament(gen_hero, results, POPULATION_SIZE)

    for par1 in range(0, POPULATION_SIZE, 2):
        for par2 in range(1, POPULATION_SIZE, 2):
            if rand.random() < P_CROSS:
                gen_hero[par1], gen_hero[par2] = cross(gen_hero[par1], gen_hero[par2])
                break

    for i in range(POPULATION_SIZE):
        if rand.random() < P_MUTATION:
            gen_hero[i] = mutation(gen_hero[i])

    gen_count += 1

