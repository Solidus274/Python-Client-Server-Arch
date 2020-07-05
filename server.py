import json
import socket
import sys
from Lesson_5.log.server_log_config import logger_server
from Lesson_4.common.utils import get_message, send_message
from Lesson_4.common.variables import (ACCOUNT_NAME, ACTION, DEFAULT_PORT,
                                       ERROR, MAX_CONNECTIONS, PRESENCE,
                                       RESPONSE_DEFAULT_IP_ADDRESS, RESPONSE,
                                       TIME, USER)


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клинта, проверяет корректность, возвращает
    словарь-ответ для клиента.
    """
    logger_server.debug('Получение сообщения')
    if (
            ACTION in message and
            message[ACTION] == PRESENCE and
            TIME in message and
            USER in message and
            message[USER][ACCOUNT_NAME] == 'Guest'
    ):
        logger_server.debug('Сообщение корректно')
        return {
            RESPONSE: 200
        }
    logger_server.error('Сообщение некорректно')
    return {
        RESPONSE_DEFAULT_IP_ADDRESS: 400,

        ERROR: 'Bad Request.'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.

    server.py -a 127.0.0.1 -p 8888
    """
    logger_server.debug('Загрузка параметров командной строки')
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        logger_server.warning('Не указан порт для прослушивания')
        sys.exit(1)

    # Загружаем, на какой порт обращаться.
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        logger_server.error('Неверно задан номер порта')
        sys.exit(1)
    except ValueError:
        logger_server.error('Указано неверное значение порта')
        sys.exit(1)

    # Готовим сокет
    transport = socket.socket()
    transport.bind((listen_address, listen_port))
    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)
    logger_server.debug('Прослушивание порта')
    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            logger_server.debug(f'Принято сообщение от клиента {message_from_client}')
            response = process_client_message(message_from_client)
            send_message(client, response)
            logger_server.debug(f'Направлен ответ на сообщение от клиента {response}')
            client.close()
        except (ValueError, json.JSONDecodeError):
            logger_server.error('Принято некорретное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
