import unittest

from Lesson_4.client import main, process_ans, create_presence


class TestClient(unittest.TestCase):

    """Тест для проверки типа возвращаемых данных"""
    def test_create_presence(self):
        self.assertEqual(type(create_presence()), dict)

    """Тест для проверки ошибки неверного ответа от сервера"""
    def test_process_ans(self):
        message = 'hello'
        with self.assertRaises(ValueError):
            process_ans(message)

    """Тест для проверки ошибки наличия подключения к серверу"""
    def test_main(self):
        with self.assertRaises(ConnectionRefusedError):
            main()


if __name__ == "__main__":
    unittest.main()



