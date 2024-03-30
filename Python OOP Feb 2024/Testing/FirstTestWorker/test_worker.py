from unittest import TestCase, main


from worker import Worker


class TestWorker(TestCase):

    def setUp(self):  # runs before each test case
        self.worker = Worker("JohnDow", 20_000, 100)

    def test_correct_init(self):
        self.assertEqual("JohnDow", self.worker.name)
        self.assertEqual(20_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_incrementing_energy_when_rest_method_is_called(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_raising_error_when_worker_tries_to_work_with_no_energy(self):
        self.worker.energy = 0  # Arrange

        with self.assertRaises(Exception) as ex:
            self.worker.work()  # Act

        self.assertEqual('Not enough energy.', str(ex.exception))  # Assert

    def test_workers_money_increased_when_work_method_is_called(self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary,
                         msg="This is test msg, if my test is passed maybe should appear")
        expected_energy_after_work = 99
        self.assertEqual(expected_energy_after_work, self.worker.energy)

    def test_get_info_method_returning_the_correct_str(self):
        self.assertEqual(f'JohnDow has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
