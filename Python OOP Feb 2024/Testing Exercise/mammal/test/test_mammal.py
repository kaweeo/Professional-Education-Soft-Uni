from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Dolphin", "fish", "tone")

    def test_correct_init(self):
        self.assertEqual("Dolphin", self.mammal.name)
        self.assertEqual("fish", self.mammal.type)
        self.assertEqual("tone", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method_returning_correct_str(self):
        self.assertEqual("Dolphin is of type fish", self.mammal.info())




if __name__ == "__main__":
    main()