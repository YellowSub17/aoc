import time
import numpy as np
import itertools


import logging
logging.basicConfig(filename='game.log', level=logging.INFO)
logger = logging.getLogger('x')



class Game:

    def __init__(self, hard=False):

        logger.info('Initializing game.')
        self.p_health = 50
        self.p_mana = 500
        self.p_armour = 0
        self.b_health = 55
        self.b_damage = 8
        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0
        self.total_mana_spent = 0
        self.gameover = 0
        self.n_rounds = 0
        self.hard = hard
        self.log_stats()



    def log_stats(self):
        logger.info(f'\tP: hp={self.p_health} mana={self.p_mana} armour={self.p_armour} mana_spent={self.total_mana_spent}')
        logger.info(f'\tB: hp={self.b_health} damage={self.b_damage}')


    def attack(self):
        logger.info(f'Boss attacks, dealing {max(1, self.b_damage-self.p_armour)}.')
        self.p_health -= max(1, self.b_damage-self.p_armour)
        if self.p_health <=0:
            logger.info('Boss has killed player.')
            self.gameover = -1


    def cast_magic_missle(self):
        logger.info('Player casts magic missle dealing 4 damage.')
        if self.p_mana<53:
            logger.info('Attempted to cast magic missle, but not enough mana')
            self.gameover = -1
            return
        self.p_mana -= 53
        self.total_mana_spent += 53
        self.b_health -= 4
        if self.b_health <=0:
            logger.info('Magic missle killed the Boss!')
            self.gameover = 1

    def cast_drain(self):
        logger.info('Player casts drain dealing 2 damage and healing 2 points.')
        if self.p_mana<73:
            logger.info('Attempted to cast drain, but not enough mana')
            self.gameover = -1
            return
        self.p_mana -= 73
        self.total_mana_spent += 73
        self.b_health -= 2
        self.p_health += 2
        if self.b_health <=0:
            logger.info('Drain killed the Boss!')
            self.gameover = 1

    def cast_shield(self):
        logger.info('Player casts shield. Rasing armour to 7 for 6 turns')
        if self.shield_timer >0:
            logger.info('Shield already cast! Player has died.')
            self.gameover = -1
            return

        if self.p_mana<113:
            logger.info('Attempted to cast shield, but not enough mana')
            self.gameover = -1
            return
        self.shield_timer = 6
        self.p_mana -= 113
        self.total_mana_spent += 113
        self.p_armour +=7

    def cast_poison(self):
        logger.info('Player casts poison.')
        if self.poison_timer >0:
            logger.info('Poison already cast! Player has died.')
            self.gameover = -1
            return
        if self.p_mana<173:
            logger.info('Attempted to cast poison, but not enough mana')
            self.gameover = -1
            return
        self.poison_timer = 6
        self.p_mana -= 173
        self.total_mana_spent += 173

    def cast_recharge(self):
        logger.info('Player casts recharge.')
        if self.recharge_timer >0:
            logger.info('Recharge already cast! Player died.')
            self.gameover = -1
            return
        if self.p_mana<229:
            logger.info('Attempted to cast recharge, but not enough mana')
            self.gameover = -1
            return
        self.recharge_timer = 5
        self.p_mana -= 229
        self.total_mana_spent += 229

    def resolve_effects(self):
        logger.info('Resolving effects.')
        if self.shield_timer > 0:
            self.shield_timer -= 1
            logger.info(f'Shield spell has {self.shield_timer} turns remaining.')
            if self.shield_timer == 0:
                logger.info('Shield spell has worn off. Decreasing armour by 7.')
                self.p_armour -= 7

        if self.poison_timer > 0:
            logger.info(f'Poison spell deals 3 damage. {self.poison_timer} turns remaining.')
            self.poison_timer -= 1
            self.b_health -= 3
            if self.poison_timer == 0:
                logger.info('Poison spell has worn off.')

        if self.recharge_timer > 0:
            self.recharge_timer -= 1
            logger.info(f'Recharging mana 101 points. {self.recharge_timer} turns remaining.')
            self.p_mana += 101
            if self.recharge_timer == 0:
                logger.info('Recharge spell has worn off.')



    def round(self, spell):

        self.n_rounds += 1
        if self.n_rounds > 100:
            logger.info(f'BREAK BREAK BREAK')
            exit()

        if self.gameover !=0:
            logger.info(f'Game is already over.')
            return self.gameover, self.total_mana_spent

        logger.info(f'')
        logger.info(f'')
        logger.info(f'')
        logger.info(f'##### ROUND {self.n_rounds}.')
        logger.info(f'## Players turn.')

        if self.hard:
            logger.info(f'Losing 1 point of health from hard mode.')
            self.p_health -=1
            if self.p_health <=0:
                logger.info(f'Player died from hardmode!')
                self.gameover = -1

        if self.gameover != 0:
            self.log_stats()
            return self.gameover, self.total_mana_spent



        self.resolve_effects()

        if self.gameover != 0:
            self.log_stats()
            return self.gameover, self.total_mana_spent


        if spell == 'a':
            self.cast_magic_missle()
        if spell == 'b':
            self.cast_drain()
        if spell == 'c':
            self.cast_shield()
        if spell == 'd':
            self.cast_poison()
        if spell == 'e':
            self.cast_recharge()


        if self.gameover != 0:
            self.log_stats()
            return self.gameover, self.total_mana_spent

        logger.info(f'')
        logger.info(f'## Bosses turn.')

        self.resolve_effects()

        if self.gameover != 0:
            self.log_stats()
            return self.gameover, self.total_mana_spent

        self.attack()

        if self.gameover != 0:
            logger.info(f'')
            self.log_stats()
            return self.gameover, self.total_mana_spent

        logger.info(f'')
        logger.info(f'## Round summary.')
        self.log_stats()

        return 0, self.total_mana_spent


    def run_sim(self, scroll):

        for spell in scroll:
            state, mana = self.round(spell)
            if state!=0:
                break
        return state, mana









