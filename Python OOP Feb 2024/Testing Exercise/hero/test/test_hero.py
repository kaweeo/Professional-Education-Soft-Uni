from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("hero", 3, 100, 10)
        self.enemy_hero = Hero("enemy", 2, 80, 5)

    def test_correct_init(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_method_exeption_throwing(self):
        self.hero.username = "enemy"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_raising_value_error_if_health_less_then_or_equal_to_zero(self):
        self.hero.health = -10

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(
            "Your health is lower than or equal to 0. You need to rest",
            str(ve.exception)
        )

    def test_battle_method_rasing_value_error_if_enemy_hero_with_negative_or_zero_health(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(
            f"You cannot fight {self.enemy_hero.username}. He needs to rest",
            str(ve.exception)
        )

    def test_battle_method_if_no_errors_and_exceptions_are_raised_and_is_draw(self):
        self.hero = Hero("hero", 3, 20, 10)
        self.enemy_hero = Hero("enemy", 2, 20, 15)
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

    def test_battle_method_if_no_errors_and_exceptions_are_raised_and_hero_wins(self):
        self.hero = Hero("hero", 3, 100, 10)
        self.enemy_hero = Hero("enemy", 2, 20, 15)
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))
        self.assertEqual(4, self.hero.level)
        self.assertEqual(75, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_method_if_no_errors_and_exceptions_are_raised_and_enemy_hero_wins(self):
        self.hero = Hero("hero", 1, 10, 10)
        self.enemy_hero = Hero("enemy", 2, 20, 15)
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))
        self.assertEqual(3, self.enemy_hero.level)
        self.assertEqual(15, self.enemy_hero.health)
        self.assertEqual(20, self.enemy_hero.damage)

    def test_str_method_for_correct_retuning(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                 f"Health: {self.hero.health}\n" \
                 f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, str(self.hero))


if __name__ == "__main__":
    main()
