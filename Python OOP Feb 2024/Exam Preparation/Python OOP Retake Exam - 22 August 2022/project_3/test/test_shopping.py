from project.shopping_cart import ShoppingCart

from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.test = ShoppingCart("Kinky", 1000.0)

    def test_init(self):
        self.assertEqual("Kinky", self.test.shop_name)
        self.assertEqual(1000.0, self.test.budget)
        self.assertEqual({}, self.test.products)

    def test_shop_name_raising_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.shop_name = "kinky"
        self.assertEqual(
            "Shop must contain only letters and must start with capital letter!",
            str(ve.exception)
        )

        with self.assertRaises(ValueError) as ve:
            self.test.shop_name = "KL_inky"
        self.assertEqual(
            "Shop must contain only letters and must start with capital letter!",
            str(ve.exception)
        )

    def test_add_to_cart_working(self):
        expected = "beer product was successfully added to the cart!"

        self.assertEqual(expected, self.test.add_to_cart("beer", 2.2))

        self.assertEqual({"beer": 2.2}, self.test.products)

    def test_add_to_cart_raising_ValuerError(self):
        expected = f"Product computer cost too much!"

        with self.assertRaises(ValueError) as ve:
            self.test.add_to_cart("computer", 999.99)

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({}, self.test.products)

    def test_remove_from_card_working(self):
        self.test.add_to_cart("beer", 2.2)

        expected = "Product beer was successfully removed from the cart!"

        self.assertEqual(expected, self.test.remove_from_cart("beer"))
        self.assertEqual({}, self.test.products)

    def test_remove_from_cart_raising_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.remove_from_cart("beer")
        self.assertEqual("No product with name beer in the cart!", str(ve.exception))

    def test__add__(self):
        self.two = ShoppingCart("Two", 9.99)
        self.two.add_to_cart("meze", 1.99)
        self.test.add_to_cart("beer", 2)

        self.test_two = self.test.__add__(self.two)

        expected_name = "KinkyTwo"
        self.assertEqual(expected_name, self.test_two.shop_name)
        self.assertEqual(1009.99, self.test_two.budget)

        expected_products = {
            "meze": 1.99,
            "beer": 2
        }
        self.assertEqual(expected_products, self.test_two.products)

        expected_updated_products = {
            "meze": 1.99,
            "beer": 2,
            "coke": 2,
            "nuts": 5,
        }

        self.test_two.products.update({"coke": 2, "nuts": 5})

        self.assertEqual(expected_updated_products, self.test_two.products)

        expected_updated_products_other = {
            "meze": 1.99,
            "beer": 2,
            "coke": 2,
            "nuts": 5,
            "nuggets": 15.2
        }

        self.test_two.products.update({"nuggets": 15.2})
        self.assertEqual(expected_updated_products_other, self.test_two.products)

    def test_buy_products_raising_value_error(self):
        self.test.products = {
            "meze": 1.99,
            "beer": 2,
            "coke": 2,
            "nuts": 5,
            "nuggets": 1500.2
        }

        expected_msg = "Not enough money to buy the products! Over budget with 511.19lv!"

        with self.assertRaises(ValueError) as ve:
            self.test.buy_products()
        self.assertEqual(expected_msg, str(ve.exception))
        products = {
            "meze": 1.99,
            "beer": 2,
            "coke": 2,
            "nuts": 5,
            "nuggets": 1500.2
        }
        self.assertEqual(products, self.test.products)

    def test_buy_products_successfully(self):
        self.test.products = {
            "meze": 1.99,
            "beer": 2,
            "coke": 2,
            "nuts": 5,
            "nuggets": 500.2
        }

        expected_msg = 'Products were successfully bought! Total cost: 511.19lv.'
        self.assertEqual(expected_msg, self.test.buy_products())


if __name__ == "__main__":
    main()
