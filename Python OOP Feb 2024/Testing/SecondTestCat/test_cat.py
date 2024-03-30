from unittest import TestCase, main
#from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Buba")

    def test_cat_size_increasing_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cannot_eat_if_fed_raising_error(self):
        self.cat.fed = True  # arrange
        with self.assertRaises(Exception) as ex:
            self.cat.eat()  # act
        self.assertEqual('Already fed.', str(ex.exception))  # asssert

    def test_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleepy_cat_sleeps_and_its_not_sleepy_after_that(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
