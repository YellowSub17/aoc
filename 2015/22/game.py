


import logging

logging.basicConfig(filename='game.log', level=logging.INFO)
logger = logging.getLogger()



class Game:

    def __init__(self):
        logger.info('Initializing game')
        self.p_health = 50
        self.p_mana = 500
        self.p_armour = 0
        self.b_health = 55
        self.b_damage = 8
        self.shield_timer = 0
        self.poison_timer = 0
        self.recharge_timer = 0

        self.total_mana_spent = 0

        self.n_turns = 0


    def attack(self):

        logger.info('Boss attacks!')
        self.p_health -= max(1, self.b_damage-self.p_armour)


    def cast_magic_missle(self):
        logger.info('Player casts magic missle.')
        self.p_mana -= 53
        self.total_mana_spent += 53
        self.b_health -= 4

    def cast_drain(self,opp):
        logger.info('Player casts drain.')
        self.p_mana -= 74
        self.total_mana_spent += 74
        self.b_health -= 2
        self.p_health += 2

    def cast_shield(self):
        logger.info('Player casts shield.')
        if self.sheild_timer >0:
            logger.info('Sheild already cast! Player died.')
            self.p_health = 0
            return
        self.shield_timer = 6
        self.p_mana -= 113
        self.total_mana_spent += 113
        self.p_armour +=7

    def cast_poison(self, opp):
        logger.info('Player casts poison.')
        if self.poison_timer >0:
            logger.info('Poison already cast! Player died.')
            self.p_health = 0
            return
        self.poison_timer = 6
        self.p_mana -= 173
        self.total_mana_spent += 173

    def cast_recharge(self, opp):
        logger.info('Player casts recharge.')
        if self.recharge_timer >0:
            logger.info('Recharge already cast! Player died.')
            self.p_health = 0
            return
        self.recharge_timer = 5
        self.p_mana -= 229
        self.total_mana_spent += 229

    def resolve_effects(self):
        logger.info('Resolving effects.')
        if self.sheild_timer > 0:
            self.sheild_timer -= 1
            logger.info(f'Sheild spell has {self.sheild_timer} turns remaining.')
        if self.sheild_timer == 0:
            logger.info('Sheild spell has worn off.')
            self.armour -= 7
        if self.poison_timer > 0:
            logger.info(f'Poison spell deals damage. {self.poison_timer} turns remaining.')
            self.poison_timer -= 1
            self.b_health -= 3
        if self.recharge_timer > 0:
            self.recharge_timer -= 1
            logger.info(f'Recharging mana. {self.recharge_timer} turns remaining.')
            self.p_mana += 101



    def turn(self, spell):
        self.n_turns += 1

        self.resolve_effects()
        if spell == 0:
            self.cast_magic_missle()
        if spell == 1:
            self.cast_drain()
        if spell == 2:
            self.cast_sheild()
        if spell == 3:
            self.cast_poison()
        if spell == 4:
            self.cast_recharge()

        self.resolve_effects()
        self.attack()





if __name__ == '__main__':
    g = Game()












