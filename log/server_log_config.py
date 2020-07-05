import logging.handlers
import sys

# Создаем объект-логгер:
logger_server = logging.getLogger('app.server')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s ")

# Создаем файловый обработчик логирования:
re_write = logging.handlers.TimedRotatingFileHandler("app.server.log", when='D', interval=1, encoding='utf-8')
re_write.setLevel(logging.DEBUG)
re_write.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger_server.addHandler(re_write)
logger_server.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger_server.addHandler(console)