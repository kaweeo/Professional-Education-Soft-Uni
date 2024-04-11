from project.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):
    def setUp(self):
        self.bc = Movie("Bone Collector", 1994, 9.4)
        self.jp = Movie("Jurassic Park", 1998, 9.1)

    def test_init(self):
        self.assertEqual("Bone Collector", self.bc.name)
        self.assertEqual(1994, self.bc.year)
        self.assertEqual(9.4, self.bc.rating)
        self.assertEqual([], self.bc.actors)

    def test_name_setter_raising_ve(self):
        expected = "Name cannot be an empty string!"
        with self.assertRaises(ValueError) as ve:
            self.bcc = Movie("", 1900, 1.1)
        self.assertEqual(expected, str(ve.exception))

    def test_year_setter_raising_ve(self):
        expected = "Year is not valid!"
        with self.assertRaises(ValueError) as ve:
            self.bcc = Movie("BCC", 1658, 1.1)
        self.assertEqual(expected, str(ve.exception))

    def test_actor_method(self):
        self.bc.add_actor("Densel Washington")
        self.bc.add_actor("John Dow")
        self.bc.add_actor("John Dow")
        self.assertEqual(f"John Dow is already added in the list of actors!", self.bc.add_actor("John Dow"))
        exptected_list = ["Densel Washington", "John Dow"]
        self.assertEqual(exptected_list, self.bc.actors)



    def test___gt__(self):
        expected = f'"Bone Collector" is better than "Jurassic Park"'
        self.assertEqual(expected, self.bc.__gt__(self.jp))

        self.jp.rating=100
        expected = f'"Jurassic Park" is better than "Bone Collector"'
        self.assertEqual(expected, self.bc.__gt__(self.jp))

    def test___repr__(self):
        expected = f"Name: Jurassic Park\n" \
                   f"Year of Release: 1998\n" \
                   f"Rating: 9.10\n" \
                   f"Cast: John Dow, Test Test, Test2 Test2"
        self.jp.add_actor("John Dow")
        self.jp.add_actor("Test Test")
        self.jp.add_actor("Test2 Test2")
        self.assertEqual(expected, self.jp.__repr__())


if __name__ == "__main__":
    main()