if __name__ == '__main__':


#     example_winning_key =('e', 'd', 'c', 'a', 'a', 'd', 'a', 'a', 'a', 'a')
    # g = Game(False)
    # state, mana = g.run_sim(example_winning_key)
    # print(state, mana)




    # example_winning_key = ('e', 'c', 'b', 'e', 'c', 'b', 'b', 'c', 'a', 'a', 'a', 'a', 'a')
    # g = Game(True)
    # state, mana = g.run_sim(example_winning_key)
    # print(state, mana)





    print(time.asctime())




    min_mana = 9999

    hard =False ### ~1 minute
    hard =True ### ~2 minute 10 seconds


    logging.disable(logging.INFO)


    starting_scrolls = list(itertools.product('abcde', repeat=4))
    live_ends = []
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        g = Game(hard=hard)
        state, mana = g.run_sim(starting_scroll)
        if state ==0:
            live_ends.append(starting_scroll)
        if state == 1:
            logging.critical(f'{starting_scroll} {mana}')
            if mana < min_mana:
                min_mana = mana

    print()
    print(f'AAA) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()


    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=3))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')
                if mana < min_mana:
                    min_mana = mana
            if state == 0:
                if mana < min_mana:
                    live_ends.append(game_key)


    print()
    print(f'BBB) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()

    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=3))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')

                if mana < min_mana:
                    min_mana = mana
            if state == 0:

                if mana < min_mana:
                    live_ends.append(game_key)

    print()
    print(f'CCC) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()

    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=1))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')

                if mana < min_mana:
                    min_mana = mana
            if state == 0:

                if mana < min_mana:
                    live_ends.append(game_key)

    print()
    print(f'DDD) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()


    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=1))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')

                if mana < min_mana:
                    min_mana = mana
            if state == 0:

                if mana < min_mana:
                    live_ends.append(game_key)

    print()
    print(f'EEE) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()


    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=1))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')

                if mana < min_mana:
                    min_mana = mana
            if state == 0:

                if mana < min_mana:
                    live_ends.append(game_key)

    print()
    print(f'FFF) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()

    starting_scrolls = live_ends[:]
    live_ends = []
    mid_scrolls = list(itertools.product('abcde', repeat=1))
    for i_starting_scroll, starting_scroll in enumerate(starting_scrolls):
        print(i_starting_scroll, end='\r')
        for i_mid_scroll, mid_scroll in enumerate(mid_scrolls):

            g = Game(hard=hard)
            game_key = starting_scroll+mid_scroll
            state, mana = g.run_sim(game_key)

            if state == 1:
                logging.critical(f'{game_key} {mana}')

                if mana < min_mana:
                    min_mana = mana
            if state == 0:

                if mana < min_mana:
                    live_ends.append(game_key)

    print()
    print(f'GGG) live ends: {len(live_ends)}')
    if len(live_ends)>0:
        print(f'example live_end: {live_ends[-1]}')
    print(f'Current mana min: {min_mana}')
    print()






    print(time.asctime())









