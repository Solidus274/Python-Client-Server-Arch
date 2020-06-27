import unittest
from Lesson_4.common.utils import get_message


class TestUtils(unittest.TestCase):

    """Тест для проверки ошибки неверного атрибута"""
    def test_get_message(self):
        message = 'hello'
        with self.assertRaises(AttributeError):
            get_message(message)


if __name__ == "__main__":
    unittest.main()