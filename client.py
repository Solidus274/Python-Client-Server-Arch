import json
import socket
import sys
import time
from Lesson_4.common.utils import get_message, send_message
from Lesson_4.common.variables import (
    ACCOUNT_NAME, ACTION, DEFAULT_IP_ADDRESS, DEFAULT_PORT, ERROR, PRESENCE,
    RESPONSE, TIME, USER)
from Lesson_5.log.client_log_config import logger_client


def create_presence(account_name='Guest'):
    """Функция генерирует запрос о присутствии клиента."""
    logger_client.debug('Генерация запроса о присутствии клиента')
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """Функция разбирает ответ сервера."""
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            logger_client.debug('Ответ от сервера получен')
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    logger_client.error('Код ответа вне допустимого диапазона')
    raise ValueError


def main():
    """Загружаем параметы коммандной строки."""
    logger_client.debug('Старт клиентского приложения')
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            logger_client.warning(f'Неверно задан номер порта: {server_port}')
            raise ValueError
    except IndexError:
        logger_client.warning(f'Номер порта не предоставлен. '
                       f'Применены настройки по умолчанию: {DEFAULT_IP_ADDRESS}, {DEFAULT_PORT}')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        logger_client.error('Указано неверное значение порта')
        sys.exit(1)

    logger_client.debug('Инициализация сокета и обмен')
    transport = socket.socket()
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        logger_client.debug(f'Сообщение отправлено')
    except (ValueError, json.JSONDecodeError):
        logger_client.error('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
