import logging
import sys

# Создаем объект-логгер:
logger_client = logging.getLogger('app.client')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s ")

# Создаем файловый обработчик логирования:
fh = logging.FileHandler("app.client.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger_client.addHandler(fh)
logger_client.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger_client.addHandler(console)