from django.test import TestCase
from ..models import Knight, Archer, Catapult, Army
from ..views import GameActions


class GameTestCase(TestCase):

    def setUp(self):

        # Units
        self.knight1 = Knight.objects.create(sword=10)
        self.knight2 = Knight.objects.create(sword=10)
        self.archer1 = Archer.objects.create(damage=25, lives=50, sword=10)
        self.catapult1 = Catapult.objects.create(damage=50, lives=200)

        #  Armies
        #     Army 1
        self.army1 = Army.objects.create()
        self.army1.knights.add(self.knight1, self.knight2)
        self.army1.archers.add(self.archer1)

        #     Army 2
        self.army2 = Army.objects.create(armyAdd=self.army1)
        self.army2.catapults.add(self.catapult1)

        # Game actions
        self.game = GameActions()

    def test_extra_damage(self):

        self.assertEqual(self.knight1.activate_extra_damage(
                            self.knight1.sword), 30)
        self.assertEqual(self.knight1.deactivate_extra_damage(
                            self.knight1.sword), 20)
        self.assertEqual(self.archer1.activate_extra_damage(
                            self.archer1.sword), 35)
        self.assertEqual(self.archer1.deactivate_extra_damage(
                            self.archer1.sword), 25)

    def test_life_status(self):

        self.assertEqual(self.archer1.alive, True)
        self.archer1.dead
        self.assertEqual(self.archer1.alive, False)
        self.assertEqual(self.archer1.lives, 0)
        self.assertEqual(self.archer1.damage, 0)

    def test_armies(self):

        self.assertEqual(self.army1.knights.count(), 2)
        self.assertEqual(self.army1.archers.count(), 1)
        self.assertEqual(self.army1.catapults.count(), 0)
        self.assertEqual(self.army2.catapults.count(), 1)
        self.assertEqual(self.army2.armyAdd.__dict__['id'], 1)

    def test_attacks(self):

        # Unit VS Army
        self.assertEqual(
            self.game.attack_check_OK(self.knight1, self.army1),
            False)

        # Army VS Unit
        self.assertEqual(
            self.game.attack_check_OK(self.army2, self.knight2),
            True)

        # Life Unit VS Life Unit
        self.assertEqual(
            self.game.attack_check_OK(self.knight1, self.knight2),
            True)

        # Dead Unit VS Life Unit
        self.knight1.dead
        self.assertEqual(
            self.game.attack_check_OK(self.knight1, self.knight2),
            False)

        # Life Unit VS Dead Unit
        self.assertEqual(
            self.game.attack_check_OK(self.archer1, self.knight1),
            False)
