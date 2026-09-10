from unittest import TestCase, mock

from user import User


class TestUser(TestCase):

    def test_init(self):
        steve = User("Steve", 99)

        self.assertEqual(steve.name, "Steve")
        self.assertEqual(steve.age, 99)

    def test_greetings(self):
        steve = User("Steve", 99)

        self.assertEqual(steve.greetings(), "Hello, Steve!")

    def test_birthday(self):
        steve = User("Steve", 99)

        self.assertEqual(steve.age, 99)
        self.assertEqual(steve.birthday(), 100)
        self.assertEqual(steve.age, 100)

    def test_get_friends_impl(self):
        steve = User("Steve", 99)

        with self.assertRaises(NotImplementedError):
            steve.get_friends()

    def test_get_friends_single(self):
        steve = User("Steve", 99)

        with mock.patch("user.fetch_vk_api") as fetch_mock:
            self.assertEqual([], steve.get_friends(name_part="neo"))

            calls = [
                mock.call("/friends", "Steve", part="NEO"),
                mock.call().__iter__(),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

    def test_get_friends_return_value(self):
        steve = User("Steve", 99)

        with mock.patch("user.fetch_vk_api") as fetch_mock:
            fetch_mock.return_value = ["neo", "morf"]

            self.assertEqual(["neo"], steve.get_friends(name_part="neo"))
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            self.assertEqual(["neo", "morf"], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            fetch_mock.reset_mock()
            self.assertEqual(["neo", "morf"], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

    def test_get_friends_value_error(self):
        steve = User("Steve", 99)

        with mock.patch("user.fetch_vk_api") as fetch_mock:
            fetch_mock.side_effect = ValueError("wrong")

            with self.assertRaises(ValueError) as err:
                steve.get_friends(name_part="neo")

            self.assertEqual("wrong", str(err.exception))

            calls = [
                mock.call("/friends", "Steve", part="NEO"),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

    def test_get_friends_side_iter(self):
        steve = User("Steve", 99)

        with mock.patch("user.fetch_vk_api") as fetch_mock:
            fetch_mock.side_effect = [["neo"], [], ["morf"]]

            self.assertEqual(["neo"], steve.get_friends(name_part="neo"))
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            self.assertEqual([], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            fetch_mock.reset_mock()
            self.assertEqual(["morf"], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

    def test_get_friends_side_function(self):
        steve = User("Steve", 99)

        with mock.patch("user.fetch_vk_api") as fetch_mock:
            fetch_mock.side_effect = lambda *a, **kw: ["neo"]

            self.assertEqual(["neo"], steve.get_friends(name_part="neo"))
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            self.assertEqual(["neo"], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part="NEO"),
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

            fetch_mock.reset_mock()
            self.assertEqual(["neo"], steve.get_friends())
            calls = [
                mock.call("/friends", "Steve", part=None),
            ]
            self.assertEqual(calls, fetch_mock.mock_calls)

